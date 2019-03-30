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
    "ChangeDisplayImage(" : "DisplayImage(",
    "GetListOfImages(" : "GetImageList(",
    "SaveImageAssetToRobot(" : "SaveImage(",
    "DeleteImageAssetFromRobot(" : "DeleteImage(",
    "GetListOfAudioFiles(" : "GetAudioList(",
    "PlayAudioClip(" : "PlayAudio(",
    "SaveAudioAssetToRobot(" : "SaveAudio(",
    "DeleteAudioAssetFromRobot(" : "DeleteAudio(",
    "SlamGetMap(" : "GetMap(",
    "SlamGetPath(" : "GetSlamPath(",
    "SlamGetSensorSerialNumber(" : "GetSlamSerialNumber(",
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

# print(changes)
# print([value for key, value in changes.items() if 'ChangeDisplayImage(' in key][0])

for skillFile in jsFiles:
    with open(skillFile,'r') as dataFile:
        data = dataFile.read()
        # print(data)
        for key, value in changes.items():
            data = data.replace(key, value)
        # print(data)
        newFile = open('updated_'+skillFile, "x")
        newFile.write(data)
        newFile.close()
        dataFile.close()


print("Hello Misty!")