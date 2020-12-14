def read_file_by_newline(file_name, fn, delimiter='\n'):
    with open(file_name, "r", encoding='utf8', newline=delimiter) as fp:
        line = fp.readline()
        while line:
            try:
                fn(line)
                line = fp.readline()
            except Exception as e:
                print(e)

def read_file_by_blankline(file_name, fn, delimiter=' '):
    with open(file_name, "r", encoding='utf8', newline=delimiter) as fp:
        line = fp.readline()
        while line:
            try:
                fn(line)
                line = fp.readline()
            except Exception as e:
                print(e)

