import os

files = [f for f in os.listdir('.') if os.path.isfile(f)]
jsFiles = []
for f in files:
    if f.endswith(".js"):
        jsFiles.append(f)

print(jsFiles)

changes = {
    "LocomotionTrack(" : "DriveTrack(",
    "MoveHead(" : "MoveHeadPosition(",
    "MoveArm(" : "MoveArmPosition(",
    "MoveArms(" : "MoveArmsPosition(",
    "ClearlearnedFaceByid(" : "ForgetFace(",
    "ClearLearnedFaceByid(" : "ForgetFace(",
    "ClearlearnedFaceById(" : "ForgetFace(",
    "ClearLearnedFaceById(" : "ForgetFace(",
    "ClearLearnedFaces(": "ForgetAllFaces(",
    "GetLearnedFaces(" : "GetKnownFaces(",
    "_GetLearnedFaces(" : "_GetKnownFaces(",
    "ChangeDisplayImage(" : "DisplayImage(",
    "GetListOfImages(" : "GetImageList(",
    "_GetListOfImages(" : "_GetImageList(",
    "SaveImageAssetToRobot(" : "SaveImage(",
    "_SaveImageAssetToRobot(" : "_SaveImage(",
    "DeleteImageAssetFromRobot(" : "DeleteImage(",
    "GetListOfAudioFiles(" : "GetAudioList(",
    "_GetListOfAudioFiles(" : "_GetAudioList(",
    "PlayAudioClip(" : "PlayAudio(",
    "SaveAudioAssetToRobot(" : "SaveAudio(",
    "_SaveAudioAssetToRobot(" : "_SaveAudio(",
    "DeleteAudioAssetFromRobot(" : "DeleteAudio(",
    "_DeleteAudioAssetFromRobot(" : "_DeleteAudio(",
    "SlamGetMap(" : "GetMap(",
    "_SlamGetMap(" : "_GetMap(", 
    "SlamGetPath(" : "GetSlamPath(",
    "_SlamGetPath(" : "_GetSlamPath(",
    "SlamGetSensorSerialNumber(" : "GetSlamSerialNumber(",
    "_SlamGetSensorSerialNumber(" : "_GetSlamSerialNumber(",
    "SlamGetStatus(" : "GetSlamStatus(",
    "SlamReset(" : "ResetSlam(",
    "SlamSensorReboot(" : "RebootSlam(",
    "SlamStartMapping(" : "StartMapping(",
    "SlamStartmapping(" : "StartMapping(",
    "SlamStartTracking(" : "StartTracking(",
    "SlamStopMapping(" : "StopMapping(",
    "SlamStopTracking(" : "StopTracking(",
    "SlamStartRecording(" : "StartSlamRecording(",
    "SlamStopRecording(" : "StopSlamRecording(",
    "SlamGetVisibleImage(" : "TakeFisheyePicture(",
    "SlamGetDepthImage(" : "TakeDepthPicture(",
    "SlamStartStreaming(" : "StartSlamStreaming(",
    "SlamStopStreaming(" : "StopSlamStreaming(",
    "Getdeviceinformation(" : "GetDeviceInformation(",
    "GetDeviceinformation(" : "GetDeviceInformation(",
    "GetdeviceInformation(" : "GetDeviceInformation(",
    "GetWebsocketHelp(" : "GetWebsocketNames(",
    "MessageStreamWrite(" : "WriteSerial(",
    "HdtDrive" : "DriveHeading(",
    "\"StringMessage\"" : "\"SerialMessage\"",
    "\"FaceDetection\"" : "\"FaceRecognition\"",
    "\"ComputerVision\"" : "\"FaceRecognition\"",
    "_StringMessage(" : "_SerialMessage("
}

# SetHeadPostion => MoveHeadPosition updated commands are not indended right - you could try to fix that !
def setHeadSupporter(axis,line,file):
    dataChunks = line.split(',')
    value = dataChunks[1]
    if axis is "roll":
        line = line.replace(line,"misty.MoveHeadPosition(null,"+str(value)+",null);") 
    elif axis is "pitch":
        line = line.replace(line,"misty.MoveHeadPosition("+str(value)+",null,null);") 
    else:
        line = line.replace(line,"misty.MoveHeadPosition(null,null,"+str(value)+");") 
    file.write(line+"\n")

for skillFile in jsFiles:
    with open(skillFile,'r') as dataFile:
        data = dataFile.read()
        for key, value in changes.items():
            data = data.replace(key, value)
        tempFile = open('temp_'+skillFile, "x")
        tempFile.write(data)
        tempFile.close()
        dataFile.close()
    with open('temp_'+skillFile,'r') as dataFile:
        newFile = open('updated_'+skillFile, "x")
        for line in dataFile.readlines():
            if "misty.SetHeadPosition(\"roll\"" in line:
                setHeadSupporter("roll",line,newFile)
            elif "misty.SetHeadPosition(\"pitch\"" in line:
                setHeadSupporter("pitch",line,newFile)
            elif "misty.SetHeadPosition(\"yaw\"" in line:
                setHeadSupporter("yaw",line,newFile)
            else:
                newFile.write(line)
        os.remove('temp_'+skillFile)
        newFile.close()
        
print("Hello Misty!")