
# 谷歌专利爬虫

该Python脚本旨在自动化从谷歌专利（Google Patents）使用专利ID抓取专利信息的过程。脚本利用Selenium进行网页自动化，并使用BeautifulSoup解析HTML内容。提取的信息会保存到CSV文件中以供进一步分析。

## 功能特性

- **自动化网页爬取**: 脚本自动导航到与提供的专利ID对应的谷歌专利页面。
- **专利数据提取**: 提取每个专利的标题、摘要、发明人、受让人、提交日期和发布日期。
- **数据存储**: 提取的数据保存到CSV文件中，方便访问和分析。
- **可定制**: 可以轻松修改脚本以提取额外的信息或处理不同类型的专利ID。

## 需求

- Python 3.x
- Selenium
- BeautifulSoup
- pandas
- ChromeDriver（通过WebDriver Manager管理）

## 设置

1. 安装所需的Python库:
   ```bash
   pip install selenium beautifulsoup4 pandas webdriver-manager
   ```

2. 确保您已在计算机上安装了Google Chrome。

3. 在脚本中设置`chrome.exe`的路径:
   ```python
   chrome_options.binary_location = r"C:/Users/86132/AppData/Local/Google/Chrome/Application/chrome.exe"
   ```

## 使用方法

1. 准备一个包含`patent_id`列的CSV文件，该列包含要抓取的专利ID。

2. 修改脚本以指向您的CSV文件位置:
   ```python
   patent_ids_df = pd.read_csv(r'd:/桌面/分割后的文件/chunk_1.csv')
   ```

3. 运行脚本:
   ```bash
   python patent_scraper.py
   ```

4. 脚本会将抓取的专利数据保存到指定输出目录的CSV文件中:
   ```bash
   d:/桌面/专利相关数据/part_1_patent_information.csv
   ```

## 自定义

- **等待时间**: 您可以调整爬取操作之间的等待时间，以避免被谷歌专利屏蔽:
  ```python
  time.sleep(0.5)  # 每爬取一个专利等待0.5秒
  time.sleep(2)    # 每爬取10个专利等待2秒
  ```

- **输出目录**: 通过修改此行更改输出目录:
  ```python
  output_dir = r'd:/桌面/专利相关数据'
  ```

## 许可

此项目在MIT许可下获得许可 - 有关详细信息，请参阅[LICENSE](LICENSE)文件。

## 鸣谢

- [Selenium](https://www.selenium.dev/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [pandas](https://pandas.pydata.org/)
