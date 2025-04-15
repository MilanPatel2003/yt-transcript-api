# YouTube Transcript Serverless API

A minimal Vercel serverless function for fetching YouTube video transcripts using the `youtube-transcript` library.

## Usage

Deploy this folder to Vercel. Then call:

```
GET /api/youtube-transcript?videoId=YOUR_VIDEO_ID
```

Returns an array of transcript entries or an error.

## Example

```
GET https://your-vercel-project.vercel.app/api/youtube-transcript?videoId=dQw4w9WgXcQ
```

## Local development

- Run `npm install` in this folder before deploying or testing locally.
