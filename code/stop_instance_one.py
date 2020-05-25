import os
import json
import boto3

# AWS Region Name
region = os.getenv("AWS_REGION") if os.getenv("AWS_REGION") else "us-east-1"

# AWS EC2 Resource Object
ec2 = boto3.resource("ec2", region_name=region)

# ==============================================================================
# FUNCTION TO GET INSTANCES BY FILTER
# ==============================================================================

def filter_instances():
    # Filter to EC2 Instances
    filters = [{
        'Name': 'tag:env',
        'Values': ['hom']
        },
        {
            'Name': 'instance-state-name', 
            'Values': ['running']
        }
    ]
    # Get all EC2 Instances by Filter
    return ec2.instances.filter(Filters=filters) 

# ==============================================================================
# LAMBDA HANDLER FUNCTION
# ==============================================================================
       
def lambda_handler(event, context):
    # Get Instances
    instances = filter_instances()

    # Get each instance ID of Instances
    RunningInstances = [instance.id for instance in instances]

    # Show Instances
    for index, value in enumerate(RunningInstances):
        print(f"Instance {index} - {value}")

    # Check Instances with tag "env" and value "hom"
    if len(RunningInstances) > 0:
        print(f"Stopping {len(RunningInstances)} instances")
        shuttingDown = ec2.instances.filter(InstanceIds=RunningInstances).stop()
    else:
        print("We don't have any instance in hom to stop")

    return {
        "statusCode": 200,
        "body": json.dumps("success")
    }
