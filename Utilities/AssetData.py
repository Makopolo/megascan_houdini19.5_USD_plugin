import hou
import re
import os

def GetAssetType(assetjson):
    return assetjson["type"]

def GetAssetName(asset_json, name_rule= "name"):
    rule_tags = name_rule.split("_")    
    asset_name = "_".join(asset_json[i] for i in rule_tags if i in asset_json.keys())    
    return SanitizeAssetName(asset_name)

def SanitizeAssetName(assetName):
    return re.sub(r"[^a-zA-Z0-9]+" , "_", assetName)



def GetMajorVersion():
    return hou.applicationVersionString().split(".")[0]

def EnableUSD():
    
    USDSupportedVersions = ["18", "19", "20", "21", "22", "23"]  ########modified##### what versions the usd checkbox is active
    if hou.applicationVersionString().split(".")[0] in USDSupportedVersions:
        return True
    else : return False

def getImportParams(assetData, importOptions):
    #main information filter where the asset will be processed through. you will then be able to acess the assests info and plugin data eg. EnableUSD or Atlas checkbox 
    importParams = {}
    importParams["assetName"] = GetAssetName(assetData, "name" )
    typeNames = {"3d" : "3D_Assets", "surface" : "Surfaces" , "3dplant" : "3D_Plants", "atlas" : "Atlas"}
    
    
    if importOptions["UI"]["ImportOptions"]["EnableUSD"]:
        importParams["importType"] = "USD"
        if assetData["type"] == "surface": ########modified
            importParams["materialPath"] = "/stage"
            createBaseNetwork(importParams["materialPath"])
        ####################modified################## 

        elif assetData["type"] == "atlas" and not importOptions["UI"]["ImportOptions"]["UseAtlasSplitter"] :
                importParams["materialPath"] = "/stage"
                createBaseNetwork(importParams["materialPath"])

        elif assetData["type"] == "atlas" and importOptions["UI"]["ImportOptions"]["UseAtlasSplitter"] :
            importParams["importType"] = "Normal"
            if importOptions["UI"]["ImportOptions"]["UseAtlasSplitter"]:                
                basePath = "/obj"
                usdBasePath = "/stage"
                importParams["usdAssetPath"] =usdBasePath + "/" +importParams["assetName"]
                importParams["assetName"] = getUniqueAssetName(GetAssetName(assetData, "name"), basePath)
                importParams["assetPath"] = basePath + "/" +importParams["assetName"]
                importParams["materialPath"] = importParams["assetPath"] + "/" + "materialNet"
                createBaseNetwork(importParams["assetPath"])
                
            else :
                importParams["materialPath"] = "/mat"
####################################################################
        else:
            usdBasePath = "/stage"
            objBasePath = "/obj"

            importParams["assetName"] = getUniqueAssetName(GetAssetName(assetData, "name"), usdBasePath)
            importParams["objAssetName"] = getUniqueAssetName(GetAssetName(assetData, "name"), objBasePath)

            importParams["assetPath"] = objBasePath + "/" +importParams["objAssetName"]
            importParams["usdAssetPath"] =usdBasePath + "/" +importParams["assetName"]
            importParams["materialPath"] = usdBasePath + "/" +importParams["assetName"]
            fileextension = os.path.splitext(assetData["meshList"][0]["path"])[1]
            if fileextension != ".abc":
                createBaseNetwork(importParams["assetPath"])
            createBaseNetwork(importParams["usdAssetPath"])
    else:
        importParams["importType"] = "Normal"
        if assetData["type"] == "surface" or assetData["type"] == "brush":
            importParams["materialPath"] = "/mat"
        elif assetData["type"] == "3d" or assetData["type"] == "3dplant":
            basePath = "/obj"
            importParams["assetName"] = getUniqueAssetName(GetAssetName(assetData, "name"), basePath)
            importParams["assetPath"] = basePath + "/" +importParams["assetName"]   
            importParams["materialPath"] = importParams["assetPath"] + "/" + "materialNet"
            createBaseNetwork(importParams["assetPath"])

        elif assetData["type"] == "atlas":
            if importOptions["UI"]["ImportOptions"]["UseAtlasSplitter"]:                
                basePath = "/obj"
                importParams["assetName"] = getUniqueAssetName(GetAssetName(assetData, "name"), basePath)
                importParams["assetPath"] = basePath + "/" +importParams["assetName"]
                importParams["materialPath"] = importParams["assetPath"] + "/" + "materialNet"
                createBaseNetwork(importParams["assetPath"])
            else :
                importParams["materialPath"] = "/mat"


            

    return importParams

def getUniqueAssetName(assetName, basePath):
    for i in range(0,100):
        assetNameNew = assetName + "_" + str(i)        
        assetPath = basePath + "/" + assetNameNew        
        existingNode = hou.node(assetPath)
        if existingNode == None:
            return assetNameNew
    
def createBaseNetwork(assetPath):
    pathTokens = assetPath.split("/")
    pathList = []
    parsedPath = "/" + pathTokens[1]
    pathList.append(parsedPath)
    for pathToken in pathTokens[2:]:
        parsedPath = parsedPath + "/" + pathToken
        pathList.append(parsedPath)

    for i in range(1,len(pathList)):
        basePath = pathList[i-1]
        networkNode = hou.node(pathList[i])
        if networkNode == None:
            interNode = hou.node(basePath).createNode("subnet", pathList[i].split("/")[-1])
            hou.node(basePath).moveToGoodPosition()
            interNode.moveToGoodPosition()
        else :
            networkNode.moveToGoodPosition()


def getSupportedUSDMaterials():
    return {"Karma" : "Principled_USD", "Renderman" : "PixarSurface_USD"}

def getExrDisplacement(inputPath, res = "2K"):
    
    filepath, fileextension = os.path.splitext(inputPath)
    if fileextension == "exr":
        return inputPath
    exrFile = filepath + ".exr"    
    if os.path.isfile(exrFile):        
        return exrFile

    return inputPath
