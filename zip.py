import shutil
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('output_filename')
parser.add_argument('folder')

args = parser.parse_args()

output_filename = args.output_filename.replace('.zip', '') # .zip will be automatically append, no need to add it
shutil.make_archive(output_filename, 'zip', args.folder)
