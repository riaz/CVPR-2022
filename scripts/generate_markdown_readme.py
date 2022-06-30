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
README = "../README.md"


with open(CVPR_DATA) as cvpr_f, open(CVPR_DATA_W_PDF) as cvpr_pdf_f, open(README, "w") as md:
    cvpr_data = json.load(cvpr_f)
    cvpr_pdf_data = json.load(cvpr_pdf_f)

    md.write("# CVPR-2022\n")
    md.write("Papers and  Code from CVPR 2022, including scripts to extract them\n\n")

    for paper_cat, papers in cvpr_data.items():        
        
        md.write(f"\n### {paper_cat} \n")

        # generating the dataframe
        table = []

        for paper in papers:
            paper_title = paper['title'] 
            paper_id = paper['paperId']
            if paper_title in cvpr_pdf_data:
                link = cvpr_pdf_data[paper_title]['url']
                paper_file = link.split("/")[-1]
                paper_link = os.path.join("data", paper_cat, paper_file)
                md_link = f"[Paper]({paper_link})"
                table.append([paper_id, paper_title, md_link])
        df = pd.DataFrame(table, columns=["Paper Id", "Paper Title", "Link"])
        content  = markdownTable(df.to_dict(orient='records')).setParams(row_sep = 'markdown', quote = False, padding_weight='centerright').getMarkdown()
        md.write(content + "\n\n")