-- Database: prueba_rest

-- DROP DATABASE prueba_rest;

CREATE DATABASE prueba_rest
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'C.UTF-8'
    LC_CTYPE = 'C.UTF-8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- Table: public.usuarios

-- DROP TABLE public.usuarios;

CREATE TABLE public.usuarios
(
    nombre text COLLATE pg_catalog."default" NOT NULL,
    puesto text COLLATE pg_catalog."default" NOT NULL,
    correo text COLLATE pg_catalog."default" NOT NULL,
    fecha_nacimiento date NOT NULL
)

TABLESPACE pg_default;

ALTER TABLE public.usuarios
    OWNER to postgres;