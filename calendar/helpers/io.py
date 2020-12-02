def read_file_by_newline(file_name, fn, delimiter='\n'):
    with open(file_name, "r", encoding='utf8', newline=delimiter) as fp:
        line = fp.readline()
        while line:
            try:
                line = fp.readline()
                fn(line)
            except Exception as e:
                print(e)
