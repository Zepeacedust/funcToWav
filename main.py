import sys
import math
import wave
import random

from math import sin, cos, log, tan, atan, acos, asin, pi, e

SAMPLE_WIDTH = 1 # only 1 works right now, not quite sure why

# Go from list of numbers, to list of integers that can be interpreted as bytearray
def prepareForWriting(points):
    points = list(points)
    minimum = min(points)
    maximum = max(points)
    for point in points:
        #yield int((point+1)/2*255)
        #continue
        intermediate = (point - minimum)/(maximum-minimum) * 256**SAMPLE_WIDTH
        #print(point, intermediate)
        for i in range(SAMPLE_WIDTH, 0, -1):
            temp = intermediate // (256 ** (i-1))
            print(temp)
            yield int(temp%256)

def writePoints(points, sampleRate, destination):
    file = wave.open(destination, "w")
    file.setnchannels(1)
    file.setsampwidth(SAMPLE_WIDTH)
    file.setframerate(sampleRate)
    file.writeframes(bytearray(prepareForWriting(points)))

def scaledRange(sampleRate, duration):
    stepCount = int(duration * sampleRate)
    return map(lambda x: x / sampleRate, range(stepCount))
    
def generatePoints(func, sampleRate, duration):
    return map(func, scaledRange(sampleRate, duration))

def main(argv, argc):
    if argc != 5: # invocation name, file name function, sampleRate, duration
        print("usage is main file name ")
    fileName = argv[1]
    function = eval("lambda t:" +argv[2]) # Dirty hack, but this is not for use in prod.
    sampleRate = float(argv[3])
    duration = float(argv[4])
    writePoints(generatePoints(function, sampleRate, duration), sampleRate, fileName)


if __name__ == "__main__":
    main(sys.argv, len(sys.argv))
