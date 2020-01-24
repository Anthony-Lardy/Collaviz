import pandas as pd

def actionParTemps(Utilisateurs, Action, Date1, Date2):
    print(Utilisateurs, "----------------------------------------   ")
    dataFrame = pd.read_csv("./media/tmp/transitionDuppliCellMapping.csv", encoding='utf-8')
    List=[]
    list_nbAction=[]
    for user in Utilisateurs:
        for d in dataFrame['Date'].unique().tolist():
            if Date1 is None and Date2 is not None:
                if (d <= Date2):
                    list_nbAction.append(actionDate(dataFrame, Action, user, d))

            elif Date2 is None and Date1 is not None:
                if (d >= Date1):
                    list_nbAction.append(actionDate(dataFrame, Action, user, d))

            elif (Date2 is None) and (Date1 is None):
                list_nbAction.append(actionDate(dataFrame, Action, user, d))

            else:
                if ((d >= Date1) and (d <= Date2)):
                    list_nbAction.append(actionDate(dataFrame, Action, user, d))


        List.append(list_nbAction)
        list_nbAction=[]

    for i in List:
        print(i)
        for j in range(len(i)):
            i[j] = int(i[j])
    return List


def actionDate(dataFrame, Action, Utilisateur, Date):
    return dataFrame[(dataFrame['Action'] == Action) & (dataFrame['Utilisateur'] == Utilisateur) & (dataFrame['Date'] == Date)].count()['Date']
