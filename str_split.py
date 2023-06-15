handle = open('./tag1.txt', 'r')
r = handle.read();
print(set(r.splitlines()))