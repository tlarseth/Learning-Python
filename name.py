import sys

# Check for errors
if len(sys.argv) < 3:
    sys.exit("Make sure your using first and last name in command prompt")
elif len(sys.argv) >3:
    sys.exit("Only use first and last name in command prompt")

# Print one nametag
print("Hello, my name is", sys.argv[1], sys.argv[2])

# Print Nametags for each entry
for arg in sys.argv[1:]:
    print("Hello, my name is", arg)