# funcToWav
## Usage
`python main.py fileName function sampleRate duration` 
The function should take a variable t, which is entered in seconds.
If the function contains spaces or any control characters, it is advised to enclose it with quotes, see example. 

## example
`python main.py example_out.txt "sin(440 * 2 * pi * t) 50000 10"`
This creates 10 seconds of pure c4.

## available functions
Anything available in python without imports is availale for the function, plus the trigonometric functions and their inverses,  pi and log.
If you want to add more, simply edit the file to import them.
I know this is hacky, but it's by far simpler than any comparable solution.


## Scaling
The output is automatically scaled so the highest value is 1, and the lowest is -1.
