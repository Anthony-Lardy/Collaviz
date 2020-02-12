from datetime import datetime
from datetime import timedelta
import pandas as pd
from datetime import time



def tempsLectureReponseMoyenToutLeMonde(dataframe):
    utilisateurs = pd.unique(dataframe['Utilisateur'])
    secondes = 0
    denom = len(utilisateurs)
    for utlisateur in utilisateurs:
        val = tempsLectureReponseMoyen(dataframe, utlisateur)
        if(val == 0):
            denom -= 1
        secondes += val
    if denom == 0:
        return 0
    else:
        return secondes / denom



def tempsLectureReponseMoyen(dataframe, utilisateur):
    ecriture = dataframe.loc[(dataframe['Action'] == "Afficher le contenu d'un message")& (dataframe['Utilisateur'] == utilisateur)]["Delai"].tolist()
    if(len(ecriture) == 0):
        return 0
    secondes = 0
    for i in range(1, len(ecriture)):
        if(pd.notna(ecriture[i]) and ecriture[i] != "" ):
            t = datetime.strptime(ecriture[i], '%H:%M:%S').time()
            secondes += (t.hour * 60 + t.minute) * 60 + t.second

    moyenneDelai = secondes /len(ecriture)
    return moyenneDelai


def tempsLectureReponseMoyenGroupe(dataframe, groupe):
    secondes = 0
    denom = len(groupe)
    for utlisateur in groupe:
        val = tempsLectureReponseMoyen(dataframe, utlisateur)
        if(val == 0):
            denom -= 1
        secondes += val
    if denom == 0:
        return 0
    else:
        return secondes / denom
