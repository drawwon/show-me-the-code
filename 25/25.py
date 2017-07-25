#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/25 9:01

import webbrowser
from array import array
from sys import byteorder
from struct import pack
import pyaudio,wave
from aip import AipSpeech

APP_ID = '9928498'
API_KEY = 'QqDg2SGwVREghceMyAcs0czT'
SECRET_KEY = '2QGx38tHMPwwGfGucjsEz0KIGtODv728'
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

THRESHOLD = 500
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
RATE = 16000


def open_url(web_text):
    webbrowser.open_new_tab(web_text)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def speech_to_text():
    path = './demo.wav'
    record_to_file(path)
    url_text = aipSpeech.asr(get_file_content('path'), 'pcm', 16000, {
        'lan': 'zh',})
    print url_text
    # record_to_file(path)
    # wf = wave.open(path)
    # params = wf.getparams()
    # nchannels, sampwidth, framerate, nframes = params[:4]
    # data = wf.readframes(nframes)
    # r = sr.Recognizer()

    # open_url(web_text)

def is_silent(snd_data):
    return max(snd_data) < THRESHOLD

def trim(snd_data):
    def _trim(snd_data):
        snd_started = False
        r = array('h')
        for i in snd_data:
            if not snd_started and abs(i)>THRESHOLD:
                snd_started = True
                r.append(i)
            elif snd_started:
                r.append(i)
        return r
    snd_data = _trim(snd_data)
    snd_data.reverse()
    snd_data = _trim(snd_data)
    snd_data.reverse()
    return snd_data

def record():
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate = RATE, input=True, output=True,frames_per_buffer=CHUNK_SIZE)
    num_silent = 0
    snd_started = False
    r = array('h')

    while 1:
        snd_data = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            snd_data.byteswap()
        r.extend(snd_data)

        silent = is_silent(snd_data)
        if silent and snd_started:
            num_silent += 1
        elif not silent and not snd_started:
            snd_started = True

        if snd_started and num_silent>30:
            break
    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()
    r = trim(r)
    return sample_width, r

def record_to_file(path):
    sample_width, data = record()
    data = pack('<'+('h'*len(data)), *data)
    wf = wave.open(path,'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()
