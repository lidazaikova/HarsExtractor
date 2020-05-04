import har_extractor
##https://pypi.org/project/har-extractor/

from os import walk
import os


##путь к папке, где лежат HARы. Указать свою.
harspath = r"C:\Users\loony\Downloads\HARS"

f = []
for (dirpath, dirnames, filenames) in walk(harspath):
    f.extend(filenames)
    break

for file in f:
    foldername = file.replace(".har", "")
    fullfoldername = os.path.join(harspath,foldername)
    os.system("har-extractor -o " + "\""+ fullfoldername + "\""+ " -d " + "\"" +os.path.join(harspath, file)+"\"")
#TODO search JPEG folder and move upper in hierarchy
# fullnameslist = []
# def recurr_walk(root):
#     for (dirpath, dirnames, filenames) in walk(root, topdown=1):
#         f.extend(os.path.join(root, x) for x in dirnames) #if "JPEG" not in x
#         fullnameslist.extend(os.path.join(root, x) for x in dirnames if ("JPEG_HQ" not in x or "JPEG_LQ" not in x))
#         for name in f:
#             if (["JPEG_HQ" not in name or "JPEG_LQ" not in name]):
#                 try:
#                     f.remove(root)
#                 except ValueError:
#                     pass
#                 recurr_walk(name)
#             else: fullnameslist.append(name)
#
#
#
# recurr_walk(harspath)
# newset = set(fullnameslist)