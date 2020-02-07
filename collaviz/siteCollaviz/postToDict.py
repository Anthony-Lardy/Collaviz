def idMsgtoAll(dataframe, oldParent, newParent):
    if len(newParent) == len(oldParent):
        return newParent
    else:
        idParent = []
        for i in newParent:
            idParent.append("IDPARENT="+i)
        tmp = dataframe[dataframe.Attribut.isin(idParent)]
        utilisateurs, dates, heures = tmp.Utilisateur.tolist(), tmp.Date.tolist(), tmp.Heure.tolist()
        new = dataframe[dataframe.Utilisateur.isin(utilisateurs) & dataframe.Date.isin(dates) & dataframe.Heure.isin(heures) & dataframe.Attribut.str.contains("IDMSG", case=False) & (dataframe.Action == "Répondre à un message")].Attribut.tolist()
        idMsgNew = []
        for x in new:
            idMsgNew.append(x[6:])
        oldParent = newParent.copy()
        for j in idMsgNew:
            if j not in newParent:
                newParent.append(j)
        return idMsgtoAll(dataframe, oldParent, newParent)

def PostToDict(dataframe):
    dictPost = {}
    tmp = dataframe[(dataframe.Action == "Poster un nouveau message") & dataframe.Attribut.str.contains("IDMSG", case=False)].Attribut.tolist()
    idMsg = []
    for x in tmp:
        idMsg.append(x[6:])
    for i in idMsg[0:10]:
        dictPost[i] = idMsgtoAll(dataframe, [], [i])
    return dictPost
