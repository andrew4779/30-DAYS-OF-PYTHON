import re

txt = "I love to teach Python and Javascript"

match = re.match ("I love to teach", txt, re.I)
print(match)

span = match.span()
print(span)


