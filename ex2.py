# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.
import math

water_quantity = input("Quelle quantité d'eau faut-il assainir ? ");

water_math = float(water_quantity);

nombre_de_filtres = math.ceil(water_math / 5);
nombre_de_lampes = math.ceil(water_math * (3/5));
masse_de_chlore = water_math / 10;

print(f"Voici les éléments requis pour assainir {water_quantity}L d'eau:");
print(f"\t- Filtre(s) : {nombre_de_filtres}");
print(f"\t- Lampe(s) UV : {nombre_de_lampes}");
print(f"\t- Chlore : {masse_de_chlore}kg");