from test_camAccess import extract_camera_information
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter, landscape
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

# Function to generate a PDF report
def create_pdf_report(data):
    doc = SimpleDocTemplate("camera_report.pdf", pagesize=landscape(letter))
    elements = []

    for group, info in data.items():
        data_rows = []
        data_rows.append(["Property", "Value"])
        for key, value in info.items():
            data_rows.append([key, value])
        table = Table(data_rows, colWidths=[180, 180])
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ]))
        elements.append(table)

    doc.build(elements)

if __name__ == '__main__':

    camera_feature = extract_camera_information()
    create_pdf_report(camera_feature)
