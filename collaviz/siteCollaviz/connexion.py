from datetime import datetime

def tempsMoyenConnexion(dataframe, utilisateur):
    dataframe = dataframe.sort_values(by=['Date', 'Heure'])
    coDate = []
    coHeure = []
    lastDate = []
    lastHeure = []
    erreur = 0
    dataframeConnexion = dataframe[(dataframe.Utilisateur == utilisateur) & (dataframe.Action == 'Connexion')]
    for row in dataframeConnexion.itertuples():
        tmp = dataframe[(dataframe.Date == row.Date) & (dataframe.Heure < row.Heure) & (dataframe.Utilisateur == utilisateur)]
        if(tmp.empty):
            tmp = dataframe[(dataframe.Date < row.Date) & (dataframe.Utilisateur == utilisateur)]
            if(tmp.empty):
                coDate.append(row.Date)
                coHeure.append(row.Heure)
                continue
        last = tmp.iloc[-1]
        lastDate.append(last.Date)
        lastHeure.append(last.Heure)
        coDate.append(row.Date)
        coHeure.append(row.Heure)
    totalseconde = 0
    for i in range(len(lastDate)):
        lastHeure[i] = datetime.strptime(lastHeure[i], '%H:%M:%S').time()
        lastDate[i] = datetime.strptime(lastDate[i], '%Y-%m-%d')
        coDate[i] = datetime.strptime(coDate[i], '%Y-%m-%d')
        datetime_object_last = datetime.combine(lastDate[i], lastHeure[i])
        coHeure[i] = datetime.strptime(coHeure[i], '%H:%M:%S').time()
        datetime_object_co = datetime.combine(coDate[i], coHeure[i])
        if (((datetime_object_last-datetime_object_co).total_seconds() < 84000.0) & ((datetime_object_last-datetime_object_co).total_seconds() > 0.0)):
            totalseconde += (datetime_object_last-datetime_object_co).total_seconds()
        else:
            erreur += 1
    if len(lastDate) == 0 or (len(lastDate)-erreur) == 0:
        return 0
    return ((totalseconde/(len(lastDate)-erreur))/60)/60

def tempsMoyenConnexionall(dataframe):
    utilisateurs = dataframe.Utilisateur.unique()
    erreur = 0
    totalTempsConnexion = 0
    for utilisateur in utilisateurs:
        tmp = tempsMoyenConnexion(dataframe, utilisateur)
        totalTempsConnexion += tmp
        if tmp == 0:
            erreur += 1
    return totalTempsConnexion/(len(utilisateurs)-erreur)
