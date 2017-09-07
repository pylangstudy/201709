import collections

cnt = collections.Counter()
for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print(cnt)

import re
words = re.findall(r'\w+', 'my name is is ann.')
print(collections.Counter(words).most_common(10))
