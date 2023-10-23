def createHTML(table,name):
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
    
    with open('{}.html'.format(name), 'w') as f:
        f.write(html_content)


