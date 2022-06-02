import re
price = "2.50 f"

match = re.match(r"([a-z]+)([ - ]+)([0-9]+)", 'foofo 0', re.I)
if match:
    items = match.groups()
    print(items)

match = re.match(r"(\d+)(''+)([a-z]+)", price, re.I)
if match:
    items = match.groups()
    separated_price = [items]
    print(separated_price)