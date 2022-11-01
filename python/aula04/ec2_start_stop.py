import boto3

instance_id = 'i-0aa98dbe10772436e'

ec2_client = boto3.client('ec2', region_name='us-east-1')

def action_instance():
    response = ec2_client.stop_instances(
        InstanceIds = [instance_id]
    )

    print(response)

action_instance()