from siteCollaviz import gestionDate

def actionDate(dataFrame, Action, Utilisateur, Date):
    return dataFrame[(dataFrame['Action'] == Action) & (dataFrame['Utilisateur'] == Utilisateur) & (dataFrame['Date'] == Date)].count()['Date']

def action2Date(dataFrame, Action, Utilisateur, Date1,Date2):
    List=[]

    for d in gestionDate.gestionDate(dataFrame, Date1, Date2):
        List.append(actionDate(dataFrame, Action, Utilisateur, d))

    return sum(List)
