from common import is_subset, add_element_to_set, get_union


def get_closure(det, deps):
    z = det
    s = ''
    s = add_element_to_s(deps, z, s)

    while not is_subset(s, z) and s != '':
        z = get_union(s, z)
        s = add_element_to_s(deps, z, s)
    return z


def add_element_to_s(deps, z, s):
    for dep in deps:
        if is_subset(dep['determinant'], z):
            s = add_element_to_set(dep['dependent'], s)
    return s
