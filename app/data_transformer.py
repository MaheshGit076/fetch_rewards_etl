import hashlib

class DataTransformer:
    @staticmethod
    def mask_value(value):
        return hashlib.sha256(value.encode()).hexdigest()

    def transform(self, messages):
        transformed_data = []
        for message in messages:
            body = message['Body']
            user_data = self.parse_json(body)
            user_data['masked_ip'] = self.mask_value(user_data['ip'])
            user_data['masked_device_id'] = self.mask_value(user_data['device_id'])
            transformed_data.append(user_data)
        return transformed_data

    @staticmethod
    def parse_json(data):
        import json
        return json.loads(data)
