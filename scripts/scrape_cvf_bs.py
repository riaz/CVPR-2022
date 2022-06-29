import json
import requests
from bs4 import BeautifulSoup

def save_file(link):
    # Saving the PDF File
    local_file_name = "../data/" + link['href'].strip().split("/")[-1]
    uri = "https://openaccess.thecvf.com/" + link['href']
    r = requests.get(uri)
    with open(local_file_name, "wb") as code:
        code.write(r.content)
    return local_file_name

if __name__ == '__main__':
    paper = {}
    conference = "CVPR2022"
    res = requests.get("http://openaccess.thecvf.com/"+conference+"?day=all")
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, "html.parser")
        results = soup.find_all("dt", class_="ptitle")
        for res in results:
            print(res.text)
            paper[res.text] = {}
            anchor = res
            authors = anchor.find_next_sibling("dd")
            paper[res.text]["authors"] = []
            for auth in authors.find_all("a"):
                #print(auth.text)
                paper[res.text]["authors"].append(auth.text)
            links = authors.find_next_sibling("dd")
            for link in links.find_all("a", string="pdf", href=True):
                local_save_location = save_file(link)
                paper[res.text]["url"] = local_save_location
                #print(link['href'])
    with open("../cvf_data_w_pdf.json", "w") as fw:
        json.dump(paper, fw, ensure_ascii=False, indent=4)