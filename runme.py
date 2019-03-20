import robot

# Read input from txt file
file = open('testdata.txt', 'r')
input = file.read() 

# process input and print result
for line in robot.process_input(input):
    print line

