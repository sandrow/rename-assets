# import os
# from pathlib import Path
# import shutil
# os.chdir('/Users/santowns/Documents/rename-assets/assets')

# new_asset_folder = "new-renamed-assets"

# # Path(new_asset_folder).mkdir(exist_ok=True)
# # if not os.path.exists("new-renamed-assets"):
# #     os.mkdir("new-renamed-assets")

# for file in os.listdir():
#     if file == '.DS_Store' or file == new_asset_folder:
#         continue
#     shutil.move(file, new_asset_folder)

#     f = Path(file)
#     name, ext = f.stem, f.suffix
#     # name, ext = os.path.splitext(file)
#     splitted = name.split("-")
#     splitted = [s.strip() for s in splitted]
#     new_name = f"{splitted[3].zfill(2)}-{splitted[1]}-{splitted[2]}-{splitted[0]}{ext}"
#     f.rename(new_name)



import os

directory = '/Users/santowns/Documents/rename-assets/assets' # specify the directory path here
model_year = 'MY24' # EXAMPLE... MY24, MY23, MY22
brand = 'TESLA' # EXAMPLE... 
pillar = 'HOMEPAGE' # EXAMPLE...


for count, filename in enumerate(os.listdir(directory)):
    new_filename = f"{model_year}-{brand}-{pillar}-{count}{os.path.splitext(filename)[1]}"
    source = os.path.join(directory, filename)
    destination = os.path.join(directory, new_filename)
    os.rename(source, destination)
    
# import json
# import os

# directory = '/Users/santowns/Documents/rename-assets' # specify the directory path here
# json_file = '/Users/santowns/Documents/rename-assets' # specify the path to the JSON file here

# with open(json_file, 'r') as f:
#     data = json.load(f)
#     image_name = data['imageName']

# for filename in os.listdir(directory):
#     if filename.startswith(image_name):
#         new_filename = f"new_name{os.path.splitext(filename)[1]}"
#         source = os.path.join(directory, filename)
#         destination = os.path.join(directory, new_filename)
#         os.rename(source, destination)