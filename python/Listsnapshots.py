# Name : Listsnapshots.py
# Description : Lists EBS Volume snapshots
# Date of Creation : 03-March-2016
# Language Used : Python [boto,pymssql]

import boto.ec2
import datetime
import csv
import pymssql
import configparser

try:
	file = {}
	config = configparser.ConfigParser()
	config.read('C:\scripts\property.conf')
	credentialFile = config.get("InputFile",'credentialFile')
	regionFile = config.get("InputFile",'regionFile')					
except IOError:
	print "Input file does not exists"
	
try:
	with open(credentialFile,'r') as csvfile:
		reader = csv.DictReader(csvfile)
		for row in reader:
			customer = row['customer']
			aws_access_key_id = row['aws_access_key_id']
			aws_secret_access_key = row['aws_secret_access_key']
			with open(regionFile,'r') as csvfile:
				reader = csv.DictReader(csvfile)
				for row in reader:
					region_name = row['region']
					#Connect to AWS 
					conn = boto.ec2.connect_to_region(region_name)
					#Connection to Database : Reports1
					conndb = pymssql.connect(host=r'Reports1',user='REPORTS1\Administrator', password='awspoc@123', database='Reports')
					cur = conndb.cursor()
					try:
						res = conn.get_all_instances()
						instances = [i for r in res for i in r.instances]
						volumes = conn.get_all_volumes()
						for v in volumes:
							filter = {'block-device-mapping.volume-id':v.id}
							snaps = conn.get_all_snapshots(filters={'volume-id':v.id})
							for i in snaps:
								date = i.start_time
								date1 = date[:-14]
								y = date1[:-6]
								y = int(y)
								m = date[5:-17]
								m = int(m)
								d = date1[8:]
								d = int(d)
								d1 = datetime.date(y,m,d)

								#Calculate age of snapshot
								today = datetime.date.today()
								diff = today - d1
								diff1 = diff.days
								cur.execute("INSERT INTO ebssnapshot VALUES(%s, %s, %s, %s, %s, %d, %s, %s, %s)", (i.id,v.id,i.volume_size,region_name,d1,diff1,i.description,str(datetime.datetime.now()),customer))
								conndb.commit()
						conndb.close()
					except pymssql.OperationalError, e:
						print "Caught an expcetion", e
					except pymssql.ProgrammingError, e:
						print "Caught an exception", e
					except pymssql.DataError, e:
						print "Caught an exception", e
except IOError:
	print "Error Connecting Database"