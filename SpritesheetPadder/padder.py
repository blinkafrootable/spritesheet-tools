
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
    print('usage: padder.py -i <inputfile> -o <outputfile>')
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
            print('usage: padder.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_path = arg
        elif opt in ("-o", "--ofile"):
            output_path = arg
    
    if os.path.isfile(input_path) == False:
        print('[ERROR] The entered input file path is invalid: "' + input_path + '"')
        sys.exit(1)

    if output_path.endswith('.png') == False:
        print('[ERROR] The output file must end in .png.')
        sys.exit(1)
    
    try:
        input_image = Image.open(input_path)
    except:
        print('[ERROR] There was an error accessing the image "' + input_path + '". Make sure that the file is not being used by another program and that its directory is not administrator only')
        sys.exit(1)
    input_image_width = input_image.size[0]
    input_image_height = input_image.size[1]

    input_width = ''
    while True:
        input_width = input('Enter the width (in pixels) of each sprite in the spritesheet (has to be a positive integer): ')
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
        input_height = input('Enter the height (in pixels) of each sprite in the spritesheet (has to be a positive integer): ')
        if is_valid_number(input_height) == False:
            print('[ERROR] The input height is not a positive integer...')
            continue
        elif input_image_height % int(input_height) != 0:
            print('[ERROR] The input image\'s height is not divisible by the input height...')
            continue
        else:
            break
    input_height = int(input_height)

    padding = ''
    while True:
        padding = input('Enter the number of pixels of padding to put around each sprite (has to be a positive integer): ')
        if is_valid_number(padding) == False:
            print('[ERROR] The input padding is not a positive integer...')
        else:
            break
    padding = int(padding)

    columns = int(input_image_width/input_width)
    rows = int(input_image_height/input_height)

    output_width = input_width + padding*2
    output_height = input_height + padding*2
    output_image_width = output_width * columns
    output_image_height = output_height * rows

    # print('Output Image Width: ' + str(output_image_width) + ', Output Image Height: ' + str(output_image_height))

    output_image = Image.new('RGBA', (output_image_width, output_image_height), color=(0, 0, 0, 0))
    for r in range(rows):
        for c in range(columns):
            input_point = (input_width * c, input_height * r)
            output_point = (output_width * c, output_height * r)
            crop_info = (input_point[0], input_point[1], input_point[0]+input_width, input_point[1]+input_height)
            input_sprite = input_image.crop(crop_info)
            padded_input_sprite = Image.new('RGBA', (input_sprite.size[0]+2, input_sprite.size[1]+2), color=(0, 0, 0, 0))
            padded_input_sprite.paste(input_sprite, (1, 1))
            pixels = padded_input_sprite.load()
            for pr in range(padded_input_sprite.size[1]):
                for pc in range(padded_input_sprite.size[0]):
                    is_border_pixel = False
                    reference_pixel = [pc, pr]
                    if pr == 0:
                        reference_pixel[1] += 1
                        is_border_pixel = True
                    if pc == 0:
                        reference_pixel[0] += 1
                        is_border_pixel = True
                    if pr == padded_input_sprite.size[1]-1:
                        reference_pixel[1] -= 1
                        is_border_pixel = True
                    if pc == padded_input_sprite.size[0]-1:
                        reference_pixel[0] -= 1
                        is_border_pixel = True
                    if is_border_pixel == True:
                        pixels[pc, pr] = pixels[reference_pixel[0], reference_pixel[1]]
            output_image.paste(padded_input_sprite, output_point)

    try:
        output_image.save(output_path)
    except:
        print('[ERROR] An error occurred trying to save "' + output_path + '". Make sure that the directory that the file is in is not being used by another program and that it is not administrator only')
        sys.exit(1)
    print('DONE')

if __name__ == "__main__":
   main(sys.argv[1:])