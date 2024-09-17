#TODO: Analyser la chaîne de caractères saisie et compter le nombre de médailles.
#      Attention si la chaîne est invalide, un message d'erreur est attendu.

country = input("Pays concerné ? ");
code_medals = input("Chaine représentant les médailles ? ");

gold = 0;
silver = 0;
bronze = 0;
is_valid = True;

for letter in code_medals:
	if letter == "G":
		gold += 1;
	elif letter == "S":
		silver += 1;
	elif letter == "B":
		bronze += 1;
	else:
		is_valid = False;

if is_valid:
	print(f"{country}:\n- {gold} Or\n- {silver} Argent\n- {bronze} Bronze")
else:
	print("Ceci est une chaine invalide.");