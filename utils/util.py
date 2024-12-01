def merge(dest: dict, src: dict, path=[]):
    for key in src:
        if isinstance(dest[key], dict) and isinstance(src[key], dict):
            merge(dest[key], src[key], path + [str(key)])
        elif dest[key] is None:
            dest[key] = src[key]
    return dest
