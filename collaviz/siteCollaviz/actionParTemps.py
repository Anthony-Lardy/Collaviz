import pandas as pd
import datetime

def actionParTemps(username, fichier, Utilisateurs, Action, Date1, Date2):
    dataFrame = pd.read_csv("./media/" + username + "/mapping/" + fichier , encoding='utf-8')
    List=[]
    list_nbAction=[]
    for user in Utilisateurs:
        for d in gestionDate(dataFrame, Date1, Date2):

            list_nbAction.append(actionDate(dataFrame, Action, user, d))

        List.append((list_nbAction))
        list_nbAction=[]
    for i in List:
        for j in range(len(i)):
            i[j] = int(i[j])
    return List


def getUsers(username, file):
        dataFrame = pd.read_csv("./media/" + username + "/mapping/" + file, encoding='utf-8')
        return (dataFrame.Utilisateur.unique().tolist())


def actionDate(dataFrame, Action, Utilisateur, Date):
    return dataFrame[(dataFrame['Action'] == Action) & (dataFrame['Utilisateur'] == Utilisateur) & (dataFrame['Date'] == Date)].count()['Date']

def gestionDate(dataFrame, Date1, Date2):

    d=dataFrame['Date'].unique().tolist()
    if Date1 is "" and Date2 is not "":

        Date1=d[0].split("-")
        Date2=Date2.split("-")
        start = datetime.date(int(Date1[0]), int(Date1[1]), int(Date1[2]))
        end = datetime.date(int(Date2[0]), int(Date2[1]), int(Date2[2]))
        date_generated = [str(start + datetime.timedelta(x)) for x in range(int((end-start).days)+1)]

    elif Date2 is "" and Date1 is not "":

        Date1=Date1.split("-")
        Date2=d[len(d)-1].split("-")
        start = datetime.date(int(Date1[0]), int(Date1[1]), int(Date1[2]))
        end = datetime.date(int(Date2[0]), int(Date2[1]), int(Date2[2]))
        date_generated = [str(start + datetime.timedelta(x)) for x in range(int((end-start).days)+1)]


    elif (Date2 is "") and (Date1 is ""):

        Date1=d[0].split("-")
        Date2=d[len(d)-1].split("-")
        start = datetime.date(int(Date1[0]), int(Date1[1]), int(Date1[2]))
        end = datetime.date(int(Date2[0]), int(Date2[1]), int(Date2[2]))
        date_generated = [str(start + datetime.timedelta(x)) for x in range(int((end-start).days)+1)]

    else:

        Date1=Date1.split("-")
        Date2=Date2.split("-")
        start = datetime.date(int(Date1[0]), int(Date1[1]), int(Date1[2]))
        end = datetime.date(int(Date2[0]), int(Date2[1]), int(Date2[2]))
        date_generated = [str(start + datetime.timedelta(x)) for x in range(int((end-start).days)+1)]

    return date_generated
