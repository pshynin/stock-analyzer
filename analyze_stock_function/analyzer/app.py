# import requests

from model.aws.ec2 import AWSEvent
from model.aws.ec2 import EC2InstanceStateChangeNotification
from model.aws.ec2 import Marshaller


def lambda_handler(event, context):
    awsEvent: AWSEvent = Marshaller.unmarshall(event, AWSEvent)
    ec2StateChangeNotification: EC2InstanceStateChangeNotification = awsEvent.detail

    print("Instance " + ec2StateChangeNotification.instance_id + " transitioned to " + ec2StateChangeNotification.state)

    awsEvent.detail_type = "AnalyzeStockFunction updated event of " + awsEvent.detail_type;

    return Marshaller.marshall(awsEvent)
