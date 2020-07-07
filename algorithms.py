import random
from math import floor

global start
global end
start = ord('a') #on fixe la première lettre de l'alphabet
end = ord('z') #puis la dernière

#ajouter docstring + clareté dans l'affichage des tests

class Algorithm():

	informations = []

	def __init__(self, description):
		self.informations.append(description)

	@classmethod
	def getInfos(cls, position):
		return cls.informations[position]




class Lettres(Algorithm):
	"""docstring for Anagramme"""
	def __init__(self, description):
		super().__init__(description)

	def __str__(self): #overload
		infos = self.getInfos(0)
		return "This is the class Lettres, here are some more information : "+ infos


	@staticmethod
	def anagramme(s,s2):
		if len(s)==len(s2): #on compare en premier la taille des deux mots
			for letter in s:
				if s.count(letter) != s2.count(letter): #on compare ensuite le nombre de lettre dans les deux mots
					return False
		else:
			return False
		return True

	@staticmethod
	def palindrome(a):
	    taille = int(len(a)/2) #on s'occupe de comparer une partie du mot à l'autre
	    for x in range(taille):
	        if a[x] == a[-x-1]: #on compare une lettre à celle opposée dans le mot
	        	pass
	        else:
	            return False #si une seule comparaison n'est pas équivalente alors ce n'est pas un palindrome
	    return True #si la boucle a toujours comparé des valeurs équivalentes alors c'est un palindrome

	@staticmethod
	def romainDigits(value):
		default_keys   = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1] #valeur caractéristiques des chiffres romains
		default_values = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I'] #équivalent en chiffre romain
		romain = ""
		for i in range(len(default_keys)):
			nb = int(value/default_keys[i]) #on calcule pour chaque valeur caractéristique le nombre d'élément(s) existant(s)
			romain+= nb*default_values[i] #on ajoute à la string le nombre de fois nécessaire l'équivalent en chiifre romain
			value = value - nb*default_keys[i] #on enelève à la valeur ce qu'on vient de calculer
		return romain

		
class Math(Algorithm):

	"""docstring for Math"""
	def __init__(self, description):
		super().__init__(description)

	def __str__(self): #overload
		infos = self.getInfos(1)
		return "This is the class Math, here are some more information : "+ infos
						
	@staticmethod
	def trianglePascal(taille):
		T = []
		for i in range(0,taille):
			T.append([1]) #on ajoute le premier 1 de chaque ligne
			for j in range(1,i): #on ajoute j valeurs à la ligne considérée
				T[i].append(T[i-1][j-1]+T[i-1][j]) #on regarde la ligne d'avant et on additionne les 2 éléments côte à côte
			if i!=0:
				T[i].append(1) #on ajoute le dernier 1 de chaque ligne sauf à la première
		return T

	@staticmethod
	def factorielle(number): #gérer cas 0 et chiffres négatifs
		if number >1:
			factorielle = number
			number-=1
			while number != 1:
				factorielle*=number #on multiplie la valeur de factorielle par elle-même -1 à chaque tour
				number-=1
		elif number==0 or number == 1:
			factorielle =1
		else:
			factorielle = None
		return factorielle

	@staticmethod
	def arrondi(liste,eme):
		modified_list = []
		arrondi = [10,100,1000]
		if eme in arrondi:
			if eme == arrondi[0]:
				eme = 1
			elif eme == arrondi[1]:
				eme = 2
			else:
				eme = 3
		else:
			raise "Vous n'avez pas selectionné un arrondi correct"
		for elem in liste:
			elem = str(elem) #on convertit chaque élément de la liste en string pour pouvoir appliquer des méthodes sur les strings
			elem = elem.split('.') #on coupe le string en liste à chaque '.'
			elem[1]=elem[1][:eme] #on ne garde que eme chiffre du deuxième élément de la liste qui correspond à ce qu'il y a après la virgule
			elem = '.'.join(elem) #on remet chaque élément on float
			modified_list.append(float(elem))
		return modified_list

	@staticmethod
	def fibonacci(position): #gérer nombres négatifs
		fibonacci = [0,1]
		for i in range(2,position+1): #création liste
			fibonacci.append(fibonacci[i-1]+fibonacci[i-2]) #on additionne les 2 éléments précédents
		return fibonacci[position] #on retourne le nombre de couple au mois voulu

