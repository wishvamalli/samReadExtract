""" getReads.py: Extracts read specific information from a processed file generated using a bam file """

__author__ = "Wishva Herath"
__email__ = "wishvamalli@gmail.com"
__copyright__ = "Copyright 2012"
__status__ = "Prototype"
__version__ = "0.0.1"
__license__ = "GPL"

import sys
import gzip
import sqlite3

mainFile = sys.argv[1].strip()
db = sys.argv[2].strip()
readList = sys.argv[3].strip() #comma seperated list of reads no spaces

con = sqlite3.connect(db)
cur = con.cursor()


def getRead(readID):
    
    cur.execute("SELECT * FROM tblRead WHERE name = ?",(readID,))
    d = cur.fetchone()
    start = int(d[1])
    stop = int(d[2])
    fm.seek(start)
    print fm.read(stop-start)
    


#start reading the main file

fm = gzip.open(mainFile,"rb")
fm.seek(0)

#going though the list

if ',' in readList:
    #multiple entries
    for r in readList.strip().split(','):
        getRead(r)
    
else:
    getRead(readList.strip())
    
con.close()
fm.close()

