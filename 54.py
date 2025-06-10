N = int(input())
uniq_languages = set()
all_languages = {}
for _ in range(N):
    M = int(input())
    for _ in range(M):
        language = input()
        uniq_languages.add(language)
        all_languages[language] = all_languages.get(language, 0) + 1

all_known_languages = []
for i in all_languages:
    if all_languages[i] == N:
        all_known_languages.append(i)


print(len(all_known_languages), *all_known_languages, sep='\n')
print(len(uniq_languages), *uniq_languages, sep='\n')
