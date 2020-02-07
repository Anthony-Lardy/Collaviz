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
