


dir = r"C:\Users\Administrator\Documents\webrtc\webrtc\webrtc-checkout\src\third_party\ffmpeg\libavcodec"



import os
lis = os.listdir(dir)

for i in lis:
    if 'hevc' in i:
        print(f'"libavcodec/{i}",')