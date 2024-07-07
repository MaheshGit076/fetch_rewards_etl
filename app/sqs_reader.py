import boto3

class SQSReader:
    def __init__(self, queue_url):
        self.queue_url = queue_url
        self.sqs = boto3.client('sqs', endpoint_url="http://localhost:4566")

    def read_messages(self):
        response = self.sqs.receive_message(
            QueueUrl=self.queue_url,
            MaxNumberOfMessages=10
        )
        return response.get('Messages', [])
