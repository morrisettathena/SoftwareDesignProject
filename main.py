import reader.fileReader as fileReader
import reader.folderReader as folderReader
import reader.globals as readerGlobals
import calculation.section as section

def main():
    path = "./data"
    z = folderReader.getFileData(path)

    secData = {}
    for item in z[readerGlobals.SEC_EXT]:
        secData[item] = section.calculateSectionData(fileReader.readSecData(path + "/" + item))

    for item in secData:
        for i in secData[item]:
            print(i + ": " + str(secData[item][i]))

    grpData = {}
    for item in z[readerGlobals.GRP_EXT]:
        grpSecs = fileReader.readGrpData(path + "/" + item)
        grpData[item] = section.calculateGroupData(secData, grpSecs)

    for item in grpData:
        for i in grpData[item]:
            print(i + ": " + str(grpData[item][i]))
        
main()