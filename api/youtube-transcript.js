import { YoutubeTranscript } from "youtube-transcript";

export default async function handler(req, res) {
  const { videoId } = req.query;
  if (!videoId) {
    return res.status(400).json({ error: "Missing videoId" });
  }
  try {
    const transcript = await YoutubeTranscript.fetchTranscript(videoId);
    res.setHeader('Access-Control-Allow-Origin', '*'); // Enable CORS for all origins
    return res.status(200).json(transcript);
  } catch (e) {
    return res.status(500).json({ error: e.message });
  }
}
