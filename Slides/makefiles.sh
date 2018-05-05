
for ((i=14 ; i<=31 ; i++))
do
echo "Lecture$i"
mkdir "Lecture$i"
mv ~/Downloads/lecture${i}*.pdf ./Lecture${i}/
done
