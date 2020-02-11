import pandas as pd
from siteCollaviz import gestionDate

#Nombre de fois qu'il réponds aux autres dans l'intervalle de Date1 et Date2
def nbReponsesAuxAutres(dataframe, utilisateur, date1, date2):
    listIdMsg = []
    listIdParent= []
    final = []
    dataframeModif = gestionDate.gestionDateDataframe(dataframe, date1, date2)
    tmp = dataframeModif[(dataframeModif.Utilisateur == utilisateur) & (dataframeModif.Action == "Répondre à un message") & (dataframeModif.Attribut.str.contains("IDPARENT=",case = False))].Attribut.tolist()
    for i in tmp:
        listIdParent.append(i[9:])
    for i in listIdParent:
        listIdMsg.append("IDMSG="+i)
    utilisateurPost = dataMapping[(dataMapping.Attribut.isin(listIdMsg)) & ((dataMapping.Action == "Répondre à un message") | (dataMapping.Action == "Poster un nouveau message"))].Utilisateur.unique().tolist()
    for utilisateur in utilisateurPost:
        nbAction = dataframe[(dataframe.Attribut.isin(listIdMsg)) & ((dataframe.Action == "Répondre à un message") | (dataframe.Action == "Poster un nouveau message")) & (dataframe.Utilisateur == utilisateur)].Attribut.count()
        final.append([utilisateur, nbAction])
    return final

def nbReponsesDePersonneGroupe(dataframe, utilisateur, groupe, Date1, Date2):
    tmp = nbReponsesDePersonne(dataframe, utilisateur, Date1, Date2)
    final = [["Users", 0]]
    for i in tmp:
        if i[0] in groupe:
            final.append(i)
        else:
            final[0][1] += i[1]
    return final
