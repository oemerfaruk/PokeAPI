from weasyprint import HTML

def html2pdf():
    html = HTML(string=open('table.html').read())

    html.write_pdf('table.pdf')