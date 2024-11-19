import time
import pvporcupine
from pvrecorder import PvRecorder
from playsound import playsound
import pvrhino
import subprocess
import random
from datetime import datetime
from suntime import Sun, SunTimeException

import config
import my_spotify
import battery_report


def play_response(sound: str):
    if sound == 'evening' or sound == 'morning' or sound == 'afternoon':
        playsound(
            r'D:\Joi - project\Joi_sounds\Millie\day_greetings\{}{}.wav'.format(sound, random.randrange(0, 1))
        )
    elif sound == 'greet':
        playsound(
            r'D:\Joi - project\Joi_sounds\Millie\greetings\{}{}.wav'.format(sound, random.randrange(0, 4))
        )
    elif sound == 'done':
        playsound(
            r'D:\Joi - project\Joi_sounds\Millie\done\{}{}.wav'.format(sound, random.randrange(0, 4))
        )
    elif sound == 'battery_report':
        playsound(
            r'D:\Joi - project\Joi_sounds\Millie\battery_report\emergency power.wav'
        )
    elif sound == 'change_voice':   # going to come back to this
        pass
    # testing should change it
    elif sound == 'problem':
        playsound(
            r'D:\Joi - project\Joi_sounds\Millie\oops could not found it.wav'
        )


def commands(command_intent: str, command: dict):
    if command_intent == 'open_app':
        play_response('done')
        subprocess.Popen(r'D:\Joi - project\ahk_commands\{}.exe'.format(command['app_name']))
    elif command_intent == 'song_control':
        if 'status' in command:
            if my_spotify.play_and_pause():
                play_response('done')
            else:
                play_response('problem')
        elif 'volume_percent' in command:
            play_response('done')
            my_spotify.set_volume(
                int(command['volume_percent'][:-1])
            )
        elif 'command' in command:
            play_response('done')
            my_spotify.track_control(command['command'])


# # not sure to use
# def record_call_back(indata, frames, time, status):
#     if status:
#         print(status, file=sys.stderr)
#     q.put(bytes(indata))

porcupine = pvporcupine.create(
    access_key=config.ACCESS_KEY,
    keyword_paths=[
        r'D:\Joi - project\Wake commands\Listen-Joi_en_windows_v2_2_0.ppn',
        r'D:\Joi - project\Wake commands\Ok-Joi_en_windows_v2_2_0.ppn'
    ]
)

recorder = PvRecorder(
    device_index=config.MICROPHONE_INDEX,
    frame_length=porcupine.frame_length
)
print(PvRecorder.get_audio_devices())

rhino = pvrhino.create(
    access_key=config.ACCESS_KEY,
    context_path=r'D:\Joi - project\opening_commands\joi_commands_rhino_en_windows_v2_2_0.rhn'
)

time_now = 0

# time vars
current_time = datetime.now().strftime('%H')

latitude = 40.390060
longitude = 71.790321

try:
    sun = Sun(latitude, longitude)
    today_sunset = sun.get_local_sunset_time().strftime('%H')
    today_sunrise = sun.get_local_sunrise_time().strftime('%H')
except SunTimeException:
    today_sunset = '19'
    today_sunrise = '6'
    SunTimeException('Could not get the sun times')

if int(today_sunrise) <= int(current_time) <= 12:
    play_response('morning')
elif 12 <= int(current_time) <= int(today_sunset):
    play_response('afternoon')
else:
    play_response('evening')

try:
    recorder.start()
    print('Starting test')
    while True:
        pcm = recorder.read()
        keyword_index = porcupine.process(pcm)

        if keyword_index >= 0:
            print(f'Detected {config.KEYWORDS[keyword_index]}')
            play_response('greet')
            time_now = time.time()

        while time.time() - time_now <= 10:
            pcm = recorder.read()
            is_finalized = rhino.process(pcm)

            if is_finalized:
                inference = rhino.get_inference()
                # print('inference', inference)
                if inference.is_understood:
                    intent = inference.intent
                    slots = inference.slots
                    time_now = time.time()
                    print('intent', intent, 'slot', slots)
                    commands(intent, slots)

except KeyboardInterrupt:
    recorder.stop()
finally:
    porcupine.delete()
    recorder.delete()
