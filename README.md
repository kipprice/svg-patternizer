# SVG Patternizer

This is a basic tool to transform a SVG file into a pattern for another SVG.

## Running the script

1. `cd python`
1. `python3 patternize.py [FILE_PATH] [WIDTH] [HEIGHT] [# of REPEATS]`

Where...

`[FILE_PATH]` := The path to the file you want to transform into a pattern

`[WIDTH]` := The width of the rectangle that should be generated with this pattern

`[HEIGHT]` := The height of the rectangle that should be henerated with this pattern

`[\# OF REPEATS]` := How many times the pattern should repeat at the smallest point of the rectangle

### Runnable Example

`python3 patternize.py pattern.svg 1000 500 8` will generate a file called patternized_pattern.svg with a rectangle of dimensions 1000 x 500. 8 copies of the pattern will be rendered vertically. Open with a SVG viewer or web browser to see what it looks like.
