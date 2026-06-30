#word="eat"
#print(sorted(word))
#print(''.join(sorted(word)))
#dictionary={}

word=["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(word):
    groups={}

    for i in word:
        key="".join(sorted(i))

        if key not in groups:
            groups[key]=[]
        groups[key].append(i)

    return list(groups.values())

print(groupAnagrams(word))
