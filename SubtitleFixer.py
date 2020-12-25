import re

with open("sub.srt", encoding="utf8") as f:
    input = f.read()
    output = re.sub(r'\([^)]*\)', '', input)

f.close()

with open("subfinal.srt", mode='a', encoding="utf8") as fa:
    fa.write(output)
fa.close()

print("OK!")
