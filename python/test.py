from pprint import pprint
#from boto import ec2
import boto
import boto.ec2

AWS_ACCESS_KEY_ID = 'AKIAJMH7L7IHP3YIKAZQ'
AWS_SECRET_ACCESS_KEY = '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'
#ec2client = boto3.client('ec2')
ec2conn =  boto.connect_ec2(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
print("hi")
reservations = ec2conn.get_all_instances()
instances = [i for r in reservations for i in r.instances]
for i in instances:
    pprint(i.__dict_)
    break # remove this to list all instances