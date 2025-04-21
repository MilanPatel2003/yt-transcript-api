from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/api/yt_api_server')
def get_transcript():
    video_id = request.args.get("videoId")
    if not video_id:
        return jsonify({"error": "Missing videoId"}), 400
    try:
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        # Extract only the 'text' from each segment and join into a single paragraph
        full_text = ' '.join([segment['text'] for segment in transcript])
        return jsonify({"transcript": full_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)