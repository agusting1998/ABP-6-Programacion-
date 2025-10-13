USE hogar_inteligente;

INSERT INTO Usuario (email, nombre, apellido, passw, rol) VALUES
('yazmin@gmail.com', 'Yazmin', 'Orellana', 'pass123', 'admin'),
('diego@gmail.com', 'Diego', 'Mayo', 'pass456', 'admin'),
('matias@gmail.com', 'Matias', 'Aranda', 'pass789', 'admin'),
('santiago@gmail.com', 'Santiago', 'Hidalgo', 'pass101', 'usuario'),
('agustin@gmail.com', 'Agustin', 'Gallardo', 'pass112', 'usuario');

INSERT INTO Dispositivo (nombre_dispositivo, tipo, estado) VALUES
('luz_sala_estar', 'luz', 'encendido'),
('luz_cocina', 'luz', 'apagado'),
('camara_puerta', 'cámara', 'apagado'),
('camara_jardin', 'cámara', 'encendido'),
('termostato', 'electrodoméstico', 'encendido'),
('reproductor_tv', 'electrodoméstico', 'apagado'),
('luz_cuarto_principal', 'luz', 'apagado'),
('luz_baño', 'luz', 'encendido'),
('camara_habitacion_niños', 'cámara', 'apagado'),
('camara_garage', 'cámara', 'apagado'),
('aspiradora_robot', 'electrodoméstico', 'apagado'),
('cafetera', 'electrodoméstico', 'encendido'),
('sensor_humo_cocina', 'sensor', 'encendido'),
('sensor_movimiento_salon', 'sensor', 'apagado'),
('cerradura_inteligente', 'cerradura', 'cerrado');

INSERT INTO Automatizacion (nombre_automatizacion, descripcion, acciones) VALUES
('Modo Noche', 'Apaga luces y enciende cámaras para seguridad nocturna.', 'Apagar luces, encender cámaras'),
('Modo Día', 'Enciende luces y apaga cámaras.', 'Encender luces, apagar cámaras'),
('Bienvenida Casa', 'Enciende luces de entrada y TV.', 'Encender luces, encender TV'),
('Salir de Casa', 'Apaga todos los dispositivos.', 'Apagar todos los dispositivos'),
('Alarma de Humo', 'Suena alarma, enciende luces de emergencia y notifica.', 'Sonar alarma, encender luces, notificar');

INSERT INTO Gestion (email_usuario, nombre_dispositivo) VALUES
('yazmin@gmail.com', 'luz_sala_estar'),
('yazmin@gmail.com', 'camara_puerta'),
('diego@gmail.com', 'luz_cocina'),
('diego@gmail.com', 'termostato'),
('matias@gmail.com', 'reproductor_tv'),
('santiago@gmail.com', 'luz_sala_estar'),
('santiago@gmail.com', 'luz_cocina'),
('agustin@gmail.com', 'termostato');


INSERT INTO Activacion (email_usuario, nombre_automatizacion, fecha_activacion) VALUES
('yazmin@gmail.com', 'Modo Noche', '2025-09-12 21:00:00'),
('diego@gmail.com', 'Modo Día', '2025-09-12 08:30:00'),
('matias@gmail.com', 'Bienvenida Casa', '2025-09-11 18:45:00'),
('santiago@gmail.com', 'Modo Noche', '2025-09-11 22:15:00'),
('agustin@gmail.com', 'Alarma de Humo', '2025-09-15 01:00:00');

INSERT INTO Control (nombre_automatizacion, nombre_dispositivo) VALUES
('Modo Noche', 'luz_sala_estar'),
('Modo Noche', 'luz_cocina'),
('Modo Noche', 'luz_cuarto_principal'),
('Modo Noche', 'luz_baño'),
('Modo Noche', 'camara_puerta'),
('Modo Noche', 'camara_jardin'),
('Modo Noche', 'camara_habitacion_ninos'),
('Modo Día', 'luz_sala_estar'),
('Modo Día', 'luz_cocina'),
('Modo Día', 'camara_puerta');
