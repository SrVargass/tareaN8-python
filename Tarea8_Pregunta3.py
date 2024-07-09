def separar(lista):
 lista_par=[]
 lista_impar=[]
 for x in lista:
  if x%2==0:
      lista_par.append(x)
  else:
      lista_impar.append(x)
 lista_par.sort()
 lista_impar.sort()
 return lista_par,lista_impar

lista=[6,5,2,1,7]
print("Lista inicial:",lista)
separar(lista)
par,impar=separar(lista)
print("pares:",par)
print("impares:",impar)


