# import boto3
# from urllib.parse import urlparse
# import json
# import time
# from Transcribe_Retrieve import get_transcription_result

# # Initialize the Transcribe client
# transcribe_client = boto3.client('transcribe')
# s3_client = boto3.client('s3')

# response = s3_client.get_object(Bucket="jotter-test-bucket", Key="medical/Retrieval_test3.json")

# transcription_json = json.loads(response['Body'].read().decode('utf-8'))
# job_name = "Retrieval_test3"
# with open(f"Input/{job_name}.json", "w") as file:
#     file.write(json.dumps(transcription_json, indent=4))



# parsed_uri = urlparse("https://s3.us-east-1.amazonaws.com/jotter-test-bucket/medical/Retrieval_test2.json")
# bucket_name = parsed_uri.netloc
# object_key = parsed_uri.path.lstrip('/')

# print(object_key)
import torch
print(torch.cuda.is_available())