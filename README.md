# AWS Raffles System
![AWS Icon](icons/icons8-aws1.svg)

## Project Overview
The AWS Raffles System is a serverless application designed to manage raffle entries and draw winners. This project leverages various AWS services to create a scalable, secure, and efficient system.

## Features
1. **Simple HTML and CSS Page**: A user-friendly interface for participants to enter the raffle.
2. **DynamoDB Table**: Stores raffle entries with participant details.
3. **Lambda Function**: Handles backend logic for processing entries and drawing winners.
4. **API Gateway**: Exposes APIs for the frontend to interact with the backend services.
5. **Mutual TLS Authentication**: Ensures secure communication between clients and the API Gateway.
6. **Hosting on S3 and CloudFront**: Serves the HTML page with low latency and high availability.

## Automation
This project automates 90% of the setup steps, including:

1. **DynamoDB Table Creation**: Automatically creates the DynamoDB table with the required attributes.
2. **Lambda Functions Deployment**: Deploys the necessary Lambda functions for handling raffle entries, counting records, and drawing winners.
3. **API Gateway Configuration**: Sets up the API Gateway with the required endpoints and mutual TLS authentication.
4. **SSL/TLS Certificates Generation**: Automates the generation of self-signed SSL/TLS certificates using OpenSSL.
5. **S3 and CloudFront Setup**: Configures S3 for hosting the HTML page and sets up CloudFront for global content distribution.

This automation significantly reduces the manual effort required to set up the project, allowing you to focus on customization and enhancements.

## Resource was Created using boto3
To use the project, follow these steps:

1. **Install boto3**:
    ```sh
    pip install boto3
    ```

2. **Install AWS CLI**:
    Follow the instructions [here](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) to install the AWS CLI.

3. **Configure AWS CLI**:
    ```sh
    aws configure
    ```
    Provide your AWS access key, secret key, region, and output format when prompted.

## AWS Services Used
- ![S3 Icon](icons/SimpleStorageService.svg) **Amazon S3**: Hosts the static HTML and CSS files.
- ![API Icon](icons/APIGateway.svg) **Amazon API Gateway**: Manages API requests and routes them to the appropriate Lambda functions.
- ![CloudFront Icon](icons/CloudFront.svg) **Amazon CloudFront**: Distributes the content globally with low latency.
- ![Lambda Icon](icons/Lambda.svg) **AWS Lambda**: Executes backend logic without provisioning servers.
- ![DynamoDB Icon](icons/DynamoDB.svg) **Amazon DynamoDB**: Stores raffle entries in a NoSQL database.
- ![ACM Icon](icons/CertificateManager.svg) **AWS Certificate Manager**: Manages SSL/TLS certificates for secure communication.
- ![Route 53 Icon](icons/Route53.svg) **Amazon Route 53**: Manages DNS and routes traffic to the CloudFront distribution.

## Project throughout
1. **Create DynamoDB Table**:
   - Use the provided script to create a DynamoDB table with the necessary attributes.
   - Ensure the table has `email` as the partition key, and additional attributes for `phone_number` and `full_name`.

2. **Create 3 Lambda Functions**:
   - For adding record to DynamoDB table
   - To get the count of records on the Table
   - To Draw the winners

3. **Create API Gateway**:
   - Set up API Gateway to expose the necessary endpoints for the frontend to interact with the backend.

4. **Configure Mutual TLS Authentication**:
    - **Generate SSL/TLS Certificates**:
        - Download and install OpenSSL from [here](https://www.openssl.org/source/).
        - Follow these steps to generate a self-signed certificate:
          ```sh
          openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365 -nodes
          ```
        - Provide the necessary information when prompted, such as country, state, and organization name.
        - Use the generated `key.pem` and `cert.pem` files for mutual TLS authentication.
    - **Enable Mutual TLS Authentication**:
        - Configure mutual TLS authentication on the API Gateway to secure communication.
        - For detailed instructions, see the following [documentation](https://aws.amazon.com/ar/blogs/compute/introducing-mutual-tls-authentication-for-amazon-api-gateway/).

5. **Host HTML Page on S3 and CloudFront**:
   - Upload your HTML and CSS files to an S3 bucket.
   - Set up a CloudFront distribution to serve the content globally.
## Demo
### Video Demo
Watch the project demo video below to see the AWS Raffles System in action:

[![Watch the video](https://img.youtube.com/vi/9qJMTd4EzAI/0.jpg)]([https://www.youtube.com/watch?v=9qJMTd4EzAI](https://youtu.be/Ica3JqMlgBM))

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact
For any questions or inquiries, please contact [here](mailto:alielesawy811@gmail.com).
