
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

def command_line_help(exit_code):
    print('usage: deconstructor.py -i <inputfile> -o <outputdirectory>')
    sys.exit(exit_code)

def main(argv):

    input_path = ''
    output_path = ''

    if ('-i' not in argv or '-o' not in argv) and '-h' not in argv:
        command_line_help(2)

    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        command_line_help(2)
    for opt, arg in opts:
        if opt == '-h':
            command_line_help(0)
        elif opt in ("-i", "--ifile"):
            input_path = arg
        elif opt in ("-o", "--ofile"):
            output_path = arg
    
    if os.path.isfile(input_path) == False:
        print('[ERROR] The entered input file path does not exist: "' + input_path + '"')
        sys.exit(1)

    if input_path.endswith('.png') == False:
        print('[ERROR] The input file must end in .png')
        sys.exit(1)
    
    if os.path.isdir(output_path) == False:
        print('[ERROR] The entered output directory path does not exist: "' + output_path + '"')
        sys.exit(1)

    try:
        input_image = Image.open(input_path)
    except:
        print('[ERROR] There was an error accessing the image "' + input_path + '". Make sure that the file is not being used by another program and that its directory is not administrator only')
        sys.exit(1)
    input_image_width, input_image_height = input_image.size
    
    input_width = ''
    while True:
        input_width = input('Enter the width (in pixels) of each sprite in the spritesheet (has to be a positive integer). Make sure to include the padding width if there is padding: ')
        if is_valid_number(input_width) == False:
            print('[ERROR] The input width is not a positive integer...')
            continue
        elif input_image_width % int(input_width) != 0:
            print('[ERROR] The input image\'s width is not divisible by the input width...')
            continue
        else:
            break
    input_width = int(input_width)

    input_height = ''
    while True:
        input_height = input('Enter the height (in pixels) of each sprite in the spritesheet (has to be a positive integer). Make sure to include the padding height if there is padding: ')
        if is_valid_number(input_height) == False:
            print('[ERROR] The input height is not a positive integer...')
            continue
        elif input_image_height % int(input_height) != 0:
            print('[ERROR] The input image\'s height is not divisible by the input height...')
            continue
        else:
            break
    input_height = int(input_height)

    columns = int(input_image_width/input_width)
    rows = int(input_image_height/input_height)

    i = 0
    for r in range(rows):
        for c in range(columns):
            pos = (c * input_width, r * input_height)
            current_sprite = input_image.crop((pos[0], pos[1], pos[0]+input_width, pos[1]+input_height))
            pixels = current_sprite.load()
            pixel_color = pixels[0, 0]
            skip = True
            for pr in range(current_sprite.size[1]):
                for pc in range(current_sprite.size[0]):
                    pixel = pixels[pr, pc]
                    if pixel != pixel_color:
                        skip = False
                        break
                if skip == False:
                    break
            if skip == False:
                try:
                    current_sprite.save(output_path + '/' + os.path.basename(input_path).replace('.png', '') + '_' + str(i) + '.png')
                except:
                    print('[ERROR] There was an error trying to save to the output directory ' + output_path + '. Make sure that the directory is not in use by another program and that it is not administrator only')
                    sys.exit(2)
                i += 1
    print('DONE')
        

if __name__ == "__main__":
   main(sys.argv[1:])