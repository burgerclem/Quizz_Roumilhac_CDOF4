import os
import random
import time


def reponses_generateur(bonne_reponse):
    # function to generate responses for the question
    reponses = [bonne_reponse]
    while len(reponses) < 3 :
        # we just make a little difference ([-10, 10]) to have wrong responses close to the right one
        signe = [-1,1][random.randrange(2)]
        difference = random.randint(0,10)
       
        rep = bonne_reponse + signe * difference

        if rep not in reponses : reponses.append(rep)
    
    return reponses



clear = lambda: os.system('cls')
nombre_de_questions = 20
score=0


for i in range(nombre_de_questions):
    # Generate a question
    a = random.randint(1,15)
    b = random.randint(1,10)
    bonne_reponse = a*b

    print(f'Combien font {a} x {b} ?')

    # Generate answers for the MCQ
    rep = reponses_generateur(bonne_reponse)

    random.shuffle(rep)
    rep2={1:int(rep[0]),2:int(rep[1]),3:int(rep[2])}
    print(f"1) {rep[0]}     2) {rep[1]}     3) {rep[2]}\n")

    # Get user answer (user input) and check the result
    user_answer = input('Votre réponse : ')

    while (user_answer not in ['1','2','3','q']):
        print("Entrée non conforme, veuillez ecrire 1, 2, 3 ou 'q' pour quitter")
        user_answer = input('Votre réponse : ')
    if(user_answer == 'q'):
        break

    user_answer = int(user_answer)

    if(rep2[user_answer] == bonne_reponse):
        print("C'est une bonne réponse! +1pt")
        score+=1
    else:
        print("Dommage, c'est une mauvaise réponse :(")
    time.sleep(1)
    clear()

print("Le quizz de Mathématiques est terminé")
print("Vous avez obtenu un socre de "+str(score)+"/20")