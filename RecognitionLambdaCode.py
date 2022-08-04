import json
import boto3

def lambda_handler(event, content):

    client = boto3.client("rekognition")
    s3 = boto3.client("s3")
    fileObj = s3.get_object(Bucket = "***BucketName***", Key="***ImageName***")
    fileContent = fileObj["Body"].read()
    response = client.detect_labels(Image = {"S3Object": {"Bucket":"***BucketName***",
                                                          "Name":"***ImageName***"}},
                                    MacLabels=3, MinConfidence=80)
    print(response)
    return {
        "statusCode": 200,
        "body":json.dumps("Hello from Lambda")
        }
