# Name : Listvolumes.py
# Description : Lists EBS Volumes
# Date of Creation : 03-March-2016
# Language Used : Python [boto,pymssql]

import boto.ec2
import datetime
import csv
#import pymssql
import configparser

try:
	file = {}
	config = configparser.ConfigParser()
	config.read('C:\Users\bharbs\Desktop\New folder\property.conf')
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
					conn = boto.ec2.connect_to_region(region_name)
					#Connection to Database : Reports1
					#conndb = pymssql.connect(host=r'Reports1',user='REPORTS1\Administrator', password='awspoc@123', database='Reports')
					#print conndb
					#Define cursor
					#cur = conndb.cursor()
					try:
						res = conn.get_all_instances()
						instances = [i for r in res for i in r.instances]
						volumes = conn.get_all_volumes()
						for v in volumes:
							filter = {'block-device-mapping.volume-id':v.id}
							
							if v.attachment_state() == None:
								print v.id,customer
								#cur.execute("INSERT INTO volumes VALUES(%s, %s, %s, %d, %s, %s, %d, %s)", (v.id,'',v.attach_data.device,v.size,v.attachment_state(),region_name,str(datetime.datetime.now()),customer))
								#conndb.commit()
						else:
							ec2 = conn.get_all_instances(filters=filter)
							id = [z for k in ec2 for z in k.instances]
							for i in id:
								print v.id,customer
								#cur.execute("INSERT INTO volumes VALUES(%s, %s, %s, %d, %s, %s, %d, %s)", (v.id,i.id,v.attach_data.device,v.size,v.attachment_state(),region_name,str(datetime.datetime.now()),customer))
								#Commit changes to database
								#conndb.commit()
					#except pymssql.OperationalError, e:
						#print "Caught an expcetion", e
					#except pymssql.ProgrammingError, e:
						#print "Caught an exception", e
					#except pymssql.DataError, e:
						#print "Caught an exception", e
		
				#Close database connection
				#conndb.close()
 except IOError:
	print "Error Connecting Database"