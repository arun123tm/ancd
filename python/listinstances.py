# Name : laststopped.py
# Description : Lists EC2 isntances
# Date of Creation : March-2016
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
					conn = boto.ec2.connect_to_region(region_name,aws_access_key_id=aws_access_key_id,aws_secret_access_key=aws_secret_access_key)
					conndb = pymssql.connect(host=r'Reports1',user='REPORTS1\Administrator', password='awspoc@123', database='Reports')
					reservations = conn.get_all_instances()
					cur = conndb.cursor()
					try:
						for r in reservations:
							for i in r.instances:
								instid = i.id.strip('u')
								state = i.state.strip('u')
								publicip = i.ip_address
								privateip = i.private_ip_address
								reason = i.reason.strip('u')
								vpc = i.vpc_id
								type = i.instance_type
								region = i.placement
								cur.execute("INSERT INTO instance VALUES(%s, %s, %s, %s, %d, %d, %s, %s, %d, %s)", (instid,state,type,region,privateip,publicip,vpc,reason,str(datetime.datetime.now()),customer))
								conndb.commit()
						conn.close()	
					except pymssql.OperationalError, e:
						print "Caught an expcetion", e
					except pymssql.ProgrammingError, e:
						print "Caught an exception", e
					except pymssql.DataError, e:
						print "Caught an exception", e
except IOError:
	print "Error Connecting Database"

				
		