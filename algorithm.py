kismet_sql = 'kismet_file_here'
analysis_sql = 'analysis.db'

def conn(db_file):
    dbconn = None
    try:
        dbconn = sqlite3.connect(db_file)
    except Error as e:
        print(e)

    return dbconn

def getKistmetData():
    cur = conn(kismet_sql).cursor()
    cur.execute("SELECT * FROM devices)

    cur.fetchall()
    
    time_between = data[1] - data[0]
    
    if time_between >= 180:
        cur.execute("DELETE FROM devices WHERE mac_addr='", data[3] ,"'")
    else:
        cur.execute("UPDATE devices SET data_here WHERE mac_addr=",mac_addr,"'")
        # update table



def update(mac_addr):
    cur = conn(analysis_sql).cursor()
    count = cur.execute("SELECT count(mac_addr) FROM devices WHERE mac_addr='",mac_addr,"'")
    
    if count >= 1:
        cur.execute("SELECT * FROM devices WHERE mac_addr='",mac_addr,"'")
        
        if time_between >= 180:
            cur.execute("DELETE FROM devices WHERE mac_addr='", data[3] ,"'")
        else:
            cur.execute("UPDATE devices SET data_here WHERE mac_addr=",mac_addr,"'")
    else:
        cur.execute("INSERT INTO devices (mac_addr, other data...) VALUES ('','','','')")

def updateGUItable():
    cur = conn(analysis_sql).cursor()
    rows = cur.execute("SELECT * FROM devices")
    
    cur.fetchall()
    
    output = ''
    
    for row in rows:
        output += '<tr>'
        output += '<td>' + row[0] + '</td>'
        output += '<td>' + row[1] + '</td>'
        output += '<td>' + row[2] + '</td>'
        output += '<td>' + row[3] + '</td>'
        output += '<td>' + row[4] + '</td>'
        output += '<td>' + row[5] + '</td>'
        output += '</tr>'
    
    # append to table
    
    
    
    
    
    
    
