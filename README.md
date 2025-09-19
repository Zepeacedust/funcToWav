# funcToWav
## Usage
`python main.py fileName function sampleRate duration` 
The function should take a variable t, which is entered in seconds.
If the function contains spaces or any control characters, it is advised to enclose it with quotes, see example. 

## Example
`python main.py output.wav "sin(440 * 2 * pi * t)" 44100 10`
This creates 10 seconds of a pure A4 (440 Hz) tone, and writes it to the file `output.wav`.

## Available functions
Anything available in python without imports is availale for the function, plus the trigonometric functions, their inverses,  exp, log, and the constants `pi` and `e`. If you want to add more, simply edit the file to import them. I know this is hacky, but it's by far simpler than any comparable solution.

## Scaling
The output is automatically scaled so the highest value is 1, and the lowest is -1.
