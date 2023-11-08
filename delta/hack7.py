#remplazar el item 300 
#por tú alias
#[100,200,300,400,500,600,700]  result >  [100,200,foo,400,500,600,700]


lista = [100,200,300,400,500,600,700]

for i in range(len(lista)):
    if lista[i]==300:
        lista[i]="foo"


print(lista)