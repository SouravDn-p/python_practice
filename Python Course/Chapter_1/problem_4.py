import os 

directory_path = "/projects/ai projects/Ai pdf scanner"
contents = os.listdir(directory_path)

for item in contents:
    print(item)