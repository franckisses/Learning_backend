shopt -s extglob
if [[ "test.jpg" == *.@(jpeg|jpg) ]]
then 
    echo "Have one times"
else
    echo "have not find"
fi
