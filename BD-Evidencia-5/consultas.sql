USE hogar_inteligente;


-- 1. Listar dispositivos de cada usuario con su rol
SELECT 
    u.nombre,
    u.email,
    u.rol,
    d.nombre_dispositivo,
    d.tipo,
    d.estado
FROM Usuario u
JOIN Gestion g ON u.email = g.email_usuario
JOIN Dispositivo d ON g.nombre_dispositivo = d.nombre_dispositivo
ORDER BY u.nombre, d.nombre_dispositivo;

-- 2. Mostrar automatizaciones activadas por cada usuario
SELECT 
    u.nombre,
    a.nombre_automatizacion,
    a.descripcion,
    act.fecha_activacion
FROM Usuario u
JOIN Activacion act ON u.email = act.email_usuario
JOIN Automatizacion a ON act.nombre_automatizacion = a.nombre_automatizacion
ORDER BY act.fecha_activacion DESC;

-- 3. Dispositivos controlados por cada automatización
SELECT 
    a.nombre_automatizacion,
    a.descripcion,
    COUNT(c.nombre_dispositivo) as cantidad_dispositivos,
    GROUP_CONCAT(d.nombre_dispositivo) as dispositivos
FROM Automatizacion a
LEFT JOIN Control c ON a.nombre_automatizacion = c.nombre_automatizacion
LEFT JOIN Dispositivo d ON c.nombre_dispositivo = d.nombre_dispositivo
GROUP BY a.nombre_automatizacion, a.descripcion
ORDER BY cantidad_dispositivos DESC;

-- 4. Historial completo de automatizaciones con dispositivos afectados
SELECT 
    u.nombre as usuario,
    a.nombre_automatizacion,
    a.descripcion,
    GROUP_CONCAT(DISTINCT c.nombre_dispositivo) as dispositivos_afectados,
    act.fecha_activacion
FROM Usuario u
JOIN Activacion act ON u.email = act.email_usuario
JOIN Automatizacion a ON act.nombre_automatizacion = a.nombre_automatizacion
LEFT JOIN Control c ON a.nombre_automatizacion = c.nombre_automatizacion
GROUP BY u.email, a.nombre_automatizacion, act.fecha_activacion
ORDER BY act.fecha_activacion DESC;

-- 5. Usuarios administradores y dispositivos que gestionan
SELECT 
    u.nombre,
    u.email,
    u.rol,
    COUNT(g.nombre_dispositivo) as total_dispositivos,
    GROUP_CONCAT(d.tipo) as tipos_dispositivos
FROM Usuario u
LEFT JOIN Gestion g ON u.email = g.email_usuario
LEFT JOIN Dispositivo d ON g.nombre_dispositivo = d.nombre_dispositivo
WHERE u.rol = 'admin'
GROUP BY u.email, u.nombre, u.rol
ORDER BY total_dispositivos DESC;



-- 6. Usuarios que han activado más de una automatización
SELECT 
    u.nombre,
    u.email,
    COUNT(act.nombre_automatizacion) as total_activaciones
FROM Usuario u
JOIN Activacion act ON u.email = act.email_usuario
GROUP BY u.email, u.nombre
HAVING COUNT(act.nombre_automatizacion) > 1
ORDER BY total_activaciones DESC;

-- 7. Automatizaciones que controlan dispositivos de tipo 'luz'
SELECT DISTINCT
    a.nombre_automatizacion,
    a.descripcion,
    (SELECT COUNT(*) FROM Control WHERE nombre_automatizacion = a.nombre_automatizacion AND nombre_dispositivo IN 
        (SELECT nombre_dispositivo FROM Dispositivo WHERE tipo = 'luz')
    ) as luces_controladas
FROM Automatizacion a
WHERE a.nombre_automatizacion IN (
    SELECT DISTINCT c.nombre_automatizacion 
    FROM Control c 
    JOIN Dispositivo d ON c.nombre_dispositivo = d.nombre_dispositivo 
    WHERE d.tipo = 'luz'
);

-- 8. Dispositivos que están encendidos y son gestionados por usuarios estándar
SELECT 
    d.nombre_dispositivo,
    d.tipo,
    d.estado,
    u.nombre as usuario,
    u.email
FROM Dispositivo d
JOIN Gestion g ON d.nombre_dispositivo = g.nombre_dispositivo
JOIN Usuario u ON g.email_usuario = u.email
WHERE d.estado IN ('encendido', 'activo', 'cerrado')
  AND u.email IN (
    SELECT email FROM Usuario WHERE rol = 'usuario'
  )
ORDER BY d.tipo, u.nombre;

-- 9. Cámaras activas y automatizaciones que las controlan
SELECT 
    d.nombre_dispositivo,
    d.estado,
    COUNT(c.nombre_automatizacion) as automatizaciones_controladas,
    GROUP_CONCAT(DISTINCT c.nombre_automatizacion) as automatizaciones
FROM Dispositivo d
LEFT JOIN Control c ON d.nombre_dispositivo = c.nombre_dispositivo
WHERE d.tipo = 'cámara'
GROUP BY d.nombre_dispositivo, d.estado
ORDER BY automatizaciones_controladas DESC;

-- 10. Estadística: Cantidad de dispositivos por tipo y estado
SELECT 
    tipo,
    estado,
    COUNT(*) as cantidad,
    (SELECT COUNT(DISTINCT email_usuario) FROM Gestion WHERE nombre_dispositivo IN 
        (SELECT nombre_dispositivo FROM Dispositivo WHERE tipo = Dispositivo.tipo)
    ) as usuarios_gestionan
FROM Dispositivo
GROUP BY tipo, estado
ORDER BY tipo, estado;
