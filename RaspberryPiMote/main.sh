echo Hello World

#raspistill -o image1.jpg


while true; do
    echo Hello World
    DATE=$(date +%Y%m%d%H%M%S)
    echo $DATE
    raspistill -o image$DATE.jpg
    sleep 1
done
