import re
import pandas as pd
import csv
import os
from datetime import datetime
import unidecode
folder = "./media/tmp/"
def is_create(line):
    return 'CREATE TABLE' in line or False

def is_insert(line):
    return 'INSERT INTO' in line or False

def is_finish(line):
    return ';' in line or False

def get_table_name_create(line):
    match = re.search('CREATE TABLE IF NOT EXISTS `([0-9_a-zA-Z]+)`', line)
    if match:
        return match.group(1)
    else:
        print(line)

def get_table_name_insert(line):
    match = re.search('INSERT INTO `([0-9_a-zA-Z]+)`', line)
    if match:
        return match.group(1)
    else:
        print(line)

def create_csv_file(filename):
    filename += ".csv"
    open(folder + filename, 'w')

def set_values_insert(line, file):
    #s = ","
    p = re.compile('`([0-9_a-zA-Z]+)`')
    writer = csv.writer(file)
    writer.writerow(p.findall(line)[1:])

def is_non_zero_file(fpath):
    return os.path.isfile(fpath) and os.path.getsize(fpath) > 0

def sql_to_csv(sqlfile):
    reader = open(folder + sqlfile, 'r', encoding='utf-8')
    contenu = reader.read()
    lines = contenu.split("\n")
    insert = False
    for line in lines:
        line = unidecode.unidecode(line)
        if insert and (not is_insert(line)):
            writer = csv.writer(file)
            writer.writerow(line[1:-1].replace("',",",").replace(" '", ' ').replace("')", ")")[:-1].split(", "))
        if is_create(line):
            create_csv_file(get_table_name_create(line))
        if is_insert(line):
            filename = get_table_name_insert(line)
            insert = True
            if not is_non_zero_file(folder + filename +".csv"):
                file = open(folder + filename + ".csv", 'a')
                set_values_insert(line, file)
        if is_finish(line):
            insert = False


def nbActions(data, Action, Utilisateur):
    return data[(data['Titre'] == Action) & (data['Utilisateur'] == Utilisateur)].count()['IDTran']

def nbActionsall(file, Action):
  data = pd.read_csv(file, encoding = "utf-8")
  data.head()
  all = []
  utilisateurs = data['Utilisateur'].unique().tolist()
  for Utilisateur in utilisateurs:
      tmp = []
      tmp.append(Utilisateur)
      tmp.append(nbActions(data, Action, Utilisateur))
      all.append(tmp)
  return all
