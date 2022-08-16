
function showprg ()
{
    printf '.'
}

ls -l /usr/bin > /tmp/myfile.data

mapfile -t -s 1 -n 1500 -C showprg -c 100 BIGDATA < /tmp/myfile.data

echo


siz=${#BIGDATA[@]}
echo "size: ${siz}"
