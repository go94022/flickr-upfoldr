import argparse
import os
import sys
import semidbm
import webbrowser

parser = argparse.ArgumentParser(description="Upload a file or folder to Flickr. Folders are uploaded recursively. The parent folder becomes the Album name (aka PhotoSet). The folder path to an image is saved as a tag. The immediate parent of the source is also saved as a tag. Any embedded spaces in a name/path tag are converted to '^'")

parser.add_argument("-p", "--public", action="store_true", help="Uploaded files will be public (default is private)")
parser.add_argument("-t", "--test", action="store_true", help="Does not upload, prints actions that would occur")
parser.add_argument("-d", "--find-duplicates", action="store_true", help="Does not upload, prints list of duplicates")
parser.add_argument("-s", "--space-replace", action="store", metavar="CH", nargs=1, help="Specify a different character to replace spaces than '^'")

parser.add_argument("SRC", nargs="+", help="Folders or files to upload recursively. Use '.' for current directory.")

args = parser.parse_args()

script_dir = os.path.abspath(sys.path[0])
print(sys.path[0])
print(script_dir)
script_path = os.path.abspath(sys.argv[0])
print(sys.argv[0])
print(script_path)

# String is returned unchanged if user home does not exist
user_dir = os.path.expanduser("~")
if user_dir == "~":
	print("User profile not configured, aborting")
	exit(-1)
	
user_path = os.path.abspath(user_dir)
print(user_dir)
print(user_path)

upfoldr_dir = os.path.join(user_path, ".upfoldr")
print(upfoldr_dir)

if not os.path.exists(upfoldr_dir):
	os.mkdir(upfoldr_dir)
elif not os.path.isdir(upfoldr_dir):
	print("Profile path '{0}' already exists as file, not directory".format(upfoldr_dir))
	# TODO: ask if it is OK to remove it.
	exit(-1)
# Otherwise it exists and it is a directory, so OK to put our working data there

upfoldr_stat = os.stat(upfoldr_dir)

sys_os = sys.platform
if sys_os == "win32":
	print("it's Windows")
elif sys_os == "darwin":
	print("it's Mac")
elif sys_os.startswith("linux"):
	print("it's Linux")
else:
	print("Platform '{0}' not supported, continuing anyway".format(sys_os))
