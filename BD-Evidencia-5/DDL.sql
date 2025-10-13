-- Crear base de datos
CREATE DATABASE IF NOT EXISTS hogar_inteligente;

-- Usar la base de datos
USE hogar_inteligente;

-- Tabla Usuario
CREATE TABLE IF NOT EXISTS Usuario (
    email VARCHAR(255) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL DEFAULT '',
    apellido VARCHAR(100) NOT NULL DEFAULT '',
    passw VARCHAR(255) NOT NULL DEFAULT '',
    rol VARCHAR(50) NOT NULL DEFAULT 'usuario'
);

-- Tabla Dispositivo
CREATE TABLE IF NOT EXISTS Dispositivo (
    nombre_dispositivo VARCHAR(255) PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL DEFAULT '',
    estado VARCHAR(20) NOT NULL DEFAULT 'apagado'
);

-- Tabla Automatizacion
CREATE TABLE IF NOT EXISTS Automatizacion (
    nombre_automatizacion VARCHAR(255) PRIMARY KEY,
    descripcion TEXT,
    acciones TEXT
);

-- Tabla Gestion
CREATE TABLE IF NOT EXISTS Gestion (
    email_usuario VARCHAR(255) NOT NULL,
    nombre_dispositivo VARCHAR(255) NOT NULL,
    PRIMARY KEY (email_usuario, nombre_dispositivo),
    FOREIGN KEY (email_usuario) REFERENCES Usuario(email),
    FOREIGN KEY (nombre_dispositivo) REFERENCES Dispositivo(nombre_dispositivo)
);

-- Tabla Activacion
CREATE TABLE IF NOT EXISTS Activacion (
    email_usuario VARCHAR(255) NOT NULL,
    nombre_automatizacion VARCHAR(255) NOT NULL,
    fecha_activacion DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (email_usuario, nombre_automatizacion, fecha_activacion),
    FOREIGN KEY (email_usuario) REFERENCES Usuario(email),
    FOREIGN KEY (nombre_automatizacion) REFERENCES Automatizacion(nombre_automatizacion)
);

-- Tabla Control
CREATE TABLE IF NOT EXISTS Control (
    nombre_automatizacion VARCHAR(255) NOT NULL,
    nombre_dispositivo VARCHAR(255) NOT NULL,
    PRIMARY KEY (nombre_automatizacion, nombre_dispositivo),
    FOREIGN KEY (nombre_automatizacion) REFERENCES Automatizacion(nombre_automatizacion),
    FOREIGN KEY (nombre_dispositivo) REFERENCES Dispositivo(nombre_dispositivo)
);
