import re
import pandas as pd
from datetime import datetime

def is_insert(line):
    return 'INSERT INTO' in line or False

def is_create(line):
    return 'CREATE TABLE' in line or False

def is_finish(line):
    return ';' in line or False

def is_primary(line):
    return 'PRIMARY KEY' in line or False

def get_values(line):
    return line.partition(' VALUES ')[2]

def get_table_name_insert(line):
    match = re.search('INSERT INTO `([0-9_a-zA-Z]+)`', line)
    if match:
        return match.group(1)
    else:
        print(line)

def get_name_categorie_type(line):
    match = re.search('int\([0-9]+\)', line)
    if match:
        return "int"
    else:
        match = re.search('char', line)
        if match:
            return match.group(0)
        else:
            match = re.search('date', line)
            if match:
                return match.group(0)
            else:
                match = re.search('time', line)
                if match:
                    return match.group(0)
                else:
                    match = re.search('text', line)
                    if match:
                        return match.group(0)
                    else:
                        print(line)

def get_table_name_create(line):
    match = re.search('CREATE TABLE IF NOT EXISTS `([0-9_a-zA-Z]+)`', line)
    if match:
        return match.group(1)
    else:
        print(line)

def get_name_categorie(line):
    match = re.search('`([0-9_a-zA-Z]+)`', line)
    if match:
        return match.group(1)
    else:
        print(line)

def get_columns(line):
    match = re.search('INSERT INTO `.*` \(([^\)]+)\)', line)
    if match:
        return list(map(lambda x: x.replace('`', '').strip(), match.group(1).split(',')))

def parse_line(line):
    if line[0] == "(":
        line = line[1:-2]
        line = line.split(", ")
    return line

def sqltopanda(filename):
    d = {}
    type_categorie = {}
    values = []
    table_name = []
    columns = []
    insert = False
    create = False
    reader = open(filename, 'r', encoding='utf-8')
    contenu = reader.read()
    lines = contenu.split("\n")
    j =0

    for line in lines:
        if is_insert(line):
            insert = True
        elif is_create(line):
            table = get_table_name_create(line)
            d[get_table_name_create(line)] = pd.DataFrame()
            type_categorie[get_table_name_create(line)] = []
            create = True
        elif is_finish(line) and create:
            create = False
        if create and not is_create(line) and not is_primary(line):
            d[table][get_name_categorie(line)] = ""
            type_categorie[table].append(get_name_categorie_type(line))
        if (insert and not is_insert(line)) or (is_finish(line) and insert):
            dictio = {}
            values = parse_line(line)
            for i in range(len(values)):
                if values[i] == "NULL":
                    d[table][list(d[table].columns)[i]] = values[i]
                elif type_categorie[table][i] == "int":
                    values[i] = int(values[i])
                elif type_categorie[table][i] == "char":
                    values[i] = str(values[i])
                elif type_categorie[table][i] == "date":
                    values[i] = datetime.strptime(values[i], "'%Y-%m-%d'").date()
                elif type_categorie[table][i] == "time":
                    values[i] = datetime.strptime(values[i], "'%H:%M:%S'").time()
                else:
                    print(type_categorie[table][i], values[i], type(values[i]))
                dictio[d[table].columns[i]] = values[i]
            d[table] = d[table].append(dictio, ignore_index=True)
            if is_finish(line) and insert:
                insert = False
    #return d, type_categorie
    return "test"

# current date and time
deb = datetime.now()
sql, type_categorie = sqltopanda("traceforum.sql")
fin = datetime.now()
print("début =", deb)
print("fin =", fin)
