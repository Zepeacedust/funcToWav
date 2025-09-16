import sys
import math
import wave
import random

from math import sin, cos, log, tan, atan, acos, asin, pi, e

SAMPLE_WIDTH = 4 # only 1 works right now, not quite sure why

# Go from list of numbers, to list of integers that can be interpreted as bytearray
def prepareForWriting(points):
    points = list(points)
    minimum = min(points)
    maximum = max(points)
    for point in points:
        intermediate = ((point-minimum)/(maximum-minimum)-0.5) * (256**SAMPLE_WIDTH-1)
        for inner in int(intermediate).to_bytes(SAMPLE_WIDTH, byteorder="little", signed=True):
            yield inner

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
