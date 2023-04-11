import os
from .globals import *


def getFileType(filename: str):
    if filename.endswith(RUN_EXT):
        return RUN_EXT
    elif filename.endswith(GRP_EXT):
        return GRP_EXT
    elif filename.endswith(SEC_EXT):
        return SEC_EXT
    else:
        return OTH_TYP

def getFileData(path: str):
    files_list = os.listdir(path)

    files = {
        RUN_EXT: [],
        GRP_EXT: [],
        SEC_EXT: [],
        OTH_TYP: [],
    }

    for item in files_list:
        fileType = getFileType(path + "/" + item)
        files[fileType].append(item)

    return files



