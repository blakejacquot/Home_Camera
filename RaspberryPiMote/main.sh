# Script run with sudo that captures picture locally on Raspberri Pi and 
# then copies it to host PC. Deletes local copy of picture before capturing
# next one. You may need to change IP address of server. Run IFconfig on it
# to check current one (if not set to static)

while true; do
    # Set variables
    sleep_time_sec=1
    DATE=$(date +%Y%m%d%H%M%S)
    dir_key="/home/pi/.ssh/pi_key2"
    #dir_server="blakejacquot@192.168.1.7:/home/blakejacquot/Desktop/pics/"
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
    raspistill -v -e jpg -o $file_to_copy -ISO 400 --vflip
    echo "Done taking image"
    echo " "

    #Copy image to server
    scp -vi /home/pi/.ssh/pi_key2 image$DATE.jpg blakejacquot@192.168.1.7:/home/blakejacquot/Desktop/pics/image$DATE.jpg  
    echo "Copying file to host PC"
    $cmd

    #Remove file from host and sleep
    echo "Remove file from local machine"
    rm *.jpg
    sleep $sleep_time_sec

    echo " "
    echo "***********************************************"
    echo " "
done
