#Write a program that prints the abbreviation of the university name (i.e. KUE)

###
# A program that prints a university abbreviation
#   


university = "Krakow University of Economics"
words = university.split()  # Dzieli tekst na listę słów
abbreviation = words[0][0] + words[1][0] + words[3][0]  # Bierzemy pierwszą literę z "University" i "Economics"
print(abbreviation)