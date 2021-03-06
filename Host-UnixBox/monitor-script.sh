# Script that generates html page for viewing from all images found
# copied from Raspberri Pi

source_dir=../
destination_dir=/var/www/html/

while true; do
    #get names of .jpg files in source directory
    echo "***Looking for .jpg files in source directory"
    source_files_num=$(ls -l $source_dir*.jpg | wc -l)
    source_files=$(ls -l $source_dir*.jpg)
    echo "The number of source files $source_files_num"
    echo "The source files are"
    echo $source_files
    echo " "    

    #get names of .jpg files in destination directory
    echo "***Looking for .jpg files in destination directory"
    destination_files_num=$(ls -l $destination_dir*.jpg | wc -l) 
    destination_files=$(ls -l $destination_dir*.jpg)
    echo "The number of destination files $destination_files_num"
    echo "The destination files are"
    echo $destination_files
    echo " "

    echo "***Copying .jpg files from source directory to destination directory"
    echo "Do not overwrite existing files"
    cp -n ../*.jpg /var/www/html/

    echo "Sleeping for 5 seconds"
    sleep 5
    echo "********************"
    echo "********************"
    echo "********************"
done
