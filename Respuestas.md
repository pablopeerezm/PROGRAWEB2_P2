1. ¿Qué ventajas ofrece GraphQL sobre REST en este contexto?

GraphQL permite pedir exactamente los datos necesarios desde el frontend, en este caso `nombre`, `stock` o `disponible`, sin tener que hacer múltiples peticiones ni cargar campos innecesarios. 

Esto reduce el tráfico entre cliente y servidor, y simplifica el código en el frontend.


2. ¿Cómo se definen los tipos y resolvers en una API con GraphQL?

Los tipos se definen como estructuras que indican qué campos tiene cada objeto. En este caso `Producto` tendría `id`, `nombre`, `precio`, `stock` y `disponible`.

Los resolvers se definen dentro de las clases de consulta o mutación, y devuelven los datos que se solicitan desde le frontend.


3. ¿Por qué es importante que el backend también actualice disponible y no depender solo del frontend?

Porque en caso de manipular datos desde le navegador y saltarse la lógica de disponibilidad, podría causarnos problemas contar que está disponible un producto que en realidad no lo está.

Al controlar esa lógica también en el backend, se garantiza que el campo `disponible` siempre está bien calculado.


4. ¿Cómo garantizas que la lógica de actualización de stock y disponibilidad sea coherente?

Toda la lógica está centralizada en la mutación del backend: al modificar el stock, se recalcula automáticamente si el producto está disponible o no.

Esto asegura que la condición `stock > 0 => disponible = true` se aplique siempre.

   
