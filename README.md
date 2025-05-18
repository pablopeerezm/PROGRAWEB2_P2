# PROGRAWEB2_P2

Pablo Pérez Martínez  
Universidad Europea del Atlántico  
Programación Web II

## Práctica 2 
Backend con Flask + GraphQL

## Cómo ejecutar el proyecto: 
```sh
# Primero se levantará el backend
# Clonar el repositorio
git clone url
# Instalar dependencias
pip install flask graphene flask-cors
# Ejecutar el servidor
python app.py
# Backend ejecutándose en -> http://localhost:5000/graphql
```
```sh
# A continuación se levantará el frontend con vue
# Clonar el repositorio de la práctica 1 actualizado
git clone https://github.com/pablopeerezm/PROGRAWEB2_P1.git
# Acceder a la carpeta del proyecto
cd ski-shop
# Instalar dependencias
npm install
# Ejecutar el servidor
npm run dev
# Abrir en el navegador -> localhost:5173
```
## Cómo probar que funciona
1. Abrir http://localhost:5173
2. Debería verse la lista de productos
3. Utilizar los botones + y - para modificar el stock.
4. El campo disponible cambia automáticamente a agotado si el stock vale 0.

   
