python3 <(cat input.txt | sed "s/^\(.*\) inc /memory[\"\1\"] = memory[\"\1\"] + (/" |sed "s/^\(.*\) dec /memory[\"\1\"] = memory[\"\1\"] - (/" | sed "s/if \([^ ]*\)/if memory[\"\1\"]/" | sed "s/$/ else 0)/" | sed "1s/^/class myDict(dict):\n\tdef __missing__(self, key):\n\t\tself[key] = 0\n\t\treturn 0\nmemory = myDict()\n/" | sed '$s/$/\nprint(max([memory[x] for x in memory]))/')

