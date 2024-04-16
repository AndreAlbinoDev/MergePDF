import os
from tkinter.filedialog import askdirectory

path = askdirectory(title="selected_folder")

archives_list = os.listdir(path)

locais = {
    "text": [".txt"],
    "images": [".png", ".jpg"],
    "excell": [".xlsx", ".csv"],
    "pdfs": [".pdf"],
    "video": [".mkv"]
}

for archives in archives_list:
    name, extension = os.path.splitext(f"{path}/{archives}")
    for folder in locais:
        if extension in locais[folder]:
            if not os.path.exists(f"{path}/{folder}"):
                os.mkdir(f"{path}/{folder}")
            os.rename(f"{path}/{archives}", f"{path}/{folder}/{archives}")