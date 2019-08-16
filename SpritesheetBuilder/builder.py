
from PIL import Image
import glob, math
import os, sys, getopt

def command_line_help():
    print('usage: builder.py -i <inputdirectory> -o <outputfile>')
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
            print('usage: builder.py -i <inputdirectory> -o <outputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"):
            input_path = arg
        elif opt in ("-o", "--ofile"):
            output_path = arg
    
    if os.path.isdir(input_path) == False:
        print('[ERROR] The entered input directory path is invalid: "' + input_path + '"')
        sys.exit(1)

    if output_path.endswith('.png') == False:
        print('[ERROR] The output file must end in .png')
        sys.exit(1)

    input_sprites = glob.glob(input_path + '/*')
    for path in input_sprites:
        if path.lower().endswith('.png') == False and path.lower().endswith('.jpg') == False:
            input_sprites.remove(path)
    try:
        sample_sprite = Image.open(input_sprites[0])
    except:
        print('[ERROR] There was an error accessing any images from the input directory "' + input_path + '". Make sure that the directory is not administrator only or being used by another program and that it actually contains images')
        sys.exit(1)

    sprite_size = sample_sprite.size
    for path in input_sprites:
        if Image.open(path).size != sprite_size:
            print('[ERROR] Not all the input images are the same size. Make sure they are all the same size before running')
            sys.exit(1)
    sprite_width, sprite_height = sample_sprite.size
    sprite_count = len(input_sprites)
    horizontal_frequency = sprite_height/sprite_height
    vertical_frequency = sprite_width/sprite_height
    root = math.ceil(sprite_count**.5)
    horizontal_count = math.ceil(root * horizontal_frequency)
    vertical_count = math.ceil(root * vertical_frequency)

    output_image_width = horizontal_count * sprite_width
    output_image_height = vertical_count * sprite_height

    # print('sprite_count: ' + str(sprite_count) + ', horizontal_count: ' + str(horizontal_count) + ', vertical_count: ' + str(vertical_count) + ', horizontal_frequency: ' + str(horizontal_frequency) + ', vertical_frequency: ' + str(vertical_frequency))

    output_image = Image.new('RGBA', (output_image_width, output_image_height), color=(0, 0, 0, 0))
    for r in range(vertical_count):
        for c in range(horizontal_count):
            index = r * horizontal_count + c
            if index < sprite_count:
                try:
                    output_image.paste(Image.open(input_sprites[index]), (c * sprite_width, r * sprite_height))
                except:
                    print('[ERROR] An error occurred trying to accesss "' + input_sprites[index] + '". Make sure that the file is not being used by another program and that its directory is not administrator only')
                    sys.exit(1)

    try:
        output_image.save(output_path)
    except:
        print('[ERROR] An error occurred trying to save "' + output_path + '". Make sure that the directory that the file is in is not being used by another program and that it is not administrator only')
        sys.exit(1)
    print('DONE')

if __name__ == "__main__":
   main(sys.argv[1:])