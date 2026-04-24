#!/usr/bin/env python
import sys

for line in sys.stdin:
    data = line.strip().split(',')
    if len(data) == 6 and data[0] != "OrderID":
        product = data[1]
        price = float(data[3])
        quantity = int(data[4])
        revenue = price * quantity
        print "{0}\t{1}".format(product, revenue)
