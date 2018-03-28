#!/usr/bin/ python3
# -*- coding: utf-8 -*-

# author:   Michael Kitzan
# date:     March 28, 2018

# i   = index
# el  = list element (non-numerical)
# val = list element (numerical)

# mathematical operations appear with no spaces between the values and the operator 'num1+num2'
# concatenation operations apper with space between the values and the operator     'str1 + str2'


def make_row(values, val_bufs):
    """Creates a row of table output."""
    return "|" + "|".join([str(values[i]) + " "*val_bufs[i] for i in range(len(values))]) + "|"


def buffers(columns, values, padding):
    """Finds the required buffers for each value in the data, and the lengths of the longest values in each column."""
    max_lens = [len(str(el)) for el in columns]
    val_lens = [[val for val in max_lens]]

    # looks at all the data and keeps track of longest values, and value lengths holistically
    for el in values:
        cur_lens = []
        for i in range(len(el)):
            cur_lens.append(len(str(el[i])))
            if cur_lens[i] > max_lens[i]:
                max_lens[i] = cur_lens[i]
        val_lens.append(cur_lens)
    
    # applies padding offset to all max length values
    max_lens = [val+padding for val in max_lens]

    return [[max_lens[i]-el[i] for i in range(len(el))] for el in val_lens], max_lens


def table(columns, values, header=None, transpose=False, edge="*", padding=1, printer=print):
    """Prints a table from the columns and values data."""
    # making sure your inputs are kosher
    transpose = transpose if type(transpose) is bool else False
    header = None if type(header) is not str else header
    edge = edge[0] if (type(edge) is str) and len(edge) > 0 else "*"
    padding = padding if type(padding) is int else 1
    printer = printer if callable(printer) else print
    
    if transpose:
        values = [list(el) for el in zip(*values)]
    
    # finds and defines information used throughout the printing process
    val_bufs, max_lens = buffers(columns, values, padding)
    border = "".join([edge + "-"*val for val in max_lens]) + edge
    
    # core table printing from here out
    if header is not None:
        printer(header)
        
    printer(border + "\n" + make_row(columns, val_bufs[0]) + "\n" + border)

    for i in range(len(values)):
        printer(make_row(values[i], val_bufs[i+1]))

    printer(border)

