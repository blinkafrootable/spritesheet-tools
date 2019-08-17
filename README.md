# spritesheet-tools
A combination of useful programs used to make and modify spritesheets.

## Spritesheet Builder
The spritesheet builder takes a directory of images (.jpg or .png) and compiles them into a single spritesheet. All the images in the directory must be the same dimentions and should be sorted alphanumerically.

The program is run in the command line with the following usage:
```
python builder.py -i <inputdirectory> -o <outputfile>
```
![Spritesheet Builder Demonstration](https://github.com/blinkafrootable/spritesheet-tools/blob/master/resources/spritesheet-builder.png?raw=true "Spritesheet Builder Demonstration")

## Spritesheet Deconstructor
The spritesheet deconstructor takes an existing spritesheet and breaks it down into multiple, seperate images.

The program is run in the command line with the following usage:
```
python deconstructor.py -i <inputfile> -o <outputdirectory>
```
![Spritesheet Deconstructor Demonstration](https://github.com/blinkafrootable/spritesheet-tools/blob/master/resources/spritesheet-deconstructor.png?raw=true "Spritesheet Deconstructor Demonstration")

## Spritesheet Padder
The spritesheet padder takes an existing spritesheet (.png only) and adds padding around each sprite in the spritesheet. The number of pixels for padding is determined by the user when the program is run.

The program is run in the command line with the following usage:
```
python padder.py -i <inputfile> -o <outputfile>
```
![Spritesheet Padder Demonstration](https://github.com/blinkafrootable/spritesheet-tools/blob/master/resources/spritesheet-padder.png?raw=true "Spritesheet Padder Demonstration")

## Spritesheet Flipper
The spritesheet flipper takes an existing sphritesheet (.png only) and horizontally flips (left-right) each sprite in the spritesheet.

The program is run in the command line with the following usage:
```
python flipper.py -i <inputfile> -o <outputfile>
```
![Spritesheet Flipper Demonstration](https://github.com/blinkafrootable/spritesheet-tools/blob/master/resources/spritesheet-flipper.png?raw=true "Spritesheet Flipper Demonstration")
