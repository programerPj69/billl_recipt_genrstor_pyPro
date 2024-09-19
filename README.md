# PDF Receipt Generator

This project is a Python application that allows users to create PDF receipts for course subscriptions. Users can enter multiple courses, apply discounts, and save the receipt as a PDF file with a custom name.

## Features

- **Unlimited Course Entries**: Users can add as many courses as needed.
- **Subtotal and Total Calculation**: Automatically calculates the subtotal and total after applying any discounts.
- **Custom PDF Naming**: Users can specify the name for each generated PDF file.
- **Simple User Interface**: Interactive prompts guide users through the process of entering course details.
Usage
Clone this repository or download the script.
Run the script using Python:
bash
Copy code
python generate_multiple_pdfs.py
Follow the prompts to enter course details:
Enter the date (DD/MM/YYYY)
Enter the course name
Enter the subscription type (e.g., Lifetime, 6 months)
Enter the price (Rs.)
After entering all courses, input the discount amount.
Specify a name for the PDF file (without the extension).
The PDF will be generated and saved in the current directory.
You will be prompted to create another PDF or exit the application.
Example
plaintext
Copy code
Enter the date (DD/MM/YYYY): 16/11/2020
Enter the name of the course: Full Stack Development with React & Node JS - Live
Enter the subscription type (e.g., Lifetime, 6 months): Lifetime
Enter the price (Rs.): 10999.00
Do you want to add another course? (yes/no): no
Enter the discount amount (Rs.): 3000.00
Enter the name for this PDF (without extension): receipt1
PDF generated successfully: receipt1.pdf
Do you want to create another PDF? (yes/no): no
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to the ReportLab team for the powerful PDF generation library.
css
Copy code

### How to Use This README
1. Create a file named `README.md` in your project directory.
2. Copy the above content into the `README.md` file.
3. Modify any sections as needed to better fit your project or preferences.

This `README.md` provides a clear overview of your project, how to use it, and what users can expect.







## Requirements

- Python 3.x
- `reportlab` library

### You can install the required library using pip:

```bash
  pip install reportlab
