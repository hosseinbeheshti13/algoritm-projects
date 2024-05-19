def modified_subsets(length, subset_length):
    def generate_subsets(current_subset, remaining_elements, remaining_subsets):
        if remaining_subsets == 0:
            if not remaining_elements:
                all_subsets.append(current_subset[:])
            return
        if not remaining_elements:
            return
        current_subset.append(remaining_elements[0])
        generate_subsets(current_subset, remaining_elements[1:], remaining_subsets - 1)
        current_subset.pop()
        generate_subsets(current_subset, remaining_elements[1:], remaining_subsets)

    all_subsets = []
    generate_subsets([], list(range(1, length + 1)), subset_length)
    return all_subsets

length = 6
subset_length = 3
print("Modified subsets:", modified_subsets(length, subset_length))