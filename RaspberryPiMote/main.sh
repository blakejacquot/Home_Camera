# Script run with sudo that captures picture locally on Raspberri Pi and 
# then copies it to host PC. Deletes local copy of picture before capturing
# next one. You may need to change IP address of server. Run IFconfig on it
# to check current one (if not set to static)

sleep_time_sec=5
image_number=1
dir_key="/home/pi/.ssh/pi_key2"
#dir_server="blakejacquot@192.168.1.7:/home/blakejacquot/Desktop/pics/"

while true; do
    # Set variables
    DATE=$(date +%Y%m%d%H%M%S)
    file_to_copy="image"$DATE".jpg"
    
    #Echo variables
    echo " "
    echo "Echo variables for review"
    echo "Today's date = " $DATE
    echo "File to copy = " $file_to_copy
    echo "Directory of public/private key = " $dir_key
    echo "Directory on host PC to where files will be copied = " $dir_server
    
    #Construct scp command to execute
    echo "Construct command to execute"
    cmd="scp -i $dir_key $file_to_copy $dir_server$file_to_copy"    
    echo $cmd
    
    #Take image
    echo "Taking an image"
    echo " "
    raspistill -e jpg -o $file_to_copy -ISO 400 --vflip
    echo "Done taking image"
    echo " "

    #Copy image to server
    echo $dir_server
    #scp -vi /home/pi/.ssh/pi_key2 image$DATE.jpg $dir_server / image$DATE.jpg
    scp -vi /home/pi/.ssh/pi_key2 image$DATE.jpg blakejacquot@192.168.1.7:/home/blakejacquot/Desktop/pics/image$DATE.jpg  
    echo "Copying file to host PC"
    $cmd

    #Remove file from host and sleep
    echo "Remove file from local machine"
    rm *.jpg

    echo "Completed image number = " $image_number
    let image_number+=1
    echo " "
    echo "***********************************************"
    echo " "
    echo "Paused for " $sleep_time_sec " seconds"
    sleep $sleep_time_sec

done
