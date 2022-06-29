"""
The purpose of this program is to read
    1. read the papers categorical info from cvpr_data.json
    2. read the json of the downloaded pdf from cvpr_data_w_pdf.json

We want to create folders matching the keys in cvpr_data.json
And for every paper within, we find the location of file in disk and 
move the appropriate category

i.e Paper under ML, moves to the ML Sub-folder
"""

import json
import os
import shutil


CVPR_DATA  = "../cvpr_data.json"
CVPR_DATA_W_PDF = "../cvf_data_w_pdf.json"
TARGET_DIR = "../data"

found = 0
not_found = 0

with open(CVPR_DATA) as cvpr_f, open(CVPR_DATA_W_PDF) as cvpr_pdf_f:
    cvpr_data = json.load(cvpr_f)
    cvpr_pdf_data = json.load(cvpr_pdf_f)

    for paper_cat, papers in cvpr_data.items():
        category = os.path.join(TARGET_DIR, paper_cat)
        if not os.path.exists(category):
            try:
                os.mkdir(category)
            except OSError as error:
                print(error)
        else:
            # since the folder exists
            # we can start moving the files appropriately
            for paper in papers:
                paper_title = paper['title']                
                # we will attempt to find this paper in the cvpr_pdf_data
                if paper_title in cvpr_pdf_data:
                    src_file_path = cvpr_pdf_data[paper_title]['url']
                    src_file_name = src_file_path.strip().split("/")[-1]
                    # copy the file categorically
                    shutil.copyfile(src_file_path, os.path.join(category, src_file_name))
                    found += 1
                else:
                    print(paper_title)
                    not_found += 1
print(found)
print(not_found)


    