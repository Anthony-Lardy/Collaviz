def nbActionUtilisateur(dataframe, action, utilisateur):
    return len(dataframe[(dataframe.Utilisateur == utilisateur) & (dataframe.Action == action)].Heure.unique().tolist())

def nbActionsUtilisateur(dataframe, actions, utilisateurs):
    final = []
    for utilisateur in utilisateurs:
        tmp = []
        for action in actions:
            nb = nbActionUtilisateur(dataframe, action, utilisateur)
            tmp.append(nb)
        final.append(tmp)
    return final


def nbActionsUtilisateurMoy(dataframe, actions, utilisateurs):
    final = []
    for action in actions:
        moy = 0
        for utilisateur in utilisateurs:
            moy += nbActionUtilisateur(dataframe, action, utilisateur)
        moy = moy / len(utilisateur)
        final.append(moy)
    return final
