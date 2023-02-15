print('Witaj w quizie !')

correctly_answer = 0

print('Pytanie 1: ')
fileOne = open('answer1.txt', 'r')
questionOne = fileOne.read(120)
print(questionOne)
answerOne = input('Podaj odpowiedz: ')
if answerOne == 'c' or 'C':
    correctly_answer += 1


print('Pytanie 2: ')
fileTwo = open('answer2.txt', 'r')
questionTwo = fileTwo.read(126)
print(questionTwo)
answerTwo = input('Podaj odpowiedz: ')
if answerTwo == 'd' or 'D':
    correctly_answer += 1
fileTwo.close()


print('Pytanie 3: ')
fileThree = open('answer3.txt', 'r')
questionThree = fileThree.read(93)
print(questionThree)
answerThree = input('Podaj odpowiedz: ')
if answerThree == 'a' or 'A':
    correctly_answer += 1
fileThree.close()


print('Pytanie 4: ')
fileFour = open('answer4.txt', 'r')
questionFour = fileFour.read(94)
print(questionFour)
answerFour = input('Podaj odpowiedz: ')
if answerFour == 'c' or 'C':
    correctly_answer += 1
fileFour.close()


print('Pytanie 5: ')
fileFive = open('answer5.txt', 'r')
questionFive = fileFive.read(102)
print(questionFive)
answerFive = input('Podaj odpowiedz: ')
if answerFive == 'c' or 'C':
    correctly_answer += 1
fileFive.close()

print('Koniec pytań oto twój wynik: ')
print('Poprawne odpowiedzi: ', correctly_answer)

gradue = 1

if correctly_answer == 5:
    gradue = 5
elif correctly_answer == 4:
    gradue = 4
elif correctly_answer == 3:
    gradue = 3
elif correctly_answer == 2:
    gradue = 2

print('Ocena: ', gradue)