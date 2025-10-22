Criterios de Evaluación
Funcionalidad (40%)
 Sistema de autenticación JWT funcional
 Los tres roles implementados correctamente
 Todos los endpoints requeridos funcionan
 Validación de permisos correcta en cada endpoint
Código (30%)
 Uso de vistas basadas en clases (MethodView)
 Schemas de Marshmallow para validación
 Código organizado y legible
 Manejo apropiado de errores
Seguridad (20%)
 Contraseñas hasheadas (bcrypt o similar)
 Tokens JWT implementados correctamente
 Verificación de propiedad de recursos
 No hay endpoints sin protección que deberían tenerla
Arquitectura (10%)
 Separación de responsabilidades
 Uso de decoradores personalizados
 Código reutilizable
Plus Opcionales (Puntos Extra)
 Implementar refresh tokens
 Paginación en listados de posts
 Filtros y búsqueda de posts por categoría/autor
 Rate limiting (límite de requests por usuario)
 Tests con cobertura >70%
 Documentación con Swagger/OpenAPI
 Implementar soft delete en lugar de borrado físico
 Sistema de notificaciones (cuando alguien comenta tu post)
Ejemplo de Flujo de Trabajo
Usuario se registra → recibe confirmación
Usuario hace login → recibe JWT token
Usuario crea un post → incluye token en header Authorization: Bearer <token>
Otro usuario comenta el post → también autenticado
Moderador elimina un comentario inapropiado → verificación de rol
Admin cambia el rol de un usuario a moderador → solo admin puede hacerlo
