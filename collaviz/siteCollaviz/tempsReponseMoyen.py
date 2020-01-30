import pandas as pd

def tempsDeReponseMoyen(fichier, nb, Date1, Date2):
    dataFrame = pd.read_csv(fichier, encoding='utf-8')
    FinalList=[]
    for Utilisateur in listUtilisateurs:
        NewList=[]

        for d in gestionDate(dataFrame, Date1, Date2):
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



        FinalList.append((Utilisateur,int((sum(NewList)/len(NewList)))))

    return FinalList
