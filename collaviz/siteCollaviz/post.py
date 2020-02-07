def idMsgtoDateHeurePoster(dataframe, idMsg):
    return dataframe[dataframe.Attribut.str.contains("IDMSG=" + idMsg, case=False) & (dataframe.Action == "Poster un nouveau message")].Date.iloc[0], dataframe[dataframe.Attribut.str.contains("IDMSG=" + idMsg, case=False) & (dataframe.Action == "Poster un nouveau message")].Heure.iloc[0]
