import soundfile as wav

data, samplerate = wav.read("./test.wav")

print(data)
print(samplerate)

info = wav.info("./test.wav")

