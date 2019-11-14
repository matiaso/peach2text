import speech_recognition as sr
from os import path
from pydub import AudioSegment
import os, sys, getopt

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print('test.py -i <inputfile> -o <outputfile>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('convert.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            filename = arg
        elif opt in ("-o", "--ofile"):
            outputfile = arg

    sound = AudioSegment.from_ogg(filename)
    sound.export("transcript.wav", format="wav")

    # use the audio file as the audio source
    r = sr.Recognizer()
    f= open(outputfile, "w+")
    with sr.AudioFile("transcript.wav") as source:
        audio = r.record(source)  # read the entire audio file
        f.write(r.recognize_google(audio))
        f.close()
        os.remove("transcript.wav")


if __name__ == "__main__":
    main(sys.argv[1:])
