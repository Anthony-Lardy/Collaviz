from siteCollaviz import actionDate
import pandas as pd

def actionPourUtilisateurs(fichier, Action, Utilsateurs, Date1, Date2):
    dataFrame = pd.read_csv(fichier, encoding='utf-8')
    List=[]
    for user in Utilsateurs:
        List.append(actionDate.action2Date(dataFrame, Action, user, Date1,Date2))

    for i in range (len(List)):
        List[i] = int(List[i])

    return List
