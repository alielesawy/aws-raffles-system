const { DynamoDBClient } = require("@aws-sdk/client-dynamodb");
const { DynamoDBDocumentClient, ScanCommand, UpdateCommand } = require("@aws-sdk/lib-dynamodb");

const dynamo = new DynamoDBClient({});
const client = DynamoDBDocumentClient.from(dynamo);

module.exports.handler = async (event) => {
    console.log("---*******---start-handler");
    console.log("---*******---event", event);
    let TableName = "RaffleUsers";
    let winners_count = 3;
    try 
    {
        console.log("---*******---try");
        
        const command = new ScanCommand({
          FilterExpression: "won = :w",
          ExpressionAttributeValues: {
            ":w": "no"
          },
          TableName: TableName
        });
        
        const data = await client.send(command);

        console.log("---*******---items-count", data.Items.length);

        if(data.Items.length < winners_count){
          return "There is no enough data! " + data.Items.length + " only";
        }
        
        let indecis = [];
        let winners = [];
        for(let i =0; i < winners_count; i++){
            let newIndex = Math.floor(Math.random() * data.Items.length);
            if (indecis[0] == newIndex || indecis[1] == newIndex || indecis[2] == newIndex)
            {
                i--;
                continue;
            }
            indecis[i] = newIndex ;
            winners.push(data.Items[newIndex]);
        }
        
        for(let i = 0; i < winners.length; i++){

            const update_command = new UpdateCommand({
              TableName: TableName,
              Key: {
                email: winners[i].email
              },
              UpdateExpression: 'set won = :r',
              ExpressionAttributeValues: {
                ':r': 'yes',
              }
            });
            const response = await client.send(update_command);
            console.log(response);
        }
        
        return {
            "winners": winners
        };
        
    } catch (err) {
        console.log(err);
        return err.message;
    }
};
