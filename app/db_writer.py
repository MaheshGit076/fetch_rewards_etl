import psycopg2

class DBWriter:
    def __init__(self, config):
        self.conn = psycopg2.connect(**config)
    
    def write_to_db(self, data):
        with self.conn.cursor() as cursor:
            for record in data:
                cursor.execute("""
                    INSERT INTO user_logins (user_id, device_type, masked_ip, masked_device_id, locale, app_version, create_date)
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                """, (
                    record['user_id'],
                    record['device_type'],
                    record['masked_ip'],
                    record['masked_device_id'],
                    record['locale'],
                    record['app_version'],
                    record['create_date']
                ))
        self.conn.commit()
