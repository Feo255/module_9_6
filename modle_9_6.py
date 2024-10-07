


def all_variants(text):
    n = len(text)
    for l in range(1, n+1):
        for k in range(n -l + 1):
            yield text[k:k + l]




a = all_variants("abc")
for i in a:
    print(i)
