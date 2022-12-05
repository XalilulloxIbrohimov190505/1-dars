import random
xazina = "1"
xato ="4"
sandiq = ["{1}", "{2}", "{3}", "{4}", "{5}"]
xazina_raqam = random.randint(1, 5)
taxmin = int(input(f"Xazina qaysi sandiqda?\n{sandiq}"))
if taxmin==xazina_raqam:
    del sandiq[taxmin-1]
    sandiq.insert(taxmin-1, xazina)
    print(sandiq)
    print("Verey Good Good jop")
else:
    del sandiq[taxmin-1]
    sandiq.insert(taxmin-1, xato)
    del royxat[xazina_raqam-1]
    sandiq.insert(xazina_raqam-1,xazina)
    print(sandiq)
    print("Xato")
    print("Xazina {xazina_raqami} da edi")
    
          



