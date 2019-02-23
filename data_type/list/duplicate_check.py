def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output


def contains(values, obj):
    for value in values:
        # TODO compare with ISA data
        if obj == value:
            return True
    return False

# Remove duplicates from this list.
# values = [5, 5, 1, 1, 2, 3, 4, 4, 5]
# result = remove_duplicates(values)
# print(result)


values = [('a', 'b', 'd'), ('e','f','g'), 2, 3]
hasContain = contains(values, 2)
print(hasContain)
hasContain2 = contains(values, 10)
print(hasContain2)


