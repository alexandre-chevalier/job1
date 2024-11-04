print(10+3)

print("abcdefghijklmnopqrstuvwxyz")

print("zyxwvutsrqponmlkjihgfedcba")

ma_string="Je suis une String"

print(ma_string)

num1 = 40
num2 = 2

print(num1 + num2)

num1 = 3
num2 = 14

print(num1 * num2)

#jobs 9
nom = "call of duty"
prix = 79.99
quantite = 1

print(nom, end=" ")
print(prix, end="  ")
print(quantite)

ajout= int(input("ajout au stock"))
print(quantite)
quantite = quantite + ajout
print(quantite)

taux = prix * 10/100
print(taux)

prix = prix + taux
print(prix)

print(nom, end=" ")
print(prix, end="  ")
print(quantite)

#jobs 11

montant_init=2500
taux_rend_annu= 5/100

montant_init= montant_init + 5000
print(taux_rend_annu)
taux_rend_annu = taux_rend_annu + 0.02
print(taux_rend_annu)
print(montant_init)

gain_annuel = montant_init * taux_rend_annu
print(gain_annuel)

montant_init=montant_init + gain_annuel
print(montant_init)

montant_init = montant_init - montant_init * 0.1
print(montant_init)
print(taux_rend_annu)

taux_rend_annu = taux_rend_annu - 0.01
print(taux_rend_annu)

gain_annuel = montant_init * taux_rend_annu
print(gain_annuel)


montant_init = montant_init + gain_annuel
print(montant_init)



#pour aller plus loin

sentence = input("Ecriver une phrase")
print(sentence.count("e"))
