import io


def parse_file(path):
    handler = path
    if isinstance(handler, (str, unicode)):
        handler = open(handler)

    with handler as f:
        line_source = True

        result = list()
        while line_source:
            line_source = f.readline()
            line = line_source.rstrip('\n\r')
            if line.startswith('#'):
                result.append(line)
                continue

            #normalize
            line = line.replace('  ', ' ').replace('\t', ' ')

            #split
            line = line.split(' ')

            #filter
            line = filter(lambda v: bool(v), line)

            if len(line) >= 2:
                result.append((line[0], set(line[1:])))

        return result


def parse_string(data):
    s = io.BytesIO(data)
    return parse_file(s)


def build_file(config):
    for i, item in enumerate(config):
        try:
            if item.startswith('#'):
                continue
        except AttributeError:
            config[i] = '%s\t%s' % (item[0], ' '.join(item[1]))
    return '\n'.join(config)
