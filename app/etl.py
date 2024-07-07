from sqs_reader import SQSReader
from data_transformer import DataTransformer
from db_writer import DBWriter

def main():
    sqs_queue_url = "http://localhost:4566/000000000000/login-queue"
    postgres_config = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': 'postgres',
        'host': 'localhost'
    }

    sqs_reader = SQSReader(sqs_queue_url)
    data_transformer = DataTransformer()
    db_writer = DBWriter(postgres_config)

    messages = sqs_reader.read_messages()
    transformed_data = data_transformer.transform(messages)
    db_writer.write_to_db(transformed_data)

if __name__ == "__main__":
    main()
