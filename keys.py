from closure import get_closure
from common import get_schema, get_subsets, get_dependencies, is_subset


def keys():
    schema = get_schema()
    dependencies = get_dependencies()
    subsets = get_subsets(schema)
    k = []
    for subset in subsets:
        closure = get_closure(subset, dependencies)
        if closure == schema:
            k.append(subset)

    k = find_keys(k)
    print('the schema keys are: ' + ",".join(k))


def find_keys(k):
    result = k.copy()
    for i in range(len(k)):
        for j in range(i + 1, len(k)):
            if is_subset(k[i], k[j]):
                if result.count(k[j]) > 0:
                    result.remove(k[j])

    return result


if __name__ == '__main__':
    keys()
