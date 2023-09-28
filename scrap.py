import requests
from bs4 import BeautifulSoup
import json
import markdownify

# Function to extract content from a page
def extract_content(url):
    try:
        print("URL" , url)
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract title
            ts = soup.find_all("div",{"class" : "wp-block-group is-layout-flow wp-block-group-is-layout-flow"})
            title = []
            title.append(ts[1].h2.text)
            title.append(ts[2].h2.text)
            title.append(ts[3].h2.text)
            title.append(ts[4].h2.text)
            title.append(ts[5].h2.text)
            
            
            # Extract content
            cont = soup.find_all("p",{"class" : "wp-block-post-excerpt__excerpt"})
            print(cont)
            content = []
            content.append(cont[0].text)
            content.append(cont[1].text)
            content.append(cont[2].text)
            content.append(cont[3].text)
            content.append(cont[4].text)

            # Convert tables to markdown
            tables = soup.find_all('table')
            for table in tables:
                table.replace_with(markdownify.markdownify(str(table)))
            
            return {'title': title, 'content': content}
        else:
            return None
    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# Function to scrape multiple pages and save to a JSON file
def scrape_and_save(num_pages):
    data = []
    base_url = "https://blog.tax2win.in/"
    
    for page_num in range(1, num_pages + 1):
        page_url = f"{base_url}?query-19-page={page_num}/"
       
        page_data = extract_content(page_url)
        
        if page_data:
            print(page_data)
            data.append(page_data)
    
    with open('tax2win_blog.json', 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    num_pages_to_scrape = 5
    scrape_and_save(num_pages_to_scrape)
 
 
