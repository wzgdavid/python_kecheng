s = 'aabb aabb ab ab '.replace('ab', 'AB')
print(s)

import re
a = re.sub([r'one', r'four'], '-', 'one1two2three3four4')

print(a)