const { DynamoDBClient } = require("@aws-sdk/client-dynamodb");
const { PutCommand, DynamoDBDocumentClient } = require("@aws-sdk/lib-dynamodb");

const client = new DynamoDBClient({});
const docClient = DynamoDBDocumentClient.from(client);

exports.handler = async (event) => {
    console.log("---*******---start-handler");
    console.log("---*******---event", event);
    
    let TableName = "RaffleUsers";
    let body;

    try {
        if (event.body) {
            try {
                body = JSON.parse(event.body);
            } catch (e) {
                body = event.body;
            }
        } else {
            body = event;
        }
        console.log("---*******---body", body);

        if (!body.email) {
            return "where is your email!";
        } else if (!body.phone) {
            return "where is your phone!";
        } else if (!body.name) {
            return "where is your name!";
        }

        const command = new PutCommand({
            TableName: TableName,
            Item: {
                email: body.email,
                phone: body.phone,
                name: body.name,
                won: "no"
            },
        });

        const dynamo_response = await docClient.send(command);
        console.log("---*******---dynamo-response", dynamo_response);
        return "Thanks, Your data may have been received!";

    } catch (e) {
        console.log("---*******---e", e);
        return e.message;
    }
};
