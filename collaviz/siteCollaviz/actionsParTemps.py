from siteCollaviz import gestionDate
from siteCollaviz import actionDate
import pandas as pd

def actionsParTemps(dataFrame, Actions, Utilisateur, Date1, Date2):
    dataFrame = pd.read_csv(dataFrame, encoding='utf-8')
    List=[]
    list_nbAction=[]
    for action in Actions:
        list_nbAction=[]
        for d in gestionDate.gestionDate(dataFrame, Date1, Date2):
            list_nbAction.append(actionDate.actionDate(dataFrame, action, Utilisateur, d))

        List.append(list_nbAction)
        for i in List:
            for j in range(len(i)):
                i[j] = int(i[j])

    return List

def actionsParTempsAll(dataframe, actions, Date1, Date2):
    somme = np.array(actionsParTemps(dataFrame, actions, dataframe.Utilisateur.unique()[0], Date1, Date2)).astype(float)
    user = 0
    for utilisateur in dataframe.Utilisateur.unique():
        actif = 0
        for action in actions:
            actif += action2Date(dataframe, action, utilisateur, Date1, Date2)
        if actif is not 0:
            user += 1
            tmp = np.array(actionsParTemps(dataFrame, actions, utilisateur, Date1, Date2))
            somme[0] += tmp[0]
            somme[1] += tmp[1]
            somme[2] += tmp[2]
    if user == 0:
        return somme
    else:
        for i in range(len(somme)):
            for j in range (len(somme[i])):
                somme[i][j] = round(somme[i][j]/user, 2)
    return somme
