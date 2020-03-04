# See how short you can make the script. I could make this one line long.

# Challenge accepted

from sys import argv
script, from_file, to_file = argv

# opening files and copying in one line
open(to_file, 'w').write(open(from_file).read())
