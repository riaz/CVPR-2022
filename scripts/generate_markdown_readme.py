"""
The purpose of this script is to use the py-markdown library to 
create an index for the CVPR pages
"""

import json
import os
import pandas as pd
from markdownTable import markdownTable

CVPR_DATA  = "../cvpr_data.json"
CVPR_DATA_W_PDF = "../cvf_data_w_pdf.json"
TARGET_DIR = "../data"


with open(CVPR_DATA) as cvpr_f, open(CVPR_DATA_W_PDF) as cvpr_pdf_f, open("sample.md", "w") as md:
    cvpr_data = json.load(cvpr_f)
    cvpr_pdf_data = json.load(cvpr_pdf_f)

    for paper_cat, papers in cvpr_data.items():        
        
        md.write(f"### {paper_cat} \n")

        # generating the dataframe
        table = []

        for paper in papers:
            paper_title = paper['title'] 
            paper_id = paper['paperId']
            if paper_title in cvpr_pdf_data:
                paper_link = cvpr_pdf_data[paper_title]['url']
                md_link = f"![Paper](paper_link)"
                table.append([paper_id, paper_title, paper_link])
        df = pd.DataFrame(table, columns=["Paper Id", "Paper Title", "Link"])
        content  = markdownTable(df.to_dict(orient='records')).getMarkdown()

        md.write(content + "\n\n")