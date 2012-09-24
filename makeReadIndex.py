""" makeReadIndex.py: Creates a read centered data file and index from a bam file for quick retrieval of read specific data from a NGS experiment. """
__author__ = "Wishva Herath"
__email__ = "wishvamalli@gmail.com"
__copyright__ = "Copyright 2012"
__status__ = "Prototype"
__version__ = "0.0.1"
__license__ = "GPL"

import sys
import sqlite3 #the index is created as an sqlite database.

try:
    db = sys.argv[2].strip()
except:
    "Error: samtools view bamfile | python makeReadIndex.py datafile_name indexdatabase_name"
con = sqlite3.connect(db)
cur = con.cursor()
sql ="CREATE TABLE tblRead (name TEXT, start INT, stop INT)"
cur.execute(sql)
#warning!: indexing makes the dataentry slow but will make the searching faster!
#sql = "CREATE INDEX readIndex on tblRead(name)"
#cur.execute(sql)

dic = {}
while True:
    line = sys.stdin.readline()
    if len(line) == 0:
        break
    readID =  line.strip().split('\t')[0].strip()
    if readID in dic:
        dic[readID] = dic[readID] + '|' + line.strip()
    else:
        dic[readID] = line.strip()

pos = 0
mainFile= open(sys.argv[1],"w")

for d in dic:
    t =  d+"\t"+dic[d]+"\n"
    mainFile.write(t)
    pos2 = pos + len(t)
    cur.execute( "INSERT INTO tblRead VALUES (?,?,?)",(d, pos, pos2))
    pos = pos2
    
mainFile.close()
con.commit()
con.close()
    

