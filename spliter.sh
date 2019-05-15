
H="testH"
E="testE"
N="testN"
M="testM"
F="testF"
B="testB"

input="/home/aeredren/Documents/INSA/Telecom/projetWeb/projetWebLaveries/table.csv"

while IFS= read -r var
do
	H="$(cut -d',' -f1 <<<$var)"
	E="$(cut -d',' -f2 <<<$var)"
	N="$(cut -d',' -f3 <<<$var)"
	M="$(cut -d',' -f4 <<<$var)"
	F="$(cut -d',' -f5 <<<$var)"
	B="$(cut -d',' -f6 <<<$var)"
	ID="$(cut -d',' -f7 <<<$var)"
	TYPE="$(cut -d',' -f8 <<<$var)"

	echo "	{
		\"heures\":    \"$H\",
		\"etat\":      \"$E\",
		\"number\":    \"$N\",
		\"modele\":    \"$M\",
		\"fabricant\": \"$F\",
		\"batiment\":  \"$B\",
		\"id\": \"$ID\",
		\"type\":  \"$TYPE\"
	},"
done < "$input"
