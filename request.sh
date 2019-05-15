input="/home/aeredren/Documents/INSA/Telecom/projetWeb/projetWebLaveries/table.csv"

while IFS= read -r var
do

	N="$(cut -d',' -f3 <<<$var)"
	curl http://127.0.0.1:8000/machine/info/$N

done < "$input"
