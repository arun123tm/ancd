from boto.ec2.connection import EC2Connection
from boto.utils import get_instance_metadata

conn = EC2Connection(aws_access_key_id="AKIAJMH7L7IHP3YIKAZQ",aws_secret_access_key="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")
m = get_instance_metadata()
volumes = [v for v in conn.get_all_volumes() if v.attach_data.instance_id == m['instance-id']]

print volumes[0].attach_data.device