import pandas as pd
dataFrame = pd.read_csv("transitionDuppliCellMapping.csv", encoding='utf-8')

def nbReponsesDePersonne(dataFrame,Utilisateur, Date1, Date2):
    NewList=[]
    NewList2=[]
    FinalList=[]

    for elem in dataFrame[dataFrame['Utilisateur']==Utilisateur]['Attribut']:

        if elem[0:8]=="IDPARENT":
            NewList.append(elem[9:])

    for el in NewList:
        el='IDMSG='+el
        for d in gestionDate(dataFrame, Date1, Date2):
            for user in dataFrame[(dataFrame['Date'] == d) & (dataFrame['Attribut']==el) & (dataFrame['Action']=='Répondre à un message')]['Utilisateur'].tolist():
                NewList2.append(user)

    for user in dict.fromkeys(NewList2):
        if user!=Utilisateur:
            FinalList.append((user,NewList2.count(user)))

    return FinalList
