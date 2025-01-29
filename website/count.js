const { DynamoDBClient, ScanCommand } = require("@aws-sdk/client-dynamodb");

const client = new DynamoDBClient({});

module.exports.handler = async (event, context) => {
    console.log("---*******---start-handler");
    console.log("---*******---event", event);

    let TableName = "RaffleUsers";

    try {
        const command = new ScanCommand({
            TableName: TableName,
            Select: "COUNT"
        });

        const response = await client.send(command);

        console.log("---*******---count", response);
        return response.Count;
    } catch (e) {
        console.log("---*******---e", e);
        return { error: e.message };
    }
};
