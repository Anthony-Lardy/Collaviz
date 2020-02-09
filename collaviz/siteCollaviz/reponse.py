from siteCollaviz import post
from datetime import datetime

def tempsMoyenPostReponse(dataframe, dictPost, utilisateur):
    postDate = []
    postHeure = []
    repDate = []
    repHeure = []
    erreur = 0
    totalseconde = 0
    for i in dictPost:
        idParent= []
        a, b = post.idMsgtoDateHeurePoster(dataframe, i)
        postDate.append(a)
        postHeure.append(b)
        for j in dictPost[i]:
            idParent.append("IDPARENT="+j)
        tmp = dataframe[dataframe.Attribut.isin(idParent)]
        if utilisateur in tmp.Utilisateur.tolist():
            repDate.append(tmp[tmp.Utilisateur == utilisateur].Date.iloc[0])
            repHeure.append(tmp[tmp.Utilisateur == utilisateur].Heure.iloc[0])
        else:
            repDate.append(0)
            repHeure.append(0)
    for i in range(len(postDate)):
        if repDate[i] == 0:
            erreur += 1
        else:
            postDate[i] = datetime.strptime(postDate[i], '%Y-%m-%d')
            postHeure[i] = datetime.strptime(postHeure[i], '%H:%M:%S').time()
            datetime_object_post = datetime.combine(postDate[i], postHeure[i])
            repDate[i] = datetime.strptime(repDate[i], '%Y-%m-%d')
            repHeure[i]= datetime.strptime(repHeure[i], '%H:%M:%S').time()
            datetime_object_rep = datetime.combine(repDate[i], repHeure[i])
            if (datetime_object_rep-datetime_object_post).total_seconds() <= 0:
                erreur += 1
            else:
                totalseconde += (datetime_object_rep-datetime_object_post).total_seconds()
    if len(postDate) == 0 or (len(postDate)-erreur) == 0:
        return 0
    return  ((totalseconde/(len(postDate)-erreur))/60)/60

def tempsMoyenPostReponseall(dataframe, dictPost):
    utilisateurs = dataframe[dataframe.Action == "Répondre à un message"].Utilisateur.unique().tolist()
    erreur = 0
    totaltemps = 0
    for utilisateur in utilisateurs:
        tmp = tempsMoyenPostReponse(dataframe, dictPost, utilisateur)
        if tmp == 0 or tmp > 100:
            erreur += 1
        else:
            totaltemps += tmp
    return totaltemps/(len(utilisateurs)-erreur)
