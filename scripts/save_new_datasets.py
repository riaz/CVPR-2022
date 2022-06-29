import json
import requests
import pandas as pd
from bs4 import BeautifulSoup

if __name__ == '__main__':
    conference = "CVPR2022"
    columns = ["paperId", "Title", "Contributors", "Link"]
    res = requests.get("https://cvpr2022.thecvf.com/dataset-contributions")
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, "html.parser")
        results = soup.find_all("tr")
        dataset = []        
        for idx,res in enumerate(results):
            if idx == 0:
                continue 
            out = []
            for key, col in zip(columns, res.find_all("td")):
                if key == "Link":                    
                    link = col.find("a", href=True)
                    out.append(link['href'])                    
                else:
                    out.append(col.text)
            dataset.append(out)
    df = pd.DataFrame(dataset, columns=columns)
    df.to_csv('../cvpr_2022_dataset.csv', index=False)