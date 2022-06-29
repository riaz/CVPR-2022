import csv
import json

categories = {}
CATEGORY_KEY = 'Session Title / Poster Group'

with open('/Users/rmunshi/Misc/CVPR2022/cvpr_sheet_curated.csv', 'r', newline='\n') as csvfile:
    reader = csv.DictReader(csvfile)
    count = 0
    category_name = ""
    for row in reader:
        count+=1
        if row[CATEGORY_KEY]:
            category_name = row[CATEGORY_KEY]
            categories[category_name] = []
        
        categories[category_name].append({
            "paperId" : row['Paper ID'],
            "posterId": row['Poster ID'],
            "title": row['Title (Corrected)'],
            "authors": row['Authors (Corrected)'].strip().split(";")
        })  
print(len(categories.keys()), count)
json_save_location = "/Users/rmunshi/Misc/CVPR2022/cvpr_data.json"
with open(json_save_location,"w") as fw:
    json.dump(categories, fw, ensure_ascii=False, indent=4)
                  