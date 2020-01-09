def mapping(fichier, utilisateur, date, heure, titre, attribut, repondre, poster, forum, message, parent):
    data = pd.read_csv(fichier, encoding="latin-1")
    new_data = data[[utilisateur, date, heure, titre, attribut]]
    columns_dict = {
        utilisateur: "Utilisateur",
        date: "Date",
        heure: "Heure",
        titre: "Action",
        attribut: "Attribut"
    }
    new_data = new_data.rename(columns=columns_dict)
    cell_dict_Action = {
        repondre: "Répondre à un message test",
        poster: "Poster un nouveau message test",
    }
    new_data = new_data.rename(columns=columns_dict)
    new_data["Action"] = new_data["Action"].replace(cell_dict_Action)
    new_data["Attribut"] = new_data["Attribut"].replace(regex=[forum], value='IDFORUMTEST=')
    new_data["Attribut"] = new_data["Attribut"].replace(regex=[message], value='IDMSGTEST=')
    new_data["Attribut"] = new_data["Attribut"].replace(regex=[parent], value='IDPARENTTEST=')
    return new_data
