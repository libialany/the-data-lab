import boto3
import csv
import json
import os

s3 = boto3.client("s3")

def lambda_handler(event, context):
    # Get bucket + object info from event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # Download file
    download_path = f"/tmp/{os.path.basename(key)}"
    s3.download_file(bucket, key, download_path)
    
    processed_data = []
    
    # Process CSV file
    with open(download_path, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Example: keep only selected fields
            processed_data.append({
                "user": row.get("user_id"),
                "action": row.get("action"),
                "timestamp": row.get("timestamp")
            })
    
    # Upload processed JSON
    output_key = f"processed/{os.path.splitext(key)[0]}.json"
    s3.put_object(
        Bucket="my-analytics-processed",
        Key=output_key,
        Body=json.dumps(processed_data)
    )
    
    return {"status": "success", "records": len(processed_data)}
