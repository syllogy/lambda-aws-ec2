import boto3

region = "us-east-1"
instances = ["INSTANCES-ID"]

ec2 = boto3.client("ec2", region_name=region)

# ==============================================================================
# LAMBDA HANDLER FUNCTION
# ==============================================================================

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print(f"Stopped your instances: {instances}")
