from datetime import datetime
from datetime import timedelta
import pandas as pd
from datetime import time

def tempsEcritureReponseMoyenToutLeMonde(dataframe):
    utilisateurs = pd.unique(dataframe['Utilisateur'])
    secondes = 0
    denom = len(utilisateurs)
    for utlisateur in utilisateurs:
        val = tempsEcritureReponseMoyen(dataframe, utlisateur)
        if(val == 0):
            denom -= 1
        secondes += val
    if denom == 0:
        return 0
    else:
        return secondes / denom




def tempsEcritureReponseMoyen(dataframe, utilisateur):
    delai = dataframe.loc[((dataframe['Action'] == "Poster un nouveau message") | (dataframe['Action'] == "Répondre à un message")) & (dataframe['Utilisateur'] == utilisateur)]["Delai"].tolist()
    if(len(delai) == 0):
        return 0

    secondes = 0
    for i in range(1, len(delai)):
        t = datetime.strptime(delai[i], '%H:%M:%S').time()
        secondes += (t.hour * 60 + t.minute) * 60 + t.second


    moyenneDelai = secondes /len(delai)
    return moyenneDelai/60

def tempsEcritureReponseMoyenGroupe(dataframe, groupe):
    secondes = 0
    denom = len(groupe)
    for utlisateur in groupe:
        val = tempsEcritureReponseMoyen(dataframe, utlisateur)
        if(val == 0):
            denom -= 1
        secondes += val
    if denom == 0:
        return 0
    else:
        return secondes / denom
