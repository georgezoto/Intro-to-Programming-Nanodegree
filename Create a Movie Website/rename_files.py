import os

def rename_files(path):
    files = os.listdir(path)
    os.chdir(path)
    for file in files:
        os.rename(file, file.translate(None, '0123456789'))
        print file

rename_files('../IPND_materials/4-Create-a-Movie-Website/1_using_functions/b_secret_message/prank')
