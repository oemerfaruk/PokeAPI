from weasyprint import HTML

def html2pdf(name):
    html = HTML(string=open('{}.html'.format(name)).read())

    html.write_pdf('{}.pdf'.format(name))