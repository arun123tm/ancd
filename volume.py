#!/usr/bin/env python2
import boto.ec2
import datetime

REGION = 'us-east-2'
conn = boto.ec2.connect_to_region(REGION,aws_access_key_id="AKIAJGS7V3NG2YXVNFCQ",aws_secret_access_key="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")

def main():
	#List all instances
	reservations = conn.get_all_instances()
	for res in reservations:
		for inst in res.instances:
			if 'Name' in inst.tags:
				print "%s (%s) [%s]" % (inst.tags['Name'], inst.id, inst.state)
			else:
				print "%s [%s]" % (inst.id, inst.state)
				
				
    #List all volumes
	volumes = conn.get_all_volumes()
	for volume in volumes:
		if 'Name' in volume.tags:
			print "%s (%s) (%s)" % (volume.tags['Name'], volume.id,volume.attach_data.instance_id)
		else:
			print "%s  (%s)" % (volume.id,volume.attach_data.instance_id)
        #print volume

        # Match to an instance id
        #print volume.attach_data.instance_id
	
		
	#Creating the snapshot
	volume_id = raw_input("Enter volume id")
	snapshot = conn.create_snapshot(volume_id, "EC2 daily snapshot")
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

        # # Object attributes:
        # print volume.__dict__

        # # Object methods:
        # print(dir(volume))

if __name__ == '__main__':
    main()