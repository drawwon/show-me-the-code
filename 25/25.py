#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/25 9:01

import webbrowser
from array import array
from sys import byteorder
from struct import pack
import pyaudio,wave
from aip import AipSpeech
import json
import re
import speech_recognition as sr
from urllib2 import Request
APP_ID = '9928498'
API_KEY = 'QqDg2SGwVREghceMyAcs0czT'
SECRET_KEY = '2QGx38tHMPwwGfGucjsEz0KIGtODv728'
aipSpeech = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

THRESHOLD = 500
CHUNK_SIZE = 1024
FORMAT = pyaudio.paInt16
RATE = 44100


def open_url(web_text):
    webbrowser.open_new_tab(web_text)

def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()




def speech_to_text():
    path = './demo.wav'
    record_to_file(path)
    # url_text = aipSpeech.asr(get_file_content('baidu.wav'), 'wav', 16000, {
    #     'lan': 'zh',
    # })
    r = sr.Recognizer()
    with sr.WavFile(path) as source:
        audio = r.record(source)
    IBM_USERNAME = '9599bd39-76eb-41cd-ad55-32ce716dddd0'
    IBM_PASSWORD = 'cUqQxW2wXiXM'
    url_text = r.recognize_ibm(audio,
                              language="zh-CN",
                              #show_all="True",
                              username=IBM_USERNAME,
                              password=IBM_PASSWORD)
    print url_text,type(url_text),repr(url_text),len(url_text)
    url_text = u''.join(url_text.split()).encode('utf-8')
    if '百度' in url_text:
        webbrowser.open_new_tab('baidu.com')
    elif '谷歌' in url_text:
        webbrowser.open_new_tab('google.com')
    # record_to_file(path)
    # wf = wave.open(path)
    # params = wf.getparams()
    # nchannels, sampwidth, framerate, nframes = params[:4]
    # data = wf.readframes(nframes)
    # r = sr.Recognizer()

    # open_url(web_text)




def is_silent(snd_data):
    "Returns 'True' if below the 'silent' threshold"
    return max(snd_data) < THRESHOLD

def normalize(snd_data):
    "Average the volume out"
    MAXIMUM = 16384
    times = float(MAXIMUM)/max(abs(i) for i in snd_data)

    r = array('h')
    for i in snd_data:
        r.append(int(i*times))
    return r

def trim(snd_data):
    "Trim the blank spots at the start and end"
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

    # Trim to the left
    snd_data = _trim(snd_data)

    # Trim to the right
    snd_data.reverse()
    snd_data = _trim(snd_data)
    snd_data.reverse()
    return snd_data

def add_silence(snd_data, seconds):
    "Add silence to the start and end of 'snd_data' of length 'seconds' (float)"
    r = array('h', [0 for i in xrange(int(seconds*RATE))])
    r.extend(snd_data)
    r.extend([0 for i in xrange(int(seconds*RATE))])
    return r

def record():
    """
    Record a word or words from the microphone and
    return the data as an array of signed shorts.

    Normalizes the audio, trims silence from the
    start and end, and pads with 0.5 seconds of
    blank sound to make sure VLC et al can play
    it without getting chopped off.
    """
    p = pyaudio.PyAudio()
    stream = p.open(format=FORMAT, channels=1, rate=RATE,
        input=True, output=True,
        frames_per_buffer=CHUNK_SIZE)

    num_silent = 0
    snd_started = False
    # print p.get_device_info_by_index(0)
    r = array('h')

    while 1:
        # little endian, signed short
        snd_data = array('h', stream.read(CHUNK_SIZE))
        if byteorder == 'big':
            snd_data.byteswap()
        r.extend(snd_data)

        silent = is_silent(snd_data)

        if silent and snd_started:
            num_silent += 1
        elif not silent and not snd_started:
            snd_started = True

        if snd_started and num_silent > 30:
            break

    sample_width = p.get_sample_size(FORMAT)
    stream.stop_stream()
    stream.close()
    p.terminate()

    # r = normalize(r)
    # r = trim(r)
    # r = add_silence(r, 0.5)
    return sample_width, r

def record_to_file(path):
    "Records from the microphone and outputs the resulting data to 'path'"
    print 'please say samething:'
    sample_width, data = record()
    # data = pack('<' + ('h'*len(data)), *data)

    wf = wave.open(path, 'wb')
    wf.setnchannels(1)
    wf.setsampwidth(sample_width)
    wf.setframerate(RATE)
    wf.writeframes(data)
    wf.close()

if __name__ == '__main__':
    speech_to_text()