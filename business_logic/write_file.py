import re
def wirteToFile(fileName,cursor):
    print ("writing in to " + fileName)
    file = open(fileName,'w')
    file.write( re.sub('[r[r]\']', '', str([row[0] for row in cursor.description]) ) +"\n" ) 
    results = cursor.fetchall()  
    for row in results:
        file.write(re.sub('[(\')]', '', str(row))+"\n")
    file.close()
    return