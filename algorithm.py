kismet_sql = 'kismet_file_here'
analysis_sql = 'analysis.db'

def getEpochTime():
    dt = datetime.datetime.now()
    epoch_time = datetime(1970, 1, 1)
    delta = abs(dt - epoch)
    return delta.total_seconds()

now = getEpochTime()

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
    
    # last seen - now
    last_between = data[1] - now
    first_between = data[0] - now
    
    if last_between <= 180:
        if first_between :
                print('send alert')
        # ignore because data is under 3 minutes since last seen
    else:
        cur.execute("UPDATE devices SET data_here WHERE mac_addr=",mac_addr,"'")
        # update table



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




# Best working time example
now = 1666747998

first_seen = 1666747331
last_seen = 1666747931

print((now - first_seen) / 60)
print((now - last_seen) / 60)

last_between = last_seen - now
first_between = first_seen - now

dist = 16.000002

if last_between <= 120:
    print('Alert: secondary, stay alert. Distance = x meters, followed for ', last_between)
    
    if first_between <= 240:
        print('ALERT: RED - You\'re being followed, approximate distance: ', dist)
        print('Details: mac_addr, ')
        print('Added data to forensics database for further investigation')
else:
    print('timed out')

Limitations:
    natable for lack of range - follower would have to be within 30 meters of your wireless access point


                
                
                
                

count = cur.execute("SELECT count(mac_addr) FROM whitelist WHERE mac_addr=' + mac_addr + '")
print(count)

if count = 0:
    # not in whitelist, proceeeeeeeeeed

# to add to whitelist:
cur.execute("INSERT INTO whitelist (timestamp, mac_addr) values ('now', mac_addr')")
