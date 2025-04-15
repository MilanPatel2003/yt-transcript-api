from youtube_transcript_api import YouTubeTranscriptApi
import json

def handler(event, context):
    request = event
    video_id = request.get("queryStringParameters", {}).get("videoId")
    if not video_id:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Missing videoId"}),
            "headers": {"Content-Type": "application/json"}
        }
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return {
            "statusCode": 200,
            "body": json.dumps(transcript),
            "headers": {"Content-Type": "application/json"}
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)}),
            "headers": {"Content-Type": "application/json"}
        }