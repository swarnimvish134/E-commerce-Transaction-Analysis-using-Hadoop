#!/usr/bin/env python
import sys
current_product = None
total = 0
for line in sys.stdin:
    Line=line.strip()
    product, revenue = line.strip().split('\t')
    revenue = float(revenue)
    if current_product == product:
        total += revenue
    else:
        if current_product:
            print “{0}\t{1}”.format(current_product,total)
        current_product = product
        total = revenue
if current_product:
    print “{0}\t{1}”.format(current_product,total)
