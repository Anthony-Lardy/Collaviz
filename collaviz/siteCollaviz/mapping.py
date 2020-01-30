import pandas as pd
def mapping(username, fichier, utilisateur, date, heure, titre, attribut, delai, repondre, poster, connexion, forum, message, parent):
    print("date :" + date)
    data = pd.read_csv('./media/' + username + "/" + fichier , encoding="utf-8")
    new_data = data[[utilisateur, date, heure, titre, attribut, delai]]
    columns_dict = {
        utilisateur: "Utilisateur",
        date: "Date",
        heure: "Heure",
        titre: "Action",
        attribut: "Attribut",
        delai: "Delai",
    }
    new_data = new_data.rename(columns=columns_dict)
    cell_dict_Action = {
        repondre: "Répondre à un message",
        poster: "Poster un nouveau message",
        connexion: "Connexion",
    }
    new_data = new_data.rename(columns=columns_dict)
    new_data["Action"] = new_data["Action"].replace(cell_dict_Action)
    new_data["Attribut"] = new_data["Attribut"].replace(regex=[forum], value='IDFORUM=')
    new_data["Attribut"] = new_data["Attribut"].replace(regex=[message], value='IDMSG=')
    new_data["Attribut"] = new_data["Attribut"].replace(regex=[parent], value='IDPARENT=')
    fichier = fichier.replace('.csv','')
    new_data.to_csv('./media/'+ username + "/mapping/" + fichier + "Mapping" + ".csv", encoding='utf-8', index=False)
