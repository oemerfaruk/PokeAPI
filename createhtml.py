def createHTML(table):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>JSON to PDF</title>
    </head>
    <body>
        <table>
            {}
        </table>
    </body>
    </html>
    """.format(table)
    
    with open('pokemon.html', 'w') as f:
        f.write(html_content)


