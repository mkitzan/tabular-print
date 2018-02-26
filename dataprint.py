def make_row(values, val_bufs):
    return "|" + "|".join([str(values[i]) + " " * val_bufs[i] for i in range(len(values))]) + "|"


def buffers(columns, values, buffer):
    max_lens = [len(str(i)) for i in columns]
    val_lens = [[i for i in max_lens]]

    for i in values:
        cur_lens = []
        for j in range(len(i)):
            cur_lens.append(len(str(i[j])))
            if cur_lens[j] > max_lens[j]:
                max_lens[j] = cur_lens[j]
        val_lens.append(cur_lens)

    return [[max_lens[i]+buffer - el[i] for i in range(len(el))] for el in val_lens], [i+buffer for i in max_lens]


def table(columns, values, edge="*", buffer=1, transpose=False, funct=print):
    if transpose:
        values = [list(el) for el in zip(*values)]
    
    val_bufs, max_lens = buffers(columns, values, buffer)
    border = "".join([edge + "-"*i for i in max_lens]) + edge
    
    funct(border + "\n" + make_row(columns, val_bufs[0]) + "\n" + border)

    for i in range(len(values)):
        funct(make_row(values[i], val_bufs[i + 1]))

    funct(border)
