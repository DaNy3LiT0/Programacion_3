"""
Desarrolla un sistema de redes sociales con objetos como "Usuario", "Publicación" 
y "Comentario". Un objeto "Usuario" puede tener una lista de objetos "Publicación", 
y  cada  "Publicación"  puede  tener  una  lista  de  objetos  "Comentario".  Puedes 
implementar métodos para que los usuarios publiquen, comenten en publicaciones 
y realicen interacciones sociales como "me gusta". La red social necesita conocer 
los usuarios registrados.
"""

class Usuario:
    def __init__(self, nombre, apellido, email,username):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__email = email
        self.__username = username
        self.__publicaciones = []
        self.__seguidores = []
        self.__seguidos = []
        self.__likes = []

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_apellido(self):
        return self.__apellido

    def set_apellido(self, apellido):
        self.__apellido = apellido

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_username(self):
        return self.__username

    def set_username(self, username):
        self.__username = username

    def get_publicaciones(self):
        return self.__publicaciones

    def agregar_publicacion(self, publicacion):
        self.__publicaciones.append(publicacion)

    def get_seguidores(self):
        return self.__seguidores

    def agregar_seguidor(self, seguidor):
        self.__seguidores.append(seguidor)

    def get_seguidos(self):
        return self.__seguidos

    def agregar_seguido(self, seguido):
        self.__seguidos.append(seguido)

    def get_likes(self):
        return self.__likes

    def agregar_like(self, like):
        self.__likes.append(like)

    def publicar(self, contenido):
        publicacion = Publicacion(self, contenido)
        self.agregar_publicacion(publicacion)
        return publicacion

    def comentar(self, publicacion, contenido):
        comentario = Comentario(self, publicacion, contenido)
        publicacion.agregar_comentario(comentario)
        return comentario

    def dar_like(self, publicacion):
        self.agregar_like(publicacion)
        publicacion.agregar_like(self)

    def seguir(self, usuario):
        self.agregar_seguido(usuario)
        usuario.agregar_seguidor(self)

class Publicacion:
    def __init__(self, usuario, contenido):
        self.__usuario = usuario
        self.__contenido = contenido
        self.__comentarios = []
        self.__likes = []

    def get_usuario(self):
        return self.__usuario

    def get_contenido(self):
        return self.__contenido

    def get_comentarios(self):
        return self.__comentarios

    def agregar_comentario(self, comentario):
        self.__comentarios.append(comentario)
    
    def eliminar_comentario(self, comentario):
        self.__comentarios.remove(comentario)

    def get_likes(self):
        return self.__likes

    def agregar_like(self, like):
        self.__likes.append(like)

class Comentario:
    def __init__(self, usuario, publicacion, contenido):
        self.__usuario = usuario
        self.__publicacion = publicacion
        self.__contenido = contenido

    def get_usuario(self):
        return self.__usuario

    def get_publicacion(self):
        return self.__publicacion

    def get_contenido(self):
        return self.__contenido
    
    def set_contenido(self, contenido):
        self.__contenido = contenido 

class RedSocial:
    def __init__(self):
        self.__usuarios = []

    def get_usuarios(self):
        return self.__usuarios

    def agregar_usuario(self, usuario):
        self.__usuarios.append(usuario)

    def buscar_usuario_por_username(self, username):
        for usuario in self.__usuarios:
            if usuario.get_username() == username:
                return usuario
        return None


# Ejemplo de uso
red_social = RedSocial()

usuario1 = Usuario("Juan", "Pérez", "juan.perez@example.com")
usuario2 = Usuario("María", "González", "maria.gonzalez@example.com")

red_social.registrar_usuario(usuario1)
red_social.registrar_usuario(usuario2)

publicacion1 = Publicacion("Hola, mundo!", usuario1)
publicacion2 = Publicacion("Este es un ejemplo de publicación", usuario2)

usuario1.publicar(publicacion1)
usuario2.publicar(publicacion2)

comentario1 = Comentario("Me gusta!", usuario2, publicacion1)
comentario2 = Comentario("Este es un comentario", usuario1, publicacion2)

publicacion1.agregar_comentario(comentario1)
publicacion2.agregar_comentario(comentario2)

print("Usuarios registrados:")
for usuario in red_social.get_usuarios():
    print(f"{usuario.get_nombre()} {usuario.get_apellido()}")

print("\nPublicaciones de Juan Pérez:")
for publicacion in usuario1.get_publicaciones():
    print(f"{publicacion.get_texto()}")

print("\nComentarios en la publicación de Juan Pérez:")
for comentario in publicacion1.get_comentarios():
    print(f"{comentario.get_texto()}")

print(f"\nMe gusta en la publicación de Juan Pérez: {publicacion1.get_me_gusta()}")