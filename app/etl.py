import os
import boto3
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from utils import mask_pii
from dotenv import load_dotenv

load_dotenv()

SQS_QUEUE_URL = "http://localhost:4566/000000000000/login-queue"
AWS_REGION = "us-east-1"
DATABASE_URL = os.getenv("DATABASE_URL")

def get_sqs_messages():
    sqs = boto3.client('sqs', region_name=AWS_REGION, endpoint_url='http://localhost:4566')
    response = sqs.receive_message(
        QueueUrl=SQS_QUEUE_URL,
        MaxNumberOfMessages=10,
        WaitTimeSeconds=10
    )
    messages = response.get('Messages', [])
    return messages

def process_message(message_body):
    data = json.loads(message_body)
    data['masked_ip'] = mask_pii(data['ip'])
    data['masked_device_id'] = mask_pii(data['device_id'])
    del data['ip']
    del data['device_id']
    return data

def write_to_postgres(data):
    engine = create_engine(DATABASE_URL)
    Session = sessionmaker(bind=engine)
    session = Session()

    insert_query = """
    INSERT INTO user_logins (user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date)
    VALUES (:user_id, :device_type, :masked_ip, :masked_device_id, :locale, :app_version, :create_date)
    """
    session.execute(insert_query, data)
    session.commit()
    session.close()

def main():
    messages = get_sqs_messages()
    for message in messages:
        data = process_message(message['Body'])
        write_to_postgres(data)

if __name__ == "__main__":
    main()
