def make_row(values, val_bufs):
    return "|" + "|".join([str(values[i]) + " " * val_bufs[i] for i in range(len(values))]) + "|"


def buffers(columns, values, buffer):
    max_lens = [len(str(i)) for i in columns]
    val_lens = [[i for i in max_lens]]

    for el in values:
        cur_lens = []
        for i in range(len(el)):
            cur_lens.append(len(str(el[i])))
            if cur_lens[i] > max_lens[i]:
                max_lens[i] = cur_lens[i]
        val_lens.append(cur_lens)

    return [[max_lens[i]+buffer - el[i] for i in range(len(el))] for el in val_lens], [i+buffer for i in max_lens]


def table(columns, values, edge="*", buffer=1, transpose=False, printer=print):
    if transpose:
        values = [list(el) for el in zip(*values)]
    
    val_bufs, max_lens = buffers(columns, values, buffer)
    border = "".join([edge + "-"*i for i in max_lens]) + edge
    
    printer(border + "\n" + make_row(columns, val_bufs[0]) + "\n" + border)

    for i in range(len(values)):
        printer(make_row(values[i], val_bufs[i + 1]))

    printer(border)
