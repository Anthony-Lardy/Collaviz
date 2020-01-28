from collections import OrderedDict, defaultdict
import pandas as pd

folder = "./media/tmp/"

def duppliCellulelist(fichier, colonne, separateur):

    data = pd.read_csv(folder + fichier, encoding = 'utf-8')
    row_list = []
    for index, row in data.iterrows():
        if len(row[colonne].split(separateur)) > 1:
            for i in row[colonne].split(separateur):
                row[colonne] = i
                row_list.append(row.to_dict(OrderedDict))
        else:
            row_list.append(row.to_dict(OrderedDict))
    newData = pd.DataFrame(row_list, columns=data.columns)
    fichier = fichier.replace('.csv','')
    newData.to_csv(folder + fichier + "DuppliCell" + ".csv", encoding='utf-8', index=False)
