def createHTML(table):
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>JSON to PDF</title>
    </head>
    <body>
        <table>
            <tr>
                <th>Ability</th>
                <th>Description</th>
            </tr>
            {0}
        </table>
    </body>
    </html>
    """.format(table)
    
    with open('table.html', 'w') as f:
        f.write(html_content)


