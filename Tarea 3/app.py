from pymongo import MongoClient

cliente = MongoClient('mongodb://localhost:27017/')
db = cliente['diccionario']
opcion = -1
while opcion != 0:
  print('========= MENU ========')
  print('[1] Mostrar')
  print('[2] Agregar')
  print('[3] Actualizar')
  print('[4] Eliminar')
  print('[5] Buscar')
  print('[0] Salir')
  opcion = int(input('Opcion: '))

  if opcion == 1:
    lista = [i for i in db.palabra.find()]
    if len(lista) == 0:
      print('No hay palabras!')
    else:
      for i in lista:
        print('-'*30)
        print(f'Nombre: {i["nombre"]}\nSignificado: {i["significado"]}')

  elif opcion == 2:
    db.palabra.insert_one({
      'nombre': input('Nombre: ').lower(),
      'significado': input('Significado: ').lower()
    })
    print('Palabra agregada!')

  elif opcion == 3:
    nombre = input('Ingrese el nombre de la palabra: ').lower()
    palabra = db.palabra.find_one({'nombre':nombre})
    if palabra:
      significado = input('Ingrese el nuevo significado: ')
      db.palabra.update_one({'nombre':nombre},{'$set':{'significado':significado}})
      print('Palabra actualizada!')
    else:
      print('La palabra no existe!')
  
  elif opcion == 4:
    nombre = input('Ingrese el nombre de la palabra: ').lower()
    palabra = db.palabra.find_one({'nombre':nombre})
    if palabra:
      db.palabra.delete_one({'nombre':nombre})
      print('Palabra eliminada!')
    else:
      print('La palabra no existe!')
  
  elif opcion == 5:
    nombre = input('Ingrese el nombre de la palabra: ').lower()
    palabra = db.palabra.find_one({'nombre':nombre})
    if palabra:
      print(f'Nombre: {palabra["nombre"]}\nSignificado: {palabra["significado"]}')
    else:
      print('La palabra no existe!')