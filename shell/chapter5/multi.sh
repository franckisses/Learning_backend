echo "$@"
for FN in "$@"
do
    echo "$FN"
    chmod 777 "$FN"
done
