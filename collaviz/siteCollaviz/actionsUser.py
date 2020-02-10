from siteCollaviz import actionDate
import pandas as pd

def actionsParUtilisateur(fichier, Utilisateur, ListOfAction, Date1,Date2):
    dataFrame = pd.read_csv(fichier, encoding='utf-8')
    List=[]
    for action in ListOfAction:
        List.append(actionDate.action2Date(dataFrame, action, Utilisateur, Date1,Date2))
        
    for i in range (len(List)):
        List[i] = int(List[i])

    return List
