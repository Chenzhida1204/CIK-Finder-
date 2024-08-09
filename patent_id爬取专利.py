import os
from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from os.path import join
import time
def get_script_path():
    return os.path.dirname(os.path.abspath(__file__))

def initialize_webdriver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    
    # 设置Chrome浏览器的路径
    chrome_options.binary_location = r"C:/Users/86132/AppData/Local/Google/Chrome/Application/chrome.exe"
    
    # 使用WebDriver Manager来管理ChromeDriver
    service = ChromeService(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

def build_patent_url(patent_id):
    return f'https://patents.google.com/patent/US{patent_id}B2'

def fetch_patent_page(driver, url, patent_id):
    driver.get(url)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
    page_source = driver.page_source
    
    # 解析网页内容
    bs = BeautifulSoup(page_source, 'html.parser')
    title = bs.title.text if bs.title else 'No Title'

    return driver.page_source

def parse_patent_info(html):
    bs = BeautifulSoup(html, 'html.parser')
    def get_text_or_none(selector):
        element = bs.select_one(selector)
        return element.text.strip() if element else 'Not Found'

    title = get_text_or_none('h1#title')
    abstract = get_text_or_none('section#abstract.patent-text')
    inventors = ', '.join([elem['content'] for elem in bs.select('meta[name="DC.contributor"][scheme="inventor"]')])
    assignee = bs.select_one('meta[name="DC.contributor"][scheme="assignee"]')['content'] if bs.select_one('meta[name="DC.contributor"][scheme="assignee"]') else None
    date_submitted = bs.select_one('meta[name="DC.date"][scheme="dateSubmitted"]')['content'] if bs.select_one('meta[name="DC.date"][scheme="dateSubmitted"]') else None
    issue_date = bs.select_one('meta[name="DC.date"][scheme="issue"]')['content'] if bs.select_one('meta[name="DC.date"][scheme="issue"]') else None

    return {
        'Title': title,
        'Abstract': abstract,
        'Inventors': inventors,
        'Assignee': assignee,
        'Date Submitted': date_submitted,
        'Issue Date': issue_date,
    }

# 假设的 get_text_or_none 函数实现

def main():
    script_path = get_script_path()
    driver = initialize_webdriver()
    
    try:
        # 从CSV文件中读取专利ID
        patent_ids_df = pd.read_csv(r'd:/桌面/分割后的文件/chunk_1.csv')
        # 移除包含 NaN 值的行
        patent_ids_df.dropna(subset=['patent_id'], inplace=True)
        # 确保 patent_id 列的数据类型正确
        patent_ids_df['patent_id'] = patent_ids_df['patent_id'].astype(int)

        all_patent_info = []

        for index, patent_id in enumerate(patent_ids_df['patent_id']):
            patent_id = int(patent_id)
            if patent_id is not None:  # 检查patent_id是否为有效值
                patent_url = build_patent_url(patent_id)
                html = fetch_patent_page(driver, patent_url, patent_id)
                patent_info = parse_patent_info(html)
                patent_info['Patent ID'] = patent_id
                patent_info['URL'] = patent_url
                all_patent_info.append(patent_info)
                print(f'已爬取第{len(all_patent_info)}个专利：{patent_id}')
                                # 每爬取一个专利后等待1秒
                time.sleep(0.5)
                
                # 每爬取10个专利后等待10秒
                if (index + 1) % 10 == 0:
                    time.sleep(2)
            else:
                print('无效的专利ID，跳过')
                break
        df = pd.DataFrame(all_patent_info)
        output_dir = r'd:/桌面/专利相关数据'
        # 检查目录是否存在，如果不存在，则创建它
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_path = join(output_dir, 'part_1_patent_information.csv')
        df.to_csv(output_path, index=False)
        print(f'所有专利信息已保存到 {output_path}')

    finally:
        driver.quit()

if __name__ == '__main__':
    main()




