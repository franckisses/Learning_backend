function max ()
{
    if [ $1 -gt $2 ]
    then 
        echo $1
    else
        echo $2
    fi
}

max 128 20 

echo $BIGR
