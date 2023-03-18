import copy


def input(fname):
    ll = []
    with open(fname, 'r', encoding='utf-8-sig') as fin:
        for line in fin:
            items = line.strip().strip("\n").split(",")
            ll.append(items)
    return ll


def output(fname, ll):
    with open(fname, "w", encoding='utf-8-sig') as fout:
        for item in ll:
            fout.write(",".join(item))
            fout.write("\n")