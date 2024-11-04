import math
#jobs 1
"""
def My_print_hello():
    print("hello world")

My_print_hello();
"""
#jobs 2
"""
name="alex"
def my_print_name(name):
    print(name)

my_print_name(name)
"""

#jobs 3
"""
nombre1 = int(input("nombre 1 :   "))
nombre2 = int(input("nombre 2 :   "))
def add(nombre1, nombre2):
    print("le resultat est : ", nombre1 + nombre2)

add(nombre1,nombre2)
"""

#jobs 4
"""
def GetHello():
    return print("hello la plateforme")

GetHello()
"""

#jobs 5
"""
num1 = int(input("numero 1 : "))
operator = input("signe : ")
num2 = int(input("numero 2 : "))

def calcule(num1, operator, num2):
    if operator == "*":
       resultat= print("le resultat est:  ",num1 * num2)
    elif operator == "/":
       resultat= print("le resultat est:  ",num1 / num2)
    elif operator == "-":
        resultat= print("le resultat est:  ",num1 - num2)
    elif operator == "+":
      resultat= print("le resultat est:  ",num1 + num2)
    return resultat

calcule(num1, operator, num2)
"""

#jobs 6

"""
def result(nombre):
    if nombre < 0:
        resultat = print("Negatif")
    elif nombre > 0:
       resultat  =  print("Positif")
    else:
        resultat = print("veuillez rentrer un nombre")
    return resultat

for i in range(5):
    nombre = int(input("rentrez un nombre :  "))
    result(nombre)

"""

#jobs 7
"""
progra = input("veuillez entrer votre langage de programmation :  ")

def langage(prog):
    if prog == "javascript":
        print("tu es un développeur web")
    elif prog == "python":
        print("tu es un développeur ia")
    elif prog == "java":
        print("tu es un développeur logiciel")
    elif prog == "reactjs":
        print("tu es un développeur mobile")
    else:
        print("unjour, je serai le meilleur developpeur")

langage(progra)
"""

#jobs 8
"""
type= input(" c'est un fruit ou un legume ? ")
saison= input("quel est la saison ?  ")

def aliments(type, saison):
    if type == "fruits" and saison == "hiver":
        aliment = print("orange, mandarine et kiwi")
    elif type == "fruits" and saison == "ete":
        aliment = print("poire, fraise et cassis")
    elif type == "legume" and saison == "hiver":
       aliment = print("carotte, topinambour et endive")
    elif type == "legume" and saison == "ete":
       aliment = print("artichaut, aubergine et navet")

    return aliment

aliments(type, saison)

"""

#jobs 9
"""
note1= int(input("note 1 : "))
note2= int(input("note 2 : "))
note3= int(input("note 3 : "))

def moyenne(n1, n2,n3):
    resultat = (n1+n2+n3)/3
    print(resultat)
    if resultat <= 20 and resultat >= 15:
        print("trés bon élèves")
    elif resultat<=14 and resultat>=11:
        print("bon élève")
    elif resultat<=10 and resultat>=8:
       print("élève moyen")
    elif resultat<=7 and resultat>=0:
       print("élève devant faire des efforts")
    else:
        print("vous avez mal rentrer vos notes")
    

moyenne(note1, note2, note3)

"""

#jobs  10
"""
chiffre = int(input("entrez un nombre"))

def pair_impair(chiffre):
    if chiffre > 0 or type(chiffre) == int:
        if chiffre %2 ==0 :
            print("ce chiffre est pair")
        else:
            print("ce chiffre est impair")
    else:
        print("ce n'est pas un bon chiffre")

pair_impair(chiffre)
"""
#jobs 11
"""
def time_to_text(nombre):
    heure   =  int(nombre / 60)
    minutes =  nombre % 60
    print(heure)
    print(minutes)
    if nombre > 60 :
        return print(heure, "heure et", minutes, " minutes")
    if nombre > 120 :
        return print(heure, "heures et", minutes, " minutes")
    else:
        return print(heure, "heures et", minutes, " minutes")


time_to_text(185)
time_to_text(55)
time_to_text(65)
"""

#aller plus loin


mot = input("Entrez un mot")

def inverser(mot):
    invers = slice(mot, len(mot))
    print("mot inverser ", invers)
    
inverser(mot)