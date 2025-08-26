from pydub import AudioSegment,utils,silence,generators

audio=AudioSegment.from_file('test_audio.wav')

slice_audio=audio[0:10000]

slice_audio.export('sliced_audio.mp3', format='mp3')

fade_in_audio=audio.fade_in(15000)
fade_in_audio.export('fade_in_audio.ogg', format ='ogg')

fade_out_audio=audio.fade_out(15000)
fade_out_audio.export('fade_out_audio.ogg', format ='ogg')

high_au=audio + 30
low_au=audio - 20
high_au.export('high_au.mp3', format='mp3')
low_au.export('low_au.mp3', format='mp3')

audio=audio.set_frame_rate(24000)
audio.export()
