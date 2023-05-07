import os
import pypandoc

input_file = "report.md"
output_file = "output.docx"

# Convert the Markdown file to Word using Pandoc and PyPandoc
pypandoc.convert_file(input_file, "docx", outputfile=output_file)

# Print the absolute path of the output file
print(os.path.abspath(output_file))
