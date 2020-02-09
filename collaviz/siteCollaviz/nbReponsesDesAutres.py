import pandas as pd
from siteCollaviz import gestionDate

def nbReponsesParPersonne(fichier,Utilisateur, Date1, Date2):
    dataFrame = pd.read_csv(fichier, encoding='utf-8')

    NewList=[]
    NewList2=[]
    FinalList=[]

    for elem in dataFrame[dataFrame['Utilisateur']==Utilisateur]['Attribut']:
        if elem[0:5]=="IDMSG":
            NewList.append(elem[6:])

    for el in NewList:
        el="IDPARENT="+el
        for d in gestionDate.gestionDate(dataFrame, Date1, Date2):
            for user in dataFrame[(dataFrame['Date'] == d) & (dataFrame['Attribut']==el) & (dataFrame['Action']=='Répondre à un message')]['Utilisateur'].tolist():
                NewList2.append(user)
    for user in dict.fromkeys(NewList2):
        if user!=Utilisateur:
            FinalList.append([user,NewList2.count(user)])
    return FinalList

def nbReponsesParPersonneGroupe(dataframe, utilisateur, groupe, Date1, Date2):
    tmp = nbReponsesParPersonne(dataframe, utilisateur, Date1, Date2)
    final = [["Users", 0]]
    for i in tmp:
        if i[0] in groupe:
            final.append(i)
        else:
            final[0][1] += i[1]
    return final
