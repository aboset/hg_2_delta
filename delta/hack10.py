#agregar después del item 500
#los alias qux y thud
#[100,200,300,400,500,600,700]  result >  [100,200,300,400,500,qux,thud,600,700]


lista = [100,200,300,400,500,600,700]
for i in range(len(lista)):
    if lista[i] ==500:
        lista.insert(i+1,'qux')
    elif lista[i] == 'qux':
        lista.insert(i+1,'thud')


print(lista)