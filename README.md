Taller 3 Django
A continuación, se muestran los requerimientos:

1. Consultar la lista de medidas en formato JSON:
Para realizar el requerimiento, se hace la siguiente ruta:
http://localhost:8000/measurements/list/
Para resultar en el siguiente resultado
![image](https://user-images.githubusercontent.com/60165572/131186667-306d426c-f8b7-4811-9f4f-0f4479ec7d3d.png)

2. Dar una medida por id: en este caso, se muestra el que tiene el ID1 con la siguiente ruta: http://localhost:8000/measurements/byId/
Se puede ver en este caso que retorna el de ID = 1
![image](https://user-images.githubusercontent.com/60165572/131187844-424423bd-cdd5-44c7-8ca4-f14fda9efa22.png)

3. Borrar una medida dado su identificador:
Para esto, se ejecuta la siguiente ruta: http://localhost:8000/measurements/deleteById/
En la consulta anterior se puede ver que hay un elemento con pk=3, nótese que ese es el que va a ser eliminado, ya que la ruta devuelve todos los que quedaron:
![image](https://user-images.githubusercontent.com/60165572/131187095-4d77c5a3-81fe-44d5-9474-f42659b41e47.png)

4. Actualizar por ID. Saliendo de la lista resultante después de eliminar el de ID 3, se puede ver ahora que vamos a actualizar el de pk, su place a "Ay mi madre, el bicho al United"
Esto con la siguiente ruta: http://localhost:8000/measurements/editById
Obteniendo el actualizado, tal como se muestra en la imagen:
![image](https://user-images.githubusercontent.com/60165572/131188263-f40e7cc6-4e6f-43f3-903f-ea89d527d94d.png)



