def define_array():
  array = []
  arrayLenght = int(input("Ingrese la dimensión del Array: "))
  while arrayLenght == 0:
        print("El arreglo no puede estar vacío")
        arrayLenght = int(input("Ingrese la dimensión del Array: "))
  for x in range(arrayLenght):
        arrayItems = int(input("Ingrese un valor: "))
        array.append(arrayItems)
  print(array)
  search = int(input("Ingresa el valor a buscar en el arreglo: "))
  found = binary_search(array, search)
  if found != None:
    print("El valor se encuentra en la posición: ", found)
  else:
    print("El valor no existe.")

def binary_search(arr, value):
  arr.sort()
  print("El arreglo ordenado: ",arr)
  firstIndex = 0
  lastIndex = len(arr) - 1
  while firstIndex <= lastIndex:
    middleIndex = (firstIndex + lastIndex) // 2
    aux = arr[middleIndex]
    if aux == value:
      return middleIndex
    if aux > value:
      lastIndex = middleIndex - 1
    else:
      firstIndex = middleIndex + 1
  return None

define_array()