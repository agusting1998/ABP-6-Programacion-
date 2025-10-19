USE hogar_inteligente;

-- 10 Usuarios
INSERT INTO Usuario (email, nombre, apellido, passw, rol) VALUES
('yazmin@gmail.com', 'Yazmin', 'Orellana', 'pass123', 'admin'),
('diego@gmail.com', 'Diego', 'Mayo', 'pass456', 'admin'),
('matias@gmail.com', 'Matias', 'Aranda', 'pass789', 'admin'),
('santiago@gmail.com', 'Santiago', 'Hidalgo', 'pass101', 'usuario'),
('agustin@gmail.com', 'Agustin', 'Gallardo', 'pass112', 'usuario'),
('laura@gmail.com', 'Laura', 'Gomez', 'passL44', 'usuario'),
('carlos@gmail.com', 'Carlos', 'Perez', 'passC77', 'usuario'),
('ana@gmail.com', 'Ana', 'Rodriguez', 'passA32', 'usuario'),
('javier@gmail.com', 'Javier', 'Lopez', 'passJ19', 'usuario'),
('elena@gmail.com', 'Elena', 'Martinez', 'passE55', 'admin');

-- 15 Dispositivos
INSERT INTO Dispositivo (nombre_dispositivo, tipo, estado) VALUES
('luz_sala_estar', 'luz', 'encendido'),
('luz_cocina', 'luz', 'apagado'),
('camara_puerta', 'cámara', 'apagado'),
('camara_jardin', 'cámara', 'encendido'),
('termostato_principal', 'electrodoméstico', 'encendido'),
('reproductor_tv', 'electrodoméstico', 'apagado'),
('luz_cuarto_principal', 'luz', 'apagado'),
('luz_baño', 'luz', 'encendido'),
('camara_habitacion_ninos', 'cámara', 'apagado'),
('camara_garage', 'cámara', 'apagado'),
('aspiradora_robot', 'electrodoméstico', 'apagado'),
('cafetera', 'electrodoméstico', 'encendido'),
('sensor_humo_cocina', 'sensor', 'activo'),
('sensor_movimiento_salon', 'sensor', 'inactivo'),
('cerradura_inteligente', 'cerradura', 'cerrado');

-- 10 Automatizaciones
INSERT INTO Automatizacion (nombre_automatizacion, descripcion, acciones) VALUES
('Modo Noche', 'Apaga luces y enciende cámaras para seguridad nocturna.', 'Apagar luces, encender cámaras'),
('Modo Día', 'Enciende luces y apaga cámaras.', 'Encender luces, apagar cámaras'),
('Bienvenida Casa', 'Enciende luces de entrada y TV.', 'Encender luces, encender TV'),
('Salir de Casa', 'Apaga todos los dispositivos.', 'Apagar todos los dispositivos'),
('Alarma de Humo', 'Suena alarma, enciende luces de emergencia y notifica.', 'Sonar alarma, encender luces, notificar'),
('Riego Matutino', 'Activa el riego del jardín a las 6:00 AM.', 'Activar sistema de riego'),
('Clima Caluroso', 'Enciende el aire acondicionado si la temperatura sube de 28°C.', 'Encender aire acondicionado, notificar'),
('Control de Acceso', 'Notifica al abrir o cerrar la cerradura principal.', 'Notificar evento de cerradura'),
('Apagado Automático', 'Apaga luces que han estado encendidas por más de 4 horas.', 'Apagar luces'),
('Cámaras Activas', 'Enciende todas las cámaras de seguridad al salir el último usuario.', 'Encender todas las cámaras');

-- 10 Gestiones
INSERT INTO Gestion (email_usuario, nombre_dispositivo) VALUES
('yazmin@gmail.com', 'luz_sala_estar'),
('yazmin@gmail.com', 'camara_puerta'),
('diego@gmail.com', 'luz_cocina'),
('diego@gmail.com', 'termostato_principal'),
('matias@gmail.com', 'reproductor_tv'),
('santiago@gmail.com', 'luz_sala_estar'),
('santiago@gmail.com', 'luz_cocina'),
('agustin@gmail.com', 'termostato_principal'),
('laura@gmail.com', 'aspiradora_robot'),
('carlos@gmail.com', 'cerradura_inteligente');

-- 10 Activaciones
INSERT INTO Activacion (email_usuario, nombre_automatizacion, fecha_activacion) VALUES
('yazmin@gmail.com', 'Modo Noche', '2025-09-12 21:00:00'),
('diego@gmail.com', 'Modo Día', '2025-09-12 08:30:00'),
('matias@gmail.com', 'Bienvenida Casa', '2025-09-11 18:45:00'),
('santiago@gmail.com', 'Modo Noche', '2025-09-11 22:15:00'),
('agustin@gmail.com', 'Alarma de Humo', '2025-09-15 01:00:00'),
('laura@gmail.com', 'Riego Matutino', '2025-09-13 06:00:00'),
('carlos@gmail.com', 'Modo Día', '2025-09-14 09:00:00'),
('ana@gmail.com', 'Salir de Casa', '2025-09-15 10:00:00'),
('javier@gmail.com', 'Modo Noche', '2025-09-14 20:30:00'),
('elena@gmail.com', 'Clima Caluroso', '2025-09-15 14:00:00');

-- 10 Controles
INSERT INTO Control (nombre_automatizacion, nombre_dispositivo) VALUES
('Modo Noche', 'luz_sala_estar'),
('Modo Noche', 'luz_cocina'),
('Modo Noche', 'luz_cuarto_principal'),
('Modo Noche', 'camara_puerta'),
('Modo Noche', 'camara_jardin'),
('Modo Día', 'luz_sala_estar'),
('Modo Día', 'luz_cocina'),
('Bienvenida Casa', 'luz_sala_estar'),
('Bienvenida Casa', 'reproductor_tv'),
('Alarma de Humo', 'sensor_humo_cocina');
