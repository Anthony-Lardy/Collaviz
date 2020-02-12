import pandas as pd
from datetime import timedelta
import numpy as np
from siteCollaviz import gestionDate
def tempsDeReponseMoyen(dataFrame, listUtilisateurs, Date1, Date2):

    FinalList=[]
    for Utilisateur in listUtilisateurs:
        NewList=[]

        for d in gestionDate.gestionDate(dataFrame, Date1, Date2):

            for elem in dataFrame[(dataFrame['Utilisateur']==Utilisateur) & (dataFrame['Date'] == d)]['Attribut'].tolist():
                countIDPARENT=0
                countIDMSG=0
                if elem[0:8]=="IDPARENT":

                    duree1=timedelta(hours=int(0), minutes=int(0), seconds=int(0))
                    duree2=timedelta(hours=int(0), minutes=int(0), seconds=int(0))
                    for heure1 in dataFrame[(dataFrame['Date'] == d) & (dataFrame['Attribut']=="IDPARENT="+elem[9:]) & (dataFrame['Action']=='Répondre à un message')]['Heure'].tolist():
                        heure1=heure1.split(":")
                        duree1+= timedelta(hours=int(heure1[0]), minutes=int(heure1[1]), seconds=int(heure1[2]))
                        countIDPARENT+=1

                    for heure2 in dataFrame[(dataFrame['Date'] == d) & (dataFrame['Attribut']=="IDMSG="+elem[9:]) & (dataFrame['Action']=='Poster un nouveau message')]['Heure'].tolist():
                        heure2=heure2.split(":")
                        duree2+= timedelta(hours=int(heure2[0]), minutes=int(heure2[1]), seconds=int(heure2[2]))
                        countIDMSG+=1

                    if duree2!=timedelta(hours=int(0), minutes=int(0), seconds=int(0)):

                        duree1=duree1.total_seconds()/countIDPARENT
                        duree2=duree2.total_seconds()/countIDMSG
                        NewList.append(np.abs(duree1-duree2))
        if(len(NewList) == 0):
            FinalList.append(0)
        else:
            FinalList.append((int((sum(NewList)/len(NewList)))))
    return FinalList


def tempsDeReponseMoyenall(dataframe, Date1, Date2):
    tempsAll = 0
    erreur = 0
    tab = tempsDeReponseMoyen(dataframe, dataframe.Utilisateur.unique(), Date1, Date2)
    for temps in tab:
        if temps == 0:
            erreur += 1
        else:
            tempsAll += temps
    return tempsAll/((len(dataframe.Utilisateur.unique())-erreur))

def tempsDeReponseMoyenGroupSomme(dataframe, listUtilisateurs, Date1, Date2):
        return sum(tempsDeReponseMoyen(dataframe, listUtilisateurs, Date1, Date2))


def indicateurTempsMoyen(fichier, utilisateur, listUsers, Date1, Date2):
    dataframe = pd.read_csv(fichier, encoding='utf-8')
    tempsUti = tempsDeReponseMoyen(dataframe, [utilisateur], Date1, Date2)[0]
    tempsAll = tempsDeReponseMoyenall(dataframe, Date1, Date2)
    tempsGroupe = tempsDeReponseMoyenGroupSomme(dataframe, listUsers, Date1, Date2)
    return [tempsUti, tempsAll, tempsGroupe]
