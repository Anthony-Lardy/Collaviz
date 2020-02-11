import pandas as pd
from siteCollaviz import gestionDate

# Nombre de fois que les autres lui ont répondu
def nbReponsesParPersonne(dataframe, utilisateur, date1, date2):
    tmp = dataframe[(dataframe.Utilisateur == utilisateur) & ((dataframe.Action == "Poster un nouveau message") | (dataframe.Action == "Répondre à un message")) & (dataframe.Attribut.str.contains("IDMSG=", case=False))].Attribut.tolist()
    listIdMsg = []
    listIdParent= []
    final = []
    for i in tmp:
        listIdMsg.append(i[6:])
    for i in listIdMsg:
            listIdParent.append("IDPARENT="+i)
    dataframeModif = gestionDate.gestionDateDataframe(dataframe, date1, date2)
    utilisateurRep = dataframeModif[(dataframeModif.Attribut.isin(listIdParent)) & (dataframeModif.Action == "Répondre à un message")].Utilisateur.unique().tolist()
    for utilisateur in utilisateurRep:
        nbAction = dataframeModif[(dataframeModif.Attribut.isin(listIdParent)) & (dataframeModif.Action == "Répondre à un message") & (dataframeModif.Utilisateur == utilisateur)].Utilisateur.count()
        final.append([utilisateur, nbAction])
    return final

def nbReponsesParPersonneGroupe(dataframe, utilisateur, groupe, Date1, Date2):
    tmp = nbReponsesParPersonne(dataframe, utilisateur, Date1, Date2)
    final = [["Users", 0]]
    for i in tmp:
        if i[0] in groupe:
            final.append(i)
        else:
            final[0][1] += i[1]
    return final
