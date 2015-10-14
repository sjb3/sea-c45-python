""" analysis_Dna

& Name: Justin Byun
& SEA-C45:
& HW 8: DNA Counting

"""

import sys

if len(sys.argv) < 2:
    print("You must supply a file name as an argument when running this program.")
    
    sys.exit(2)

filename = sys.argv[1]
inputfile = open(filename)
seq = ""
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    
    if linenum % 4 == 2:
        line = line.rstrip()
        seq = seq + line


total_count = 0
g_count = 0
c_count = 0
a_count = 0
t_count = 0

gc_count = 0
at_count = 0

for bp in seq:
    total_count = total_count + 1

    if bp == 'C':
        c_count = c_count + 1
        
    if bp == 'G':
        g_count = g_count + 1



gc_count = gc_count + 1
gc_count = g_count + c_count

gc_content = float((gc_count) / total_count)

print('GC-content:', gc_content)
print ('G content', g_count)
print ('C content', c_count)

for bp in seq:
    total_count = total_count + 1

    if bp == 'A':
        a_count = a_count + 1

    if bp == 'T':
        t_count = t_count + 1
        

at_count = a_count + t_count
at_content = float((at_count) / total_count)

# Print the answer
print('AT-content:', at_content)
print('A content', a_count)
print('T content', t_count)

total_countVariables = g_count + c_count + a_count + t_count

print ('Total count variables=', total_countVariables)

print ("The length of the seq variables=", len(seq))
print ('AT/GC ratio', at_count / gc_count)

