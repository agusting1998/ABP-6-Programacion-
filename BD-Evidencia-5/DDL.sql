CREATE TABLE Usuario (
    email VARCHAR(255) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    passw VARCHAR(255) NOT NULL,
    rol VARCHAR(50) NOT NULL DEFAULT 'usuario'
);

CREATE TABLE Dispositivo (
    nombre_dispositivo VARCHAR(255) PRIMARY KEY,
    tipo VARCHAR(50) NOT NULL,
    estado VARCHAR(20) NOT NULL
);

CREATE TABLE Automatizacion (
    nombre_automatizacion VARCHAR(255) PRIMARY KEY,
    descripcion TEXT,
    acciones TEXT
);

CREATE TABLE Gestion (
    email_usuario VARCHAR(255),
    nombre_dispositivo VARCHAR(255),
    PRIMARY KEY (email_usuario, nombre_dispositivo),
    FOREIGN KEY (email_usuario) REFERENCES Usuario(email),
    FOREIGN KEY (nombre_dispositivo) REFERENCES Dispositivo(nombre_dispositivo)
);
CREATE TABLE Activacion (
    email_usuario VARCHAR(255),
    nombre_automatizacion VARCHAR(255),
    fecha_activacion DATETIME,
    PRIMARY KEY (email_usuario, nombre_automatizacion, fecha_activacion),
    FOREIGN KEY (email_usuario) REFERENCES Usuario(email),
    FOREIGN KEY (nombre_automatizacion) REFERENCES Automatizacion(nombre_automatizacion)
);
CREATE TABLE Control (
    nombre_automatizacion VARCHAR(255),
    nombre_dispositivo VARCHAR(255),
    PRIMARY KEY (nombre_automatizacion, nombre_dispositivo),
    FOREIGN KEY (nombre_automatizacion) REFERENCES Automatizacion(nombre_automatizacion),
    FOREIGN KEY (nombre_dispositivo) REFERENCES Dispositivo(nombre_dispositivo)
);
