import csv

# Define the input CSV file and output Markdown file paths
students_csv = 'students.csv'  # Replace with your CSV file path
tasks_csv = 'tasks.csv'  # Replace with your CSV file path
output_md = 'STUDENTS.md'  # The generated Markdown file

# Function to generate the markdown table
def generate_md_table(student_csv, tasks_csv, output_md):

    with open(student_csv, newline='', encoding='utf-8') as students:
        students_reader = csv.DictReader(students)

        with open(tasks_csv, newline='', encoding='utf-8') as tasks:
            tasks_reader = csv.DictReader(tasks)

            tasks = list(tasks_reader)

            tasks_count = sum(1 for _ in tasks)
                
            # Open the output file to write
            with open(output_md, 'w', encoding='utf-8') as mdfile:
                # Write the header row for the markdown table
                mdfile.write('# Ученики 11 кракена\n\n')
                mdfile.write('| ФИО | GitHub | Блог | ')
                
                for row in tasks:
                    name = row['DisplayName']
                    print(row)
                    mdfile.write(name + ' | ')
                
                mdfile.write('\n')
                mdfile.write('| --- | --- | --- |' + ' --- |' * tasks_count + '\n')
                
                # Iterate through each row of the CSV file and write to the markdown file
                for row in students_reader:
                    name = row['Name']
                    username = row['username']
                    
                    tasks_row = ''
                    for trow in tasks:
                        tasks_row += f' [Отчет](https://{username}.github.io/{trow['URL']}) |'

                    # Construct each row in markdown format
                    md_row = f'| {name} | [{username}](https://github.com/{username}) | [Блог {username}](https://{username}.github.io) |' + tasks_row + '\n'
                    mdfile.write(md_row)

    print(f'Markdown table generated and saved to {output_md}')

# Call the function to generate the markdown table
generate_md_table(students_csv, tasks_csv, output_md)
