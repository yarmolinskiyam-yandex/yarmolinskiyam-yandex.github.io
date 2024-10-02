import csv

# Define the input CSV file and output Markdown file paths
input_csv = 'students.csv'  # Replace with your CSV file path
output_md = 'STUDENTS.md'  # The generated Markdown file

# Function to generate the markdown table
def generate_md_table(input_csv, output_md):
    with open(input_csv, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        
        # Open the output file to write
        with open(output_md, 'w', encoding='utf-8') as mdfile:
            # Write the header row for the markdown table
            mdfile.write('# Ученики 11 кракена\n\n')
            mdfile.write('| ФИО | GitHub | Blog |\n')
            mdfile.write('| --- | --- | --- |\n')
            
            # Iterate through each row of the CSV file and write to the markdown file
            for row in reader:
                name = row['Name']
                username = row['username']
                
                # Construct each row in markdown format
                md_row = f'| {name} | [{username}](https://github.com/{username}) | [Блог {username}](https://{username}.github.io) |\n'
                mdfile.write(md_row)

    print(f'Markdown table generated and saved to {output_md}')

# Call the function to generate the markdown table
generate_md_table(input_csv, output_md)
