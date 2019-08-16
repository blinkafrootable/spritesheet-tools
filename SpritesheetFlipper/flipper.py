
import PIL
from PIL import Image
import os, sys, getopt

def is_valid_number(string):
    try:
        if int(string) > 0:
            return True
        else:
            return False
    except ValueError:
        return False

def command_line_help():
    print('usage: flipper.py -i <inputfile> -o <outputfile>')
    sys.exit(2)

def main(argv):

    input_path = ''
    output_path = ''

    if ('-i' not in argv or '-o' not in argv) and '-h' not in argv:
        command_line_help()

    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        command_line_help()
    for opt, arg in opts:
        if opt == '-h':
            print('usage: flipper.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_path = arg
        elif opt in ("-o", "--ofile"):
            output_path = arg
    
    if os.path.isfile(input_path) == False:
        print('The entered input file path is invalid: "' + input_path + '"')
        sys.exit(1)

    input_image = Image.open(input_path)
    input_image_width, input_image_height = input_image.size

    input_width = ''
    while True:
        input_width = input('Enter the width (in pixels) of each sprite in the spritesheet (has to be a positive integer). Make sure to include the padding width if there is padding: ')
        if is_valid_number(input_width) == False:
            print('The input width is not a positive integer...')
            continue
        elif input_image_width % int(input_width) != 0:
            print('The input image is not divisible by the input width...')
            continue
        else:
            break
    input_width = int(input_width)

    input_height = ''
    while True:
        input_height = input('Enter the height (in pixels) of each sprite in the spritesheet (has to be a positive integer). Make sure to include the padding height if there is padding: ')
        if is_valid_number(input_height) == False:
            print('The input height is not a positive integer...')
            continue
        elif input_image_height % int(input_height) != 0:
            print('The input image is not divisible by the input height...')
            continue
        else:
            break
    input_height = int(input_height)

    columns = int(input_image_width/input_width)
    rows = int(input_image_height/input_height)

    output_image = Image.new('RGBA', (input_image_width, input_image_height), color=(0, 0, 0, 0))
    for r in range(rows):
        for c in range(columns):
            pos = (c * input_width, r * input_height)
            current_sprite = input_image.crop((pos[0], pos[1], pos[0]+input_width, pos[1]+input_height))
            current_sprite = current_sprite.transpose(PIL.Image.FLIP_LEFT_RIGHT)
            output_image.paste(current_sprite, pos)

    output_image.save(output_path)
    print('DONE')

if __name__ == "__main__":
   main(sys.argv[1:])