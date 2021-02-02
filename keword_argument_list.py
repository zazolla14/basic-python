#digunkan untuk cutom argumen agar dapat di psangan sesuka hati 
def create_html(tag, text, **Attributes):   #memanggil keword Argumen list yang berbentuk dictionary, sehingga bernilai key dan value
    html = (f"<{tag}")

    for key,value in Attributes.items():    #perulangan dilakaukan diantara kalimat yang ingin dimasukan argumen tambahan
        html = html + f" {key}:'{value}'"
    
    html = html + f"> {text} </{tag}>"
    print(Attributes)
    return html

html = create_html ("p", "Hello Python", style="paragraf")
print(html)
#<a href=" "> Ini Link </a>
html = create_html ("a", "Ini Link", href="google.com", style="link")
print(html)
html = create_html ("h1", "INI JUDUL", style="bold")
print(html)