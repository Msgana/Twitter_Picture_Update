import picamera
from tweet_function import postImage
from subprocess import call
from datetime import datetime
from time import sleep


# file path for pictures and video recording
picture_filePath = "/home/pi/Desktop/NASA/timestamped_pictures/"

#define count and number of pictures that will be taken
picTotal = 5
picCount = 0

#using while loop
while picCount < picTotal:
    # Grab the current time
    currentTime = datetime.now()
    # Create file name for our picture
    picTime = currentTime.strftime("%Y/%m/%d-%H:%M:%S")
    picName = picTime + '.jpg'
    completeFilePath = picture_filePath + picName

    # Take picture using new filepath
    with picamera.PiCamera() as camera:
        camera.resolution = (1280,720)
        camera.capture(completeFilePath)
        print("Picture taken!")
        
        postImage(completeFilePath)

        print("Twitter feed has been updated with " + picName + "at" + currentTime)

        # Advance our picture counter
        picCount += 1
        sleep(5)  # wait 15 minutes for next picture shot
        
        
        
 def timeStamp(filepath):
     # Create our stamp variable
    timestampMessage = currentTime.strftime("%Y.%m.%d - %H:%M:%S")
    # Create time stamp command to have executed
    timestampCommand = "/usr/bin/convert " + completeFilePath + " -pointsize 30 \
    -fill green -annotate +750+700 '" + timestampMessage + "' " + completeFilePath
    # Actually execute the command!
    call([timestampCommand], shell=True)

"""
    # Create our stamp variable
    timestampMessage = currentTime.strftime("%Y.%m.%d - %H:%M:%S")
    # Create time stamp command to have executed
    timestampCommand = "/usr/bin/convert " + completeFilePath + " -pointsize 30 \
    -fill green -annotate +750+700 '" + timestampMessage + "' " + completeFilePath
    # Actually execute the command!
    call([timestampCommand], shell=True)
    print("Picture timestamped!")
"""
