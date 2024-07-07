# Fetch Rewards Data Engineering Take Home

## Overview
This project reads JSON data from an AWS SQS Queue, masks PII data, and writes the transformed data to a PostgreSQL database.

## Setup
1. Ensure Docker and Docker Compose are installed on your machine.
2. Clone the repository.
3. Build and start the Docker services:
    ```sh
    docker-compose up --build
    ```
4. Verify the data in the PostgreSQL database:
    ```sh
    psql -d postgres -U postgres -p 5432 -h localhost -W
    select * from user_logins;
    ```

## Decisions and Assumptions
- **Reading Messages**: Used boto3 to read messages from the SQS queue.
- **Data Structures**: Utilized dictionaries to handle JSON data.
- **Masking PII**: Used SHA-256 hashing to mask `device_id` and `ip`.
- **Writing to Postgres**: Used psycopg2 to handle database operations.
- **Application Deployment**: The application runs in a Docker container for easy deployment.

## Next Steps
- Implement error handling and logging.
- Add unit tests for individual components.
- Set up CI/CD pipelines for automated testing and deployment.
- Optimize data processing for large-scale datasets.

## Production Deployment
- Use managed services like AWS SQS and RDS for scaling.
- Implement robust monitoring and alerting.
- Secure PII data with encryption and access controls.

## Scaling and PII Recovery
- **Scaling**: Use auto-scaling for SQS consumers and partitioned databases.
- **PII Recovery**: Maintain a secure mapping of original to masked values in a separate, encrypted database.

## Assumptions
- JSON structure in SQS messages is consistent.
- Database schema is fixed as provided.
- Basic Docker and SQL knowledge for setup and verification.

