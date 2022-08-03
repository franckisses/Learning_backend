for FN in *.xlsx
do 
    mv "$(pwd)/${FN}" "${FN%.xlsx}"
done
