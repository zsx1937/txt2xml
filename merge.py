import os
import sys
path="/Users/zsx/Desktop/myVOC2007/JPEGImages/"
result="/Users/zsx/Desktop/myVOC2007/all.txt"
rf = open(result, 'w')
filecount=0
for root,dirs,files in os.walk(path):
      for name in files:
            filecount=filecount+1
            rf.write(name.replace(".jpg","")+'\n')
rf.close()
print("filecount ",filecount)
      
