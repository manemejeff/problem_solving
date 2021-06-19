
new = True
old = False

d = dict(zip('abc', range(1, 4)))

text = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor'

if old:
    counts = dict()
    for c in text:
        counts[c] = counts.get(c, 0) + 1
    print(counts)

if old:
    counts = dict()
    for c in text:
        key = c.lower().strip()
        if key:
            counts[key] = counts.get(key, 0) + 1
    print(counts)

if new:
    d = dict.fromkeys('abcd', 0)