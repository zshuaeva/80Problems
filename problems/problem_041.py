# Complete the add_csv_lines function which accepts a list
# as its only parameter. Each item in the list is a
# comma-separated string of numbers. The function should
# return a new list with each entry being the corresponding
# sum of the numbers in the comma-separated string.
#
# These kinds of strings are called CSV strings, or comma-
# sepearted values strings.
#
# Examples:
#   * input:  []
#     output: []
#   * input:  ["3", "1,9"]
#     output: [3, 10]
#   * input:  ["8,1,7", "10,10,10", "1,2,3"]
#     output:  [16, 30, 6]
#
# Look up the string split function to find out how to
# split a string into pieces.

# Write out your own pseudocode to help guide you.

def add_csv_lines(csv_lines):
    result = []
    for i in csv_lines:
        csv = (i.split(","))    #split string version number
        part_sum = 0            #create sum variable
        for j in csv:           #iterate over the parted string numbers
            number = int(j)     #convert string num to int
            part_sum += number  #incriment sum
        result.append(part_sum) #push sum into result list outside of loop
    return result               #return result

print(add_csv_lines(["3", "1,9"]))
