import moviepy
from tkinter import filedialog
from datetime import datetime
import os
import mido

#파일 위치에서 실행
try:
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
except:
    pass

now = datetime.now()

wheremidi = filedialog.askopenfilename(initialdir="./midi/")
#print("악보 파일 경로: "+wheremidi)
filename=(wheremidi.split("/")[-1]).split(".")[0]

midi = mido.MidiFile(wheremidi, clip=True)
songlen= midi.length

models=[]
wheremodel="./inst/"
for item in os.listdir(wheremodel):
    full_path = os.path.join(wheremodel, item)
    if os.path.isdir(full_path):
        models.append(item)

for i,n in enumerate(models):
    print(f"{i+1}: {n}")

instmodel=models[int(input("폴더를 선택하세요 / Select a folder : "))-1]

wherecode="./inst/"+instmodel+"/"

whereimg = wherecode+"back.png"
base = moviepy.ImageClip(whereimg, duration=songlen)

nowtime=0
nowline=1

log={}
cache={}
audio=[]
video=[base]
octav=1
lastprint=-1

for n in midi.play():
    if n.is_meta:
        continue
    nowtime+=n.time

    if n.type=="note_on" and n.velocity>0:
        nownote=int(n.note+octav*12)

        log[nownote]=nowtime

    elif n.type=="note_off" or (n.type=="note_on" and n.velocity==0):
        nownote=int(n.note+octav*12)

        if nownote>119 or nownote<36:
            print(f"경고: 범위 벗어남 / 노트:{nownote} 시간:{nowtime} 라인:{nowline}")
            continue
        
        #노트 off가 두번씩 있기도
        if nownote not in log:
            continue

        if nownote in cache:
            overload=cache[nownote]
        else:
            overload=moviepy.VideoFileClip(f"{wherecode}{nownote}.mp4")
            cache[nownote]=overload

        over=overload.copy()

        over=over.resized((100, 100))
        starttime=log[nownote]

        #임시
        if nowtime-starttime>over.duration:
            howlong=over.duration
        else:
            howlong=nowtime-starttime

        #over = over.with_effects([moviepy.vfx.Loop(duration=500)])

        over=over.subclipped(0, howlong).with_start(starttime).with_end(nowtime)
        x=((int(nownote)-36)%12)*100
        y=((int(nownote)-36)//12)*100
        over=over.with_position((x, y))

        #audio.append(over.audio.with_start(starttime))
        audio.append(over.audio.with_duration(howlong).with_start(starttime))

        video.append(over)
        log.pop(nownote)
        if nowtime//10 != lastprint:
            print(f"{nowtime:.1f}/{songlen:.1f}", end=" ")
            print(n)
            lastprint=nowtime//10
    nowline+=1


#아웃풋 폴더 없으면 생성
if not os.path.exists(f"./output/{instmodel}"):
    os.makedirs(f"./output/{instmodel}")

fin=moviepy.CompositeVideoClip(video, use_bgclip=True)
yymmddhhmmss=now.strftime("%y%m%d%H%M%S")
audio = moviepy.CompositeAudioClip(audio)
fin = fin.with_audio(audio)
#NVIDIA fin.write_videofile(f"./output/{instmodel}/{yymmddhhmmss} {filename} {instmodel} {octav}.mp4", codec="libx264", preset="ultrafast", fps=24, audio_codec="aac", threads=8)
#codec="libx264", preset="ultrafast"
#codec="h264_nvenc", preset="fast"

print("완료되었습니다 / Completed ")