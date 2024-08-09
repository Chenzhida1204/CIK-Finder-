
# Patent Scraper for Google Patents

This Python script is designed to automate the process of scraping patent information from Google Patents using patent IDs. The script utilizes Selenium for web automation and BeautifulSoup for parsing the HTML content. The extracted information is saved into a CSV file for further analysis.

## Features

- **Automated Web Scraping**: The script automatically navigates to the Google Patents pages corresponding to the provided patent IDs.
- **Patent Data Extraction**: It extracts the title, abstract, inventors, assignee, date submitted, and issue date for each patent.
- **Data Storage**: The extracted data is saved into a CSV file for easy access and analysis.
- **Customizable**: The script can be easily modified to extract additional information or to handle different types of patent IDs.

## Requirements

- Python 3.x
- Selenium
- BeautifulSoup
- pandas
- ChromeDriver (managed by WebDriver Manager)

## Setup

1. Install the required Python packages:
   ```bash
   pip install selenium beautifulsoup4 pandas webdriver-manager
   ```

2. Ensure you have Google Chrome installed on your machine.

3. Set the `chrome.exe` path in the script:
   ```python
   chrome_options.binary_location = r"your chrome way"
   ```

## Usage

1. Prepare a CSV file with a column named `patent_id` containing the patent IDs you want to scrape.

2. Modify the script to point to the location of your CSV file:
   ```python
   patent_ids_df = pd.read_csv(r'your file name')
   ```

3. Run the script:
   ```bash
   python patent_scraper.py
   ```

4. The script will save the scraped patent data into a CSV file in the specified output directory:
   ```bash
   out put way
   ```

## Customization

- **Waiting Time**: You can adjust the waiting time between scraping operations to avoid being blocked by Google Patents:
  ```python
  time.sleep(0.5)  # Wait 0.5 seconds between scraping each patent
  time.sleep(2)    # Wait 2 seconds after every 10 patents
  ```

- **Output Directory**: Change the output directory by modifying this line:
  ```python
  output_dir = "output file way"
  ```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Selenium](https://www.selenium.dev/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)
- [pandas](https://pandas.pydata.org/)
