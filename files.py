def read_and_modify_file(input_filename, output_filename):
  """
  Reads the content of the input file, modifies it, and writes the modified 
  content to the output file.

  Args:
    input_filename: The name of the input file.
    output_filename: The name of the output file.
  """
  try:
    with open(input_filename, 'r') as infile:
      content = infile.read()

    # Modify the content (example: convert to uppercase)
    modified_content = content.upper() 

    with open(output_filename, 'w') as outfile:
      outfile.write(modified_content)

    print(f"Successfully modified '{input_filename}' and wrote to '{output_filename}'.")

  except FileNotFoundError:
    print(f"Error: Input file '{input_filename}' not found.")
  except IOError:
    print(f"Error: Could not read from '{input_filename}' or write to '{output_filename}'.")

if __name__ == "__main__":
  while True:
    try:
      input_filename = input("Enter the input filename: ")
      output_filename = input("Enter the output filename: ")
      read_and_modify_file(input_filename, output_filename)
      break 
    except FileNotFoundError:
      print(f"Error: Input file '{input_filename}' not found.")
      continue