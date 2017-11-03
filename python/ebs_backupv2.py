import boto.ec2
import datetime
#Connecting to region
conn = boto.ec2.connect_to_region("ap-southeast-1")

#Create Snapshot
#volume_id = raw_input("Enter volume id")
description = str(datetime.date.today())
file =  open("volumeid.txt", "r")
for line in file:
        volume_id = line.rstrip()
        print volume_id
        snapshot = conn.create_snapshot(volume_id,description)
        print snapshot.id
        snaps = conn.get_all_snapshots(filters={'volume-id':volume_id})

        for i in snaps:
                print i,i.start_time
                date = i.start_time
                date1 = date[:-14]
                print "date1", date1
                y = date1[:-6]
                y = int(y)
                m = date[5:-17]
                m = int(m)
                d = date1[8:]
                d = int(d)
                d1 = datetime.date(y,m,d)
                print "snapshot creation date", d1

                today = datetime.date.today()

                diff = today - d1
                diff1 = diff.days
                print diff1

                if diff1 <= 7:
                        print "do not delete snapshot"
                else:
                        print "delete snapshot"

