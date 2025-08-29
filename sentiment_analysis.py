from pydub import  AudioSegment

audio = AudioSegment.from_file('test_audio.wav')
cut_audio = audio[10000:30000]
cut_audio.export('cut_audio.mp3', format="mp3")

fadein = cut_audio.fade_in(5000)
fadein.export('fade_in.ogg', format="ogg")

fadeout = cut_audio.fade_out(5000)
fadeout.export('fade_out.ogg', format="ogg")

total = fadein + fadeout
total.export('total.wav', format="wav")

total = total - 30
total.export('total1.wav', format="wav")

ten_seconds = 10 * 1000
first_10_seconds = audio[:ten_seconds]
first_10_seconds.export('first.wav', format="wav")

last_5_seconds = audio[-5000:]
last_5_seconds.export('last.wav', format="wav")

end = last_5_seconds - 3
end.export('end.wav', format="wav")

beginning = first_10_seconds + 6
beginning.export('begin.wav', format="wav")

backwards = audio.reverse()
backwards.export('back.wav', format="wav")

with_style = beginning.append(end, crossfade=1500)
with_style.export('style.wav', format="wav")
