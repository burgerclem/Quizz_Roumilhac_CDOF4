import pandas as pd
import os
import random
import time
clear = lambda: os.system('cls')

df= pd.read_csv('data.csv')
score=0

for index,row in df.iterrows():
    print(row["question"]+"\n")

    rep=row["mauvaise reponse"].split(",")
    rep.append(str(row["bonne reponse"]))
    random.shuffle(rep)
    rep2={1:int(rep[0]),2:int(rep[1]),3:int(rep[2])}
    print("1)"+rep[0]+"     2)"+rep[1]+"     3)"+rep[2]+"\n")

    x=int(input())
    if(x==66):
        break
    while(x!=1 and x!=2 and x!=3):
        print("Entrée non conforme, veuillez ecrire 1,2 ou 3")
        x=int(input())
    
    if(int(row["bonne reponse"])==rep2[x]):
        print("C'est une bonne réponse! +1pts")
        score+=1
    else:
        print("Dommage, c'est une mauvaise réponse :(")
    time.sleep(3)
    clear()
    
print("Le quizz de Mathématiques est terminé")
print("Vous avez obtenu un socre de "+str(score)+"/20")