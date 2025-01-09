import boto3
import json
import time
from JSONprocessor import Json2txt

# Initialize the Transcribe client
transcribe_client = boto3.client('transcribe')
s3_client = boto3.client('s3')

def start_medical_transcription_job(job_name, media_uri, output_bucket_name, language_code, specialty, job_type="CONVERSATION", diarisation = True, max_speakers = 2):
    """
    Start a medical transcription job.
    :param job_name: Unique name for the transcription job.
    :param media_uri: S3 URI of the media file to transcribe.
    :param output_bucket_name: S3 bucket to store the transcription result.
    :param language_code: Language code of the audio (default: 'en-US').
    :param specialty: Medical specialty (default: 'PRIMARYCARE').
    :param type: Type of transcription (default: 'CONVERSATION').
    """
    medical_transcription_settings = {
        "ShowSpeakerLabels": diarisation,
        "MaxSpeakerLabels": max_speakers if diarisation else None,
    }    

    response = transcribe_client.start_medical_transcription_job(
        MedicalTranscriptionJobName=job_name,
        LanguageCode=language_code,
        Media={'MediaFileUri': media_uri},
        OutputBucketName=output_bucket_name,
        Specialty=specialty,
        Type=job_type,
        Settings=medical_transcription_settings,
    )
    return response

def get_medical_transcription_job_status(job_name):
    """
    Get the status of a medical transcription job.
    :param job_name: Name of the transcription job.
    """
    response = transcribe_client.get_medical_transcription_job(
        MedicalTranscriptionJobName=job_name
    )
    return response

def get_transcription_result(file_name):
    """
    Retrieve the transcription result JSON from S3.
    :param transcript_uri: S3 URI of the transcription result.
    :return: Parsed JSON transcription result.
    """
    # Parse the S3 URI

    bucket_name = "jotter-test-bucket"
    object_key = f"medical/{file_name}.json"
    
    # Download the transcription result JSON
    response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
    transcription_json = json.loads(response['Body'].read().decode('utf-8'))
    
    return transcription_json

def main():
    # Configuration
    job_name = "Retrieval_test4"
    media_uri = "s3://jotter-test-bucket/CAR0002-Trimmed.mp3"  # Update with S3 URI
    output_bucket_name = "jotter-test-bucket"  # Update with S3 bucket name
    specialty = "PRIMARYCARE"
    language_code = "en-US"
    # max_speakers="3"


    
    # Start the transcription job
    print("Starting transcription job...")
    start_response = start_medical_transcription_job(job_name, media_uri, output_bucket_name, language_code, specialty)
    print("Transcription job started:", start_response)
    
    # Poll for job completion
    print("Waiting for transcription job to complete...")
    while True:
        status_response = get_medical_transcription_job_status(job_name)
        status = status_response['MedicalTranscriptionJob']['TranscriptionJobStatus']
        if status in ['COMPLETED', 'FAILED']:
            break
        print(f"Job status: {status}. Waiting...")
        time.sleep(10)  # Wait 10 seconds before polling again
    
    # Handle completed or failed job
    if status == 'COMPLETED':
        print("Transcription job completed.")
        transcript_uri = status_response['MedicalTranscriptionJob']['Transcript']['TranscriptFileUri']
        print("Transcript file URI:", transcript_uri)

        # Retrieve and display the transcription result
        transcription_result = get_transcription_result(job_name)
        with open(f"Input/{job_name}.json", "w") as file:
            file.write(json.dumps(transcription_result, indent=4))

        Json2txt(job_name) #tscribes the json output and produces csv,txt files in readable format

    elif status == 'FAILED':
        print("Transcription job failed.")
        print("Failure reason:", status_response['MedicalTranscriptionJob']['FailureReason'])

if __name__ == "__main__":
    main()
