from bs4 import BeautifulSoup

import pandas as pd

import requests

url = "https://www.amazon.com/MSI-Thin-Bezel-Quad-Core-i5-10300H-Keyboard/dp/B098JFL5DK"


def get_product_details(product_amazon_url):
    """
    takes url, 
    return : dictionary of product details
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/ 537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

    
    resp = requests.get(product_amazon_url, headers=headers)
    s = BeautifulSoup(resp.content,features="html.parser")

    soup = BeautifulSoup(resp.content, 'html.parser')
    img_results = soup.find_all('div', {'class': 'imgTagWrapper'})
    
    try:
        img_url = img_results[0].img['src']
    except:
        img_url = "Not available"


    



    # #print(img_url)
    # results2 = soup.find_all('span', {'class': 'a-icon-alt'})
    # #rating = results2[0].text
    
    

    # product_details = {}
    # product_details['image_url'] = img_url
    # #product_details['rating'] = rating
    


    print(img_url)
    table_data = s.find('table',class_="a-keyvalue prodDetTable" ) #class_="a-keyvalue prodDetTable"
    print(table_data)
    # rows = table_data.find_all('tr')

    
get_product_details(url)

    # for i in rows:
    #     td = i.find('td')
    #     th = i.find('th')
    #     td_text = td.text.encode("ascii", "ignore")
    #     td_text = td_text.decode().strip()
    #     th_text = th.text.strip()
    #     product_details[th_text] = td_text    
    
    # #print(type(product_details))

    # return product_details
    
    
    
   



