def main():
    # Step 1: Read the contents of provinces.txt into a list
    provinces_list = read_list("provinces.txt")

    # Step 2: Print the original list
    print("Original list:")
    print(provinces_list)

    # Step 3: Remove the first and last elements
    if provinces_list:
        provinces_list.pop(0)  # Remove first element
    if provinces_list:
        provinces_list.pop(-1)  # Remove last element

    # Step 4: Replace all "AB" with "Alberta"
    for i in range(len(provinces_list)):
        if provinces_list[i] == "AB":
            provinces_list[i] = "Alberta"

    # Step 5: Count how many times "Alberta" appears
    alberta_count = provinces_list.count("Alberta")

    # Step 6: Print the modified list and the count
    print("\nModified list:")
    print(provinces_list)
    print(f"\n'Alberta' occurs {alberta_count} times in the modified list.")

def read_list(filename):
    """Reads a text file and returns a list of stripped lines."""
    lines = []
    with open(filename, "rt") as file:
        for line in file:
            clean_line = line.strip()
            lines.append(clean_line)
    return lines

if __name__ == "__main__":
    main()
