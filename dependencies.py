from closure import get_closure
from common import get_dependencies, get_decompositions, get_intersection, get_union, is_subset


def calc_determinant_closure(det, depts, decs):
    z = det
    s = ''
    for dec in decs:
        closure = get_closure(get_intersection(det, dec), depts)
        s = get_union(s, get_intersection(closure, dec))

    while not is_subset(s, z) and s != '':
        z = get_union(s, z)
        for dec in decs:
            closure = get_closure(get_intersection(det, dec), depts)
            s = get_union(s, get_intersection(closure, dec))

    return z


def dependencies_preservation():
    dependencies = get_dependencies()
    decompositions = get_decompositions()
    success = True
    for dependency in dependencies:
        closure = calc_determinant_closure(dependency['determinant'], dependencies, decompositions)
        if not is_subset(dependency['dependent'], closure):
            success = False
    result = 'la decomposizione presentata '
    if not success:
        result += ' non '
    result += 'preserva le dipendenze funzionali presentate'
    print(result)


if __name__ == '__main__':
    dependencies_preservation()
