#get names of .jpg files in source directory
source_files_num=$(ls -l *.txt | wc -l)
echo $source_files_num
echo "The number of source files $source_files_num"


#get names of .jpg files in target directory
target_files_num=$(ls -l /var/www/html/*.txt | wc -l) 
echo "The number of target files $target_files_num"

a=23
echo "The value of \"a\" is $a."
while true; do
    let "a=a+1"
    echo "$a"
    cp temp.txt /var/www/html/temp$a.txt 
    echo "Copying now"
    sleep 5
done
