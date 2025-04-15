from vercel_python import Response
from youtube_transcript_api import YouTubeTranscriptApi
import json

def handler(request):
    video_id = request.args.get("videoId")
    if not video_id:
        return Response(json.dumps({"error": "Missing videoId"}), status=400, mimetype="application/json")
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        return Response(json.dumps(transcript), status=200, mimetype="application/json")
    except Exception as e:
        return Response(json.dumps({"error": str(e)}), status=500, mimetype="application/json")