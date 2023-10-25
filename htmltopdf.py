from weasyprint import HTML

def html2pdf():
    html = HTML(string=open('pokemon.html').read())

    html.write_pdf('pokemon.pdf')