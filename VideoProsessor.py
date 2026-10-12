import moviepy
import librosa
import soundfile
import os
from PIL import Image, ImageEnhance

gijun=60

models=[]
wheremodel="./inst/"
for item in os.listdir(wheremodel):
    full_path = os.path.join(wheremodel, item)
    if os.path.isdir(full_path):
        models.append(item)

for i,n in enumerate(models):
    print(f"{i+1}: {n}")

instmodel=models[int(input("폴더를 선택하세요 / Select a folder : "))-1]

wherevideo=wheremodel+instmodel+"/"
video=moviepy.VideoFileClip(wherevideo+"original.mp4")

#첫 프레임 저장
video.save_frame(wherevideo+"original.png", t=0)

img = Image.open(wherevideo+'original.png')

back = Image.new('RGB', (100*12, 100*7), color='black')

smallimg = img.resize((100,100))
#smallimg = ImageEnhance.Brightness(img).enhance(0.4)

datas = smallimg.getdata()
newData = []
for item in datas:
    darker=2
    newData.append((item[0]//2, item[1]//2, item[2]//2, 0))
smallimg.putdata(newData)

for n in range(12):
    for m in range(7):
        back.paste(smallimg, (n*100,m*100))

back.save(wherevideo+'back.png')

#영상처리
for n in range(7*12):
    print(f"{n}/{7*12}")
    nowtarget=36+n #C2부터 시작
    
    audio=video.audio
    audio.write_audiofile("temp.wav", fps=44100)


    y, sr = librosa.load("temp.wav", sr=None)
    yp = librosa.effects.pitch_shift(y, sr=sr, n_steps=nowtarget-gijun)

    tempout = "temp.wav"
    soundfile.write(tempout, yp, sr)

    audiochanged = moviepy.AudioFileClip("temp.wav")
    output = video.with_audio(audiochanged)

    output.write_videofile(wherevideo+str(nowtarget)+".mp4",audio_codec="aac",codec="libx264",logger=None)


print("완료되었습니다 / Completed ")