import boto3
def lambda_handler(event, context):

	#To get list of regions
	ec2_client = boto3.client('ec2')
	regions = [region['RegionName']
		for region in ec2_client.describe_regions()['Regions']]

	#To iterate over each regions
	for region in regions:
		ec2 = boto3.resource('ec2', region_name=region)
		print("region : ", region)
		#To get only instances in running state
		instances - ec2.instances.filter(
			Filters=[{'Name': 'instance-state-name','Values':[+'running']}])
		#To to stopr running instances
		for instance in instances:
			instance.stop()
					print('Stopped instance : ',instance.id)
