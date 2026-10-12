<a href="README.ko.md">한국어 README</a>

# VideoToPianoV2
```11/13/2025 ~```  
This program takes a video and a MIDI file as input and adjusts the pitch of the video to create a music video.  

### Usage Examples (Please turn on the sound.)
Before processing


https://github.com/user-attachments/assets/787c194f-cd08-49f6-b017-df560cd9bcd1


After processing


https://github.com/user-attachments/assets/d4c803f0-01f0-4ac7-8407-ac6f1294efee


Before processing


https://github.com/user-attachments/assets/a15dc16a-c64b-482c-8888-8583f693bc83


After processing


https://github.com/user-attachments/assets/8c8f985f-fefc-40eb-a5d3-8c13498bbea0


### Requirements
1. A .mp4 video with a 1:1 aspect ratio
2. A MIDI file

### How to Use
Python version 3.13 or lower must be installed.

#### Initial Setup
1. ```git clone https://github.com/SeunggyuKwak/VideoToPianoV2``` or download ```Source code.zip``` from Releases
2. ```pip install -r requirements.txt```

#### Video Processing
1. Create a folder with the desired name in ```/inst```
2. Save the desired video as ```original.mp4``` in ```/inst/{desired folder name}```
3. Run ```VideoProcessor.py``` and enter the number of the folder to be processed
* You only need to run this once per video. (No need to reprocess the video each time you create a new one)

#### Saving MIDI Files
1. Save the desired MIDI file (.mid, .midi) in ```/midi```

#### Video Production
1. Run ```Player.py```
2. Select the desired MIDI file (.mid/.midi) from the file selection dialog
3. Enter the number corresponding to the desired video folder
4. Check the completed video in ```/output/{selected folder name}```

### Areas for Improvement
- Add a feature to automatically detect the key of the video to ensure more accurate note playback.
- Add a feature that accounts for the volume of the notes during processing.
- Add a feature that allows users to select from a variety of instrument types (drums, bass, piano, etc.) so that multiple instruments can be used in a single video.
