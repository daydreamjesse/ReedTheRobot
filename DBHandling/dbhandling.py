import sqlite3
from DBHandling import dbcreation as dbc

def createTable(db, name, rowTitle, rowDataType):
    cmd = [('CREATE TABLE IF NOT EXISTS ' + name + ' ( ')]
    for row in range(len(rowTitle)):
        if row != (len(rowTitle) - 1):
            end = ', '
        else:
            end = ');'
        cmd.append(rowTitle[row] + ' ')
        cmd.append(rowDataType[row] + end)
    finalCmd = ''.join(cmd)
    executeCmd(db, finalCmd)
    print("Detected table " + name + ".")

def insertData(db, table, rows, values):
    cmd = [('INSERT INTO ' + table + '(' + rows + ') VALUES(')]
    end = '");'
    cmd.append('"' + values + end)
    finalCmd = ''.join(cmd)
    executeCmd(db, finalCmd)
    
def deleteData(db, table, condition):
    cmd = ('DELETE FROM ' + table + ' WHERE ' + condition + ';')
    executeCmd(db, cmd)

def retrieveData(db, item, table, limit, offset):
    if limit == 0:
        cmd = ("SELECT " + item + " FROM " + table + ";")
    else:
        cmd = ("SELECT " + item + " FROM " + table + " LIMIT " + str(limit) + " OFFSET " + str(offset) + ";")
    rows = executeCmd(db, cmd)
    return rows

def executeCmd(db, command):
    conn = dbc.dbCreate(db)
    c = conn.cursor()
    c.execute(command)
    if "SELECT" in command:
        return(c.fetchall())
    conn.commit()
    conn.close()
