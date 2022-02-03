def flatten_json(y, app_name):
    seperator = '/'
    prefix = '/%s/' % app_name
    out = {}

    def flatten(x, name=prefix):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + seperator)
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + seperator)
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)

    return out
