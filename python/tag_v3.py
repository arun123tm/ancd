#/usr/bin/python

import boto.ec2
import datetime
import time

conn = boto.ec2.connect_to_region("ap-southeast-1")
reservations = conn.get_all_instances()
for res in reservations:
    for inst in res.instances:
        if "Dev" in inst.tags:
           #ami_id = conn.create_image(inst.id,"WordNew{{timestamp}}",description='Created by AMIBackup', no_reboot=True, dry_run=False)
           #ami_id = conn.create_image(inst.id,"WordNew",description='Created by AMIBackup', no_reboot=True, dry_run=False)
           ami_id="ami-65fdd237"
           print ami_id

           lt=inst.launch_time
           #print lt
           lt=lt[:-5]
           print lt
           y=lt[:-15]
           m=lt[5:-12]
           d=lt[8:-9]
           h=lt[11:-6]
           min=lt[14:-3]
           sec=lt[17:]

           y=int(y)
           m=int(m)
           d=int(d)
           h=int(h)
           min=int(min)
           sec=int(sec)
           print sec

           d1 = datetime.date(y,m,d)
           print "d1",d1.day

           t1=datetime.time(h,min,sec)
           print t1

           today=datetime.date.today()
           print "today=",today


           onemonth = datetime.timedelta(days=30)
           print "onemonth",onemonth.days

           s1 = d1.day + onemonth.days
           s2 = s1 - onemonth.days
           print s2

           if s2 <= 30:
                print('No Termination')
           elif s2 > 30:
                print('Terminate instance')
           else:
                print("bye!!!")

"tag.py" 111L, 2379C                             