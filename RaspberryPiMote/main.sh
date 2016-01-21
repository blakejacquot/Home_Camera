echo Hello World

#raspistill -o image1.jpg


while true; do
    echo Hello World
    DATE=$(date +%Y%m%d%H%M%S)
    echo $DATE
    raspistill -o image$DATE.jpg
    scp image$DATE.jpg blakejacquot@192.168.1.6:/home/blakejacquot/Desktop/
    sleep 1
done
