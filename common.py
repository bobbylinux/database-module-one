from itertools import combinations


def get_subsets(schema):
    subsets = []
    for i in range(len(schema) + 1):
        temp = (combinations(schema, i + 1))
        for item in temp:
            subsets.append("".join(item))
    return subsets


def get_schema():
    schema_attributes = input('insert the R attributes: ')
    return "".join(sorted(schema_attributes.upper()))


def get_dependencies():
    dependencies_in = input(
        'insert the first F dependency (ex: AC->B insert: AC-B then press enter for the next dependency), '
        'insert \'stop\' to finish: ')
    dependencies = []
    while dependencies_in.lower() != 'stop':
        parts = dependencies_in.split('-')
        if len(parts) > 1:
            dependency = {
                'determinant': "".join(sorted(parts[0].upper())),
                'dependent': "".join(sorted(parts[1].upper()))
            }
            dependencies.append(dependency)
        dependencies_in = input('insert the F dependencies (ex: AC->B insert: AC-B), insert \'stop\' to finish: ')

    return dependencies


def get_decompositions():
    decompositions_in = input('insert the rho decompositions (ex: ABC BCDE), insert \'stop\' to finish: ')
    decompositions = []
    while decompositions_in.lower() != 'stop':
        decompositions.append("".join(sorted(decompositions_in.upper())))
        decompositions_in = input('insert the rho decompositions (ex: ABC BCDE), insert \'stop\' to finish: ')

    return decompositions


def is_subset(subset, superset):
    result = True
    for item in subset:
        if item not in superset:
            result = False
            break
    return result


def add_element_to_set(element, set_of_elements):
    for item in element:
        if item not in set_of_elements:
            set_of_elements += item.upper()
    return "".join(sorted(set_of_elements))


def get_union(first, second):
    union = second
    for char in first:
        if char not in second:
            union += char
    union = sorted(union)
    return "".join(union)


def get_intersection(first, second):
    intersection = ''
    for char in first:
        if char in second:
            intersection += char
    intersection = sorted(intersection)
    return "".join(intersection)
