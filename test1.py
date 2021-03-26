import re

with open('output的副本.txt', 'r') as f:
    read = f.read()
    lines = f.readlines()
    print(len(lines))
    tally = re.findall(r' {8}\d*- {7}\*F8:p \(3<3\[\d+:\d+ \d+:\d+ \d+:\d+', read)
    print(tally)
    listing = re.findall(r'\d+', str(tally))
    print(listing)
    a = listing[4]
    b = listing[6]
    print(a, b)
    txt = ' cell \(3<3\[' + str(a) + ' ' + str(b) + ' ' + '.*'
    print(txt)
with open('output的副本.txt', 'r') as g:
    txt = ' cell \(3<3\[' + str(a) + ' ' + str(b) + ' ' + '.*'
    pattern = re.compile(txt)
    lines = g.readlines()
    print(len(lines))
    for i, line in enumerate(lines):
        if re.search(pattern, line):
            t = lines[i + 1]
            print(t)
        else:
            pass
    a = re.findall(r'\d+.\d+E-\d+', t)
    print(a[0])

