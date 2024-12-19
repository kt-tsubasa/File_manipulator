import sys

command = sys.argv[1]
output_data = ''

if command == "reverse":
    import_path = sys.argv[2]
    output_path = sys.argv[3]

    with open(import_path, mode='r') as f:
        original_data = f.read().strip()

    output_data += original_data[::-1]

    with open(output_path, mode='w') as f:
        f.write(output_data)

elif command == "copy":
    import_path = sys.argv[2]
    output_path = sys.argv[3]

    with open(import_path, mode='r') as f:
        original_data = f.read().strip()
    
    output_data += original_data

    with open(output_path, mode='w') as f:
        f.write(output_data)


elif command == "duplicate-contents":
    import_path = sys.argv[2]

    with open(import_path, mode='r') as f:
        original_data = f.read().strip()
    
    for i in range(int(sys.argv[3])):
        output_data += original_data + "\n"

    with open(import_path, mode='a') as f:
        f.write(output_data)

elif command == "replace-string":
    import_path = sys.argv[2]

    with open(import_path, mode='r') as f:
        original_data = f.read().strip()

    output_data = original_data.replace(sys.argv[3], sys.argv[4])

    with open(import_path, mode='w') as f:
        f.write(output_data)