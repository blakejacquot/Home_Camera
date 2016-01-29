#Next make python wrapper for raspistill...a driver we can use for scripting

while true; do
    echo 
    
    #Set variables
    sleep_time_sec=1
    DATE=$(date +%Y%m%d%H%M%S)
    dir_key="/home/pi/.ssh/pi_key2"
    dir_server="blakejacquot@192.168.1.6:/home/blakejacquot/Desktop/pics/"
    file_to_copy="image"$DATE".jpg"
    
    #Echo variables
    echo $DATE
    echo $file_to_copy
    echo $dir_key
    echo $dir_server
    echo $dir_key $dir_server
    
    #Construct scp command to execute
    cmd="scp -i $dir_key $file_to_copy $dir_server$file_to_copy"    
    
    #Take image
    raspistill -o $file_to_copy
    
    #Copy image to server
    #scp -i /home/pi/.ssh/pi_key2 image$DATE.jpg blakejacquot@192.168.1.6:/home/blakejacquot/Desktop/pics/image$DATE.jpg  
    $cmd

    #Remove file from host and sleep
    rm *.jpg
    sleep $sleep_time_sec
done
