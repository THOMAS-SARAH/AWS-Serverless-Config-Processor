import json
import boto3
from datetime import datetime

s3_client = boto3.client('s3')
BUCKET_NAME = "saas-config-store-sarah"

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}')) if isinstance(event.get('body'), str) else event.get('body', {})
        
        tenant_id = body.get('tenant_id', 'default_tenant')
        config_data = body.get('config', {"status": "active", "tier": "enterprise"})
        
        timestamp = datetime.utcnow().strftime('%Y-%m-%d_%H-%M-%S')
        file_key = f"tenants/{tenant_id}/config_{timestamp}.json"
        
        s3_client.put_object(
            Bucket=BUCKET_NAME,
            Key=file_key,
            Body=json.dumps(config_data, indent=2),
            ContentType='application/json'
        )
        
        return {
            "statusCode": 200,
            "headers": {"Content-Type": "application/json"},
            "body": json.dumps({
                "message": "Tenant configuration processed and persisted successfully",
                "bucket": BUCKET_NAME,
                "s3_key": file_key,
                "processed_at": timestamp
            })
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }
