---
name: youtube-watcher
description: Fetch and read transcripts from YouTube videos. Use when you need to summarize a video, answer questions about its content, or extract information from it.
---

# YouTube Watcher

Fetch transcripts from YouTube videos to enable summarization, QA, and content extraction.

## Usage

Provide a YouTube URL. The skill will:
1. Fetch the video transcript (closed captions or auto-generated subtitles)
2. Return the transcript text for analysis

## What You Can Do With It

- **Summarize** a video in bullet points
- **Extract** specific facts, quotes, or data points
- **Answer questions** about the video content
- **Compare** multiple videos on the same topic
- **Build a knowledge base** from video libraries

## Notes

- Works with videos that have closed captions (CC) or auto-generated subtitles
- If a video has no subtitles, the transcript cannot be fetched
- Long videos (1+ hour) will produce long transcripts -- specify what you want extracted

## Example Invocations

```
/youtube-watcher https://www.youtube.com/watch?v=VIDEO_ID
Summarize the main points

/youtube-watcher https://www.youtube.com/watch?v=VIDEO_ID
Extract all statistics and data points mentioned

/youtube-watcher https://www.youtube.com/watch?v=VIDEO_ID
What does the speaker say about pricing?
```
