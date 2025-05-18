from flask import Flask, request, jsonify
from flask_cors import CORS
from graphene import ObjectType, String, Int, Float, Boolean, List, Field, Mutation, Schema
import graphene

# Ejemplo BBDD
productos = [
    {"id": 1, "nombre": "Esquís head", "precio": 750, "stock": 3, "disponible": True},
    {"id": 2, "nombre": "Esquís rossignol", "precio": 800, "stock": 1, "disponible": True},
    {"id": 3, "nombre": "Esquís volkl", "precio": 900, "stock": 0, "disponible": False}
]

# Tipo GraphQL para Producto
class ProductoType(ObjectType):
    id = Int()
    nombre = String()
    precio = Float()
    stock = Int()
    disponible = Boolean()

# Query para obtener todos los productos
class Query(ObjectType):
    todos_productos = List(ProductoType)

    def resolve_todos_productos(self, info):
        return productos
    
# Mutación para modificar stock
class ModificarStock(Mutation):
    class Arguments:
        id = Int(required=True)
        cantidad = Int(required=True)

    producto = Field(lambda: ProductoType)

    def mutate(root, info, id, cantidad):
        for prod in productos:
            if prod["id"] == id:
                nuevo_stock = prod["stock"] + cantidad
                prod["stock"] = max(nuevo_stock, 0)

                # Actualizar disponibilidad
                prod["disponible"] = prod["stock"] > 0

                return ModificarStock(producto=prod)
        raise Exception("Producto no encontrado")

class Mutation(ObjectType):
    modificar_stock = ModificarStock.Field()

schema = Schema(query=Query, mutation=Mutation)

# Flask y GraphQL
app = Flask(__name__)
CORS(app)

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    result = schema.execute(
        data.get("query"),
        variables=data.get("variables"),
    )
    response = {}
    if result.errors:
        response["errors"] = [str(error) for error in result.errors]
    if result.data:
        response["data"] = result.data

    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
