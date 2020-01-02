'''
BFZip v1.0
Compatable with Python 2.7

Phillip Kittelson
@gaterunner341
Provided for educational and training purposes only

Wish list for future functionality:
- Work fully in Python 3
- Check if provided dictionary and zip files are valid
'''

import argparse
import zipfile
import sys

# Declare arguments
parser = argparse.ArgumentParser()
parser.add_argument('-d','--dictionary', required=True, help='Dictionary file to be used')
parser.add_argument('-z','--zip', required=True, help='Zip file to be brute forced')
parser.add_argument('-v','--verbose', help='Allows progress messages to be displayed', action='store_true')
args = parser.parse_args()

# Declare zip file
zFile = zipfile.ZipFile(args.zip)

# Open password dictionary file
passFile = open(args.dictionary)

if args.verbose: # verbose argument
    print('\nBFZip v1.0')
    print('Using dictionary: ' + args.dictionary + '\n')
    print('Attempting to brute force ' + args.zip)
    # Iterate through dictioary file and brute force against zip file
    for line in passFile.readlines():
        password = line.strip('\n')
        try:
            print('Using password: ' + password)
            zFile.extractall(pwd=password)
            print('Password "' + password + '" sucessfull, unzipping file...')
            # If zFile.extractall is sucessfull
            sys.exit(0)
        except SystemExit:
            # Breaks out of for loop with message
            print('\nComplete')
            break
        except:
            # Allows for loop to continue until brute force sucessfull
            print('Password unsucessful\n')
            pass
else:
    print('\nBFZip v1.0')
    for line in passFile.readlines():
        password = line.strip('\n')
        try:
            zFile.extractall(pwd=password)
            print('Brute force sucessfull, unzipping file...')
            sys.exit(0)
        except SystemExit:
            print('\nComplete')
            break
        except:
            pass