import sys
from xml.dom import minidom

""" read_file opens the specified SVG and reads it in as lines """
def read_file(file_path):
    f = open(file_path, "r")
    file_contents = f.readlines()
    return file_contents

""" parse_out_dimensions tracks what dimensions a SVG path already has """
def parse_out_dimensions(file_path):
    doc = minidom.parse(file_path)
    viewBox = [svg.getAttribute('viewBox') for svg in doc.getElementsByTagName('svg')]
    return viewBox[0]

""" patternize generates the extra pieces that allow this to take a different size """
def patternize(contents, orig_view_box, dimX, dimY, pattern_size=25):

    min_dim = min(dimX, dimY)
    pattern_x = pattern_size / (dimX / min_dim)
    pattern_y = pattern_size / (dimY / min_dim)

    contents.insert(0, f'<svg width="{dimX}" height="{dimY}" viewBox="0 0 {dimX} {dimY}" xmlns="http://www.w3.org/2000/svg">\n')
    contents.insert(1, f'<defs>\n<pattern id="pattern" width="{pattern_x}%" height="{pattern_y}%" viewBox="{orig_view_box}">\n')
    contents.append("</pattern>\n</defs>\n")
    contents.append(f'<rect x="0" y="0" width="{dimX}" height="{dimY}" fill="url(#pattern)" />\n')
    contents.append('</svg>')
    return contents

""" gen_file creates a patternized version of the SVG """
def gen_file(file_path, contents):
    f = open(f'patternized_{file_path}', "w");
    f.writelines(contents);

""" print_help shows details if the user runs the program in help mode """
def print_help():
    print("  ")
    print("Welcome to the SVG Patternizer! This takes 4 arguments:")
    print("  1. The path to the file that should become the pattern (string)")
    print("  2. The width of the shape you'll be filling (number)")
    print("  3. The height of the shape you'll be filling (number)")
    print("  4. The number of times the pattern should repeat at its smallest point (number)")
    print("  ")
    print("As an example, calling this as:")
    print(" > python3 patternize.py pattern.svg 100 100 25")
    print("will generate a file called 'patternized_pattern.svg' that has a 100x100 rectangle patterned with the provided SVG at 25% scale.")
    print("  ")

def main():
    args = sys.argv
    if len(args) < 2:
        print("Please specify the file to patternize")
        return

    # handle the help case
    if args[1] == "--help" or args[1] == "-h":
        print_help()
        return

    # grab the arguments
    file_path = args[1]
    dim_x = 100 if len(args) <= 2 else int(args[2])
    dim_y = 100 if len(args) <= 3 else int(args[3])
    pattern_repeat = 4 if len(args) <= 4 else int(args[4])

    # read in the file
    fc = read_file(file_path)
    
    # add to the real content
    contents = []
    for line in fc:
        if "svg" not in line:
            contents.append(line)
    
    # generate the new patternized version
    orig_view_box = parse_out_dimensions(args[1])
    contents = patternize(contents, orig_view_box, dim_x, dim_y, 100 / pattern_repeat)

    # create the new file
    gen_file(args[1], contents)

main()
