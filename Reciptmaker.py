# Imports modules
from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet

# Function to get user input
def get_user_input():
    date = input("Enter the date (DD/MM/YYYY): ")
    name = input("Enter the name of the course: ")
    subscription = input("Enter the subscription type (e.g., Lifetime, 6 months): ")
    price = input("Enter the price (Rs.): ")
    return [date, name, subscription, price]

# Function to create PDF
def create_pdf(data, pdf_file_name):
    # Creating a Base Document Template of page size A4
    pdf = SimpleDocTemplate(pdf_file_name, pagesize=A4)

    # Standard stylesheet defined within reportlab itself
    styles = getSampleStyleSheet()

    # Fetching the style of Top level heading (Heading1)
    title_style = styles["Heading1"]
    title_style.alignment = 1

    # Creating the paragraph with the heading text
    title = Paragraph("Pjsofonic", title_style)

    # Creating a Table Style object
    style = TableStyle([
        ("BOX", (0, 0), (-1, -1), 1, colors.black),
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
        ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ])

    # Creating a table object and passing the style to it
    table = Table(data)
    table.setStyle(style)

    # Final step which builds the actual PDF
    pdf.build([title, table])
    print(f"PDF generated successfully: {pdf_file_name}")

# Main loop to create multiple PDFs
while True:
    # Initialize the DATA list with headers
    DATA = [["Date", "Name", "Subscription", "Price (Rs.)"]]

    # Collecting course data from the user
    while True:
        course_data = get_user_input()
        DATA.append(course_data)

        more = input("Do you want to add another course? (yes/no): ").strip().lower()
        if more != 'yes':
            break

    # Subtotal calculation
    subtotal = sum(float(course[3].replace(',', '').replace('/-', '')) for course in DATA[1:])
    DATA.append(["Sub Total", "", "", f"{subtotal:,.2f}/-"])

    # Discount
    discount = float(input("Enter the discount amount (Rs.): "))
    DATA.append(["Discount", "", "", f"-{discount:,.2f}/-"])

    # Total calculation
    total = subtotal - discount
    DATA.append(["Total", "", "", f"{total:,.2f}/-"])

    # Define unique PDF file name
    pdf_file_name = input("Enter the name for this PDF (without extension): ") + ".pdf"

    # Create the PDF
    create_pdf(DATA, pdf_file_name)

    # Ask if the user wants to create another PDF
    another = input("Do you want to create another PDF? (yes/no): ").strip().lower()
    if another != 'yes':
        break

print("Thank you for using the PDF generator!")
