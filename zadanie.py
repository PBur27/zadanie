
def buy_books():

    products=[{"name":"Clean Code, Robert C. Martin","price":100,"vat":0.08},
    {"name":"Applying UML and Patterns, C. Larman","price":300,"vat":0.08},
    {"name":"Shipping","price":50,"vat":0.23}]

    separator = "|-----|-----|"
    table = "|-----|Total|"
    total = 0
    for product in products:
        total += product["price"]
        table+=f"{product["name"]}|"
        separator +="-"*len(product["name"])+"|"
    table+="\n"
    table+=separator
    table+="\n"

    table+= f"|VAT 8%|{total*1.08}|"
    for product in products:
        table += f"{product["price"]*1.08}|"
    
    table+="\n"

    table+= f"|VAT 23%|{total*1.23}|"
    for product in products:
        table += f"{product["price"]*1.23}|"

    print(table)

