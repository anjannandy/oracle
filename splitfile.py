def split_file(input_file, part1_name, part2_name):
    with open(input_file, 'rb') as f:
        data = f.read()

    mid = len(data) // 2  # Splitting into two equal parts

    with open(part1_name, 'wb') as f1:
        f1.write(data[:mid])

    with open(part2_name, 'wb') as f2:
        f2.write(data[mid:])

    print(f"File '{input_file}' split into '{part1_name}' and '{part2_name}'")


if __name__ == "__main__":
    split_file("ml-llm-251.26094.80.13.zip", "part11.zip", "part12.zip")