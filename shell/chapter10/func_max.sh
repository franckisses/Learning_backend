function max ()
{
    local HIDN
    if [ $1 -gt $2 ]
    then 
        BIGR=$1
    else
        BIGR=$2
    fi
    HIDN=5
}

max 128 20 

echo $BIGR
