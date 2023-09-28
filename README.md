# Lamarr-Data-Science-screening-project

This Python script scrapes content from multiple pages of the Tax2Win blog and saves it to a JSON file. 

1. Importing Libraries: The script starts by importing the necessary Python libraries, including `requests` for making HTTP requests, `BeautifulSoup` for parsing HTML content, `json` for handling JSON data, and `markdownify` for converting HTML tables to Markdown format.

2. Content Extraction:** The `extract_content` function takes a URL as input, fetches the HTML content from that URL, and then uses BeautifulSoup to extract the titles and content paragraphs from the Tax2Win blog posts. It also identifies and converts HTML tables within the content to Markdown format using the `markdownify` library.

3. Scraping Multiple Pages: The `scrape_and_save` function iterates over a specified number of pages (in this case, five) on the Tax2Win blog by constructing the page URLs. For each page, it calls `extract_content` to retrieve and parse the content, saving it to the `data` list.

4. Data Storage: The extracted data, including titles and content, is stored in a structured format (list of dictionaries) within the `data` variable.

5. JSON File Creation: Finally, the script saves the collected data to a JSON file named 'tax2win_blog.json,' ensuring it's encoded in UTF-8 and formatted with proper indentation.

