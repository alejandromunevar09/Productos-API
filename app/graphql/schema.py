# =============================================================================
# Schema GraphQL definido en SDL (Schema Definition Language)
# Unidad 3 - Arquitectura de Aplicaciones Web
#
# Ariadne usa el enfoque schema-first: primero se define el contrato en SDL,
# luego se implementan los resolvers en Python.
# =============================================================================

type_defs = """
    type Producto {
        id: ID!
        nombre: String!
        descripcion: String
        precio: Float!
    }

    input ProductoInput {
        nombre: String!
        descripcion: String
        precio: Float!
    }

    input ProductoUpdateInput {
        nombre: String
        descripcion: String
        precio: Float
    }

    type Query {
        productos: [Producto!]!
        producto(id: ID!): Producto
    }

    type Mutation {
        crearProducto(input: ProductoInput!): Producto!
        actualizarProducto(id: ID!, input: ProductoUpdateInput!): Producto
        eliminarProducto(id: ID!): Boolean!
    }
"""