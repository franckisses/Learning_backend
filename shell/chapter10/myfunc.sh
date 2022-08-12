
function usage () {
    printf "usage: %s [ -a | -b ] file1 .....filen\n" ${0##*/} > &2
}

if [ $# -lt 1 ]
then 
    usage
fi
