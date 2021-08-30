Taller 3 Django
A continuación, se muestran los requerimientos:

1. Consultar la lista de medidas en formato JSON:
Para realizar el requerimiento, se hace la siguiente ruta:
http://localhost:8000/measurements/list/
Para resultar en el siguiente resultado
![image](https://user-images.githubusercontent.com/60165572/131340447-c8f89885-5ede-4881-b138-83c03e540348.png)


2. Dar una medida por id: en este caso, se muestra el que tiene el ID1 con la siguiente ruta: http://localhost:8000/measurements/byId/1
Se puede ver en este caso que retorna el de ID = 1
![image](https://user-images.githubusercontent.com/60165572/131340509-38ba69b6-3f2c-4c74-8f15-520a3f37c36d.png)


3. Borrar una medida dado su identificador:
Para esto, se ejecuta la siguiente ruta: http://localhost:8000/measurements/deleteById/5
En la consulta anterior se puede ver que hay un elemento con pk=5, nótese que ese es el que va a ser eliminado, ya que la ruta devuelve todos los que quedaron:
![image](https://user-images.githubusercontent.com/60165572/131340707-00c9d53c-ca35-4bed-bc44-f8c8410b788e.png)


4. Actualizar por ID. Saliendo de la lista resultante después de eliminar el de ID 5, se puede ver ahora que vamos a actualizar el de pk=2, su place a "Lio the GOAT" 👾
Esto con la siguiente ruta: http://localhost:8000/measurements/editById/2/
Obteniendo el actualizado, tal como se muestra en la imagen:
![image](https://user-images.githubusercontent.com/60165572/131341193-74eb0568-090e-4a21-b9f6-451c503f5b50.png)




