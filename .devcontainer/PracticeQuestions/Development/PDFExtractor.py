# import PyPDF2  # to read pdf
# import re  # matching strings

# # Assign File
# pdf = open("CaseStudy.pdf", 'rb')  # Open the PDF file in binary mode
# reader = PyPDF2.PdfReader(pdf)

# # Access the first page (index 0)
# page = reader.pages[0]

# # Extract text from the page
# text = page.extract_text()
# print(text)

# # Close the PDF file
# pdf.close()
# importing required classes 
from pypdf import PdfReader 

# creating a pdf reader object 
reader = PdfReader('CaseStudy.pdf') 

# printing number of pages in pdf file 
print(len(reader.pages)) 

# creating a page object 
page = reader.pages[0] 

# extracting text from page 
print(page.extract_text()) 
