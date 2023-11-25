# YouTube Transcription and ChatGPT Summarizer

<p align="left">
    <img src="https://img.shields.io/github/stars/msarnacki/YouTubeVid_Summary_ChatGPT"/>
    <img src="https://img.shields.io/github/watchers/msarnacki/YouTubeVid_Summary_ChatGPT"/>
    <img src="https://img.shields.io/github/commit-activity/t/msarnacki/YouTubeVid_Summary_ChatGPT"/>
    <img src="https://img.shields.io/github/last-commit/msarnacki/YouTubeVid_Summary_ChatGPT"/>
    <img src="https://img.shields.io/github/issues/msarnacki/YouTubeVid_Summary_ChatGPT"/>
    <img src="https://img.shields.io/github/languages/top/msarnacki/YouTubeVid_Summary_ChatGPT"/>
    <img src="https://img.shields.io/github/repo-size/msarnacki/YouTubeVid_Summary_ChatGPT"/>
</p>

## Overview

This GitHub repository contains a project focused on extracting transcriptions from YouTube videos and leveraging **ChatGPT** for generating summaries. The goal is to provide interface for downloading video transcriptions and obtaining concise summaries with customizable focus areas.

Using my script you can easly analyze the topics mentioned in the youtube videos, get the sentiment from few videos at once or easly get the video transcription to be summarized on specific issue by **ChatGPT** for you to save time on watching.

## Features

### 1. YouTube Transcription
Easily download transcriptions of YouTube videos by providing the video URL. The project utilizes [*youtube_transcript_api*](https://pypi.org/project/youtube-transcript-api/) for efficient extraction. 
- If the CC is not enabled on the video it gets the automatic generated ones for English. 
- If there are no Closed Captions for a polish video that is not automatically transribed by youtube then the script downloads the video in MP4, converts it to WAV, splits into smaller parts and then gets text from speech using [*SpeechRecognition*](https://pypi.org/project/SpeechRecognition/) - at the end translates the transcription to English using [*googletrans*](https://pypi.org/project/googletrans/).

### 2. ChatGPT Summarization
Integrate the powerful ChatGPT language model [*OpenAI API*](https://openai.com/product) to generate insightful summaries. Users can customize the summary by specifying key areas of focus, ensuring a tailored and relevant summary.

### 3. Possibility to run the code for many videos at once
You can run a script for few videos and then get the summarization of all of them at once. It makes it easy to get the sentiment from the videos about a particular topic without watching all of them!


### Technologies used:
- Python 3
- youtube_transcript_api
- SpeechRecognition
- googletrans
- pydub
- OpenAI API
- git

## Installation

Follow these steps to set up the project:

Clone the repository:
   ```bash
   git clone https://github.com/your-username/YouTube-Transcription-ChatGPT-Summarizer.git
   cd YouTube-Transcription-ChatGPT-Summarizer

    Install dependencies:

    pip install -r requirements.txt
```

Get you OpenAI API key from [here](https://openai.com/product) and setup it in *chatgpt_api_key.txt* file.

Run the application:

    python main.py

Usage

    Run the application using the provided script.
    Enter the YouTube videos URL (part of URL that comes after https://www.youtube.com/watch?v=) in video_ids.txt to download the transcriptions.
    Use ChatGPT to generate a summary, specifying focus areas if desired.