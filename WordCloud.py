def process_file(input_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()
        
        # Split the content by commas
        text_strings = content.split(',')
        
        # Remove spaces from each string
        cleaned_strings = [s.replace(' ', '') for s in text_strings]
        
        # Write the cleaned strings to OUTPUT.txt, each on a new line
        with open('OUTPUT.txt', 'w') as outfile:
            for string in cleaned_strings:
                outfile.write(string + '\n')
                
        print("Processing complete. Check OUTPUT.txt for results.")
    
    except FileNotFoundError:
        print(f"Error: The file {input_filename} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    input_filename = input("Enter the name of the text file to be processed: ")
    process_file(input_filename)
