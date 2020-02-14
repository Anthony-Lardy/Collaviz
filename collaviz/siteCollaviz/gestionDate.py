import datetime
import pandas as pd
def gestionDate(dataFrame, Date1, Date2):
    d=dataFrame['Date'].unique().tolist()
    if Date1 == "" and Date2 != "":
        Date1=d[0].split("-")
        Date2=Date2.split("-")
        start = datetime.date(int(Date1[0]), int(Date1[1]), int(Date1[2]))
        end = datetime.date(int(Date2[0]), int(Date2[1]), int(Date2[2]))
        date_generated = [str(start + datetime.timedelta(x)) for x in range(int((end-start).days)+1)]

    elif Date2 == "" and Date1 != "":

        Date1=Date1.split("-")
        Date2=d[len(d)-1].split("-")
        start = datetime.date(int(Date1[0]), int(Date1[1]), int(Date1[2]))
        end = datetime.date(int(Date2[0]), int(Date2[1]), int(Date2[2]))
        date_generated = [str(start + datetime.timedelta(x)) for x in range(int((end-start).days)+1)]


    elif (Date2 == "") and (Date1 == ""):

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


def getFirstDate(username, fichier):
        dataFrame = pd.read_csv("./media/" + username + "/mapping/" + fichier , encoding='utf-8')
        return dataFrame['Date'].unique().tolist()[0]

def gestionDateDataframe(dataframe, date1, date2):
    if date1 == '' and date2 == '':
        return dataframe
    if date1 == '':
        return dataframe[dataframe.Date <= date2]
    if date2 == '':
        return dataframe[dataframe.Date >= date1]
    else:
        return dataframe[(dataframe.Date >= date1) & (dataframe.Date <= date2)]
