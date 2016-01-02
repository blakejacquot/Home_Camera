a=23
echo "The value of \"a\" is $a."
while true; do
    let "a=a+1"
    echo "$a"
    cp temp.txt /var/www/html/temp$a.txt 
    echo "Copying now"
    sleep 5
done