class Tri(Algorithm):
	"""docstring for Tri"""
	def __init__(self, description):
		super().__init__(description)

	def __str__(self): #overload
		infos = self.getInfos(2)
		return "This is the class Tri, here are some more information : "+ infos

	@staticmethod
	def tri(liste):
		for x in range(len(liste)):
			for y in range(x,len(liste)): # range(x,len(liste)) et pas range(0,len(liste)) car on ne s'occupe plus d'un élément déjà trié
				if liste[x]>liste[y]:
					liste[x], liste[y] = liste[y], liste[x] #permutation
				else:
					pass
		return liste

	@staticmethod
	def inverser_liste(liste):
		for x in range(int(len(liste)/2)): # on compare les deux moitiés de liste
			liste[x], liste[-x-1] = liste[-x-1], liste[x] #on échange les 2 oppposés
		return liste

	@staticmethod
	def rechercheDichotomique(liste,number):
		if len(liste) >0:
			middle = len(liste)//2 #floor division
			if number == liste[middle]:
				return True
			elif number < liste[middle]:
				liste = liste[:middle]
				return Tri.rechercheDichotomique(liste,number)
			elif number > liste[middle]:
				liste = liste[middle+1:]
				return Tri.rechercheDichotomique(liste,number)
		else:
			return False


class Ascii(Algorithm):
	"""docstring for Ascii"""
	def __init__(self, description):
		super().__init__(description)

	def __str__(self): #overload
		infos = self.getInfos(3)
		return "This is the class Ascii, here are some more information : "+ infos
		
	@staticmethod
	def findPositioninAlphabet(lettre):
		lettre = lettre.lower()#robustesse
		alphabet = []
		for x in range(start, end+1):
			alphabet.append(chr(x))
		for letter in alphabet:
			if letter == lettre: #on compare chaque lettre de l'alphabet à celle recherchée
				return ord(letter)-start+1 #on transforme en nombre équivalent dans l'alphabet
			else:
				pass
		return "this letter isn't in the alphabet"

	@staticmethod
	def findLetterinAlphabet(position):
		alphabet = []
		for x in range(start, end+1): #on considère toute les lettres
			alphabet.append(chr(x)) #on créer l'alphabet
		return alphabet[(position-1)%26] #modulo gère la sortie de l'alphabet en réinitialisant si besoin

	@staticmethod
	def crypt(input_text,key):
		start = ord('\n')
		end = ord('~')
		text = ""
		for x in range(0,len(input_text)):
			if x%2 == 0:
				letter = (ord(input_text[x])-start+key)%end
			else:
				letter = (ord(input_text[x])-start-key)%end
			crypted_letter = start + letter
			text+=chr(crypted_letter)
		return text


		
if __name__ == '__main__':
	#initialisation classes
	lettres = Lettres("algo lettres")
	print(lettres)
	math = Math("algo math")
	print(math)
	tri = Tri("algo tri")
	print(tri)
	ascii = Ascii("algo ascii")
	print(ascii)

	a = "kayak" #on initialise un palindrome connu
	print(lettres.palindrome(a))

	liste = []
	for x in range (0,20):
		liste.append(random.randint(0,20)/random.randint(1,10)) #génération liste de 20 floats
	liste = math.arrondi(liste,10) #on arrondi au centieme
	print(tri.tri(liste))

	print(tri.inverser_liste(liste))

	s,s2= "chien", "niche"
	print(lettres.anagramme(s,s2))

	T = math.trianglePascal(10)
	for ligne in T:
		print(ligne)

	print(ascii.findLetterinAlphabet(27))	

	print(ascii.findPositioninAlphabet('é'))

	print(lettres.romainDigits(48))

	print(math.factorielle(-1))

	print(math.fibonacci(50))

	liste.insert(3,5) #insert(position, valeur)
	print(tri.rechercheDichotomique(tri.tri(liste),5))