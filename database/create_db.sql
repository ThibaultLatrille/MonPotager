-- PostgreSQL
CREATE DATABASE monpotager ENCODING = 'UTF-8';
CREATE EXTENSION postgis;
USE monpotager;
-- créations des tables, les noms ont été traduits en anglais
CREATE TABLE IF NOT EXISTS media (
    hash BYTEA PRIMARY KEY,
    url VARCHAR(255) UNIQUE NOT NULL,
    type CHAR(1) NOT NULL
);
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE,
    nickname VARCHAR(32) NOT NULL,
    password BYTEA NOT NULL,
    timezone VARCHAR(32) NOT NULL,
    rang VARCHAR(16),
    api_key BYTEA, -- 16 octets (GUID)
    facebook_id INTEGER,
    facebook_token BYTEA,
    twitter_id INTEGER,
    twitter_token BYTEA,
    google_id INTEGER,
    google_token BYTEA,
    github_id INTEGER,
    github_token BYTEA,
    tou_accepted BOOLEAN DEFAULT FALSE
);
CREATE TABLE IF NOT EXISTS garden (
    id SERIAL PRIMARY KEY,
    name VARCHAR(64) NOT NULL,
    owner INTEGER NOT NULL,
    location GEOGRAPHY,
    public BOOLEAN DEFAULT TRUE,
    description TEXT
);
CREATE TABLE IF NOT EXISTS interaction (
    id SERIAL PRIMARY KEY,
    name VARCHAR(64) NOT NULL,
    owner INTEGER NOT NULL,
    description TEXT
);
CREATE TABLE IF NOT EXISTS modification (
    id SERIAL PRIMARY KEY,
    datetime TIMESTAMP DEFAULT now(),
    what CHAR(1),
    item INTEGER,
    who INTEGER NOT NULL,
    approved_by INTEGER,
    action CHAR(1) NOT NULL,
    old_values JSON NOT NULL
);
CREATE TABLE IF NOT EXISTS experimentation (
    id SERIAL PRIMARY KEY,
    name VARCHAR(64) NOT NULL,
    description TEXT
);
CREATE TABLE IF NOT EXISTS role (
    who INTEGER NOT NULL,
    experimentation INTEGER NOT NULL,
    creator BOOLEAN DEFAULT FALSE,
    roles VARCHAR(8)
);
CREATE TABLE IF NOT EXISTS name (
    id SERIAL PRIMARY KEY,
    plant INTEGER NOT NULL,
    lang CHAR(3) NOT NULL,
    name VARCHAR(64) NOT NULL
);
CREATE TABLE IF NOT EXISTS specie (
    id SERIAL PRIMARY KEY,
    category CHAR(1) NOT NULL,
    --plant information below
    hardiness CHAR(1),
    exposure NUMERIC(1),
    water NUMERIC(1),
    vegetation CHAR(1),
    multiplication VARCHAR(5),
    plantation VARCHAR(8),
    foliage CHAR(1),
    ph CHAR(1),
    shapes VARCHAR(16),
    climates VARCHAR(8),
    transformations VARCHAR(8),
    height_min SMALLINT,
    height_max SMALLINT,
    diameter_min SMALLINT,
    diameter_max SMALLINT,
    flower_colours VARCHAR(32),
    leaf_colours VARCHAR(32),
    density VARCHAR(8),
    calendar BYTEA
);
CREATE TABLE IF NOT EXISTS interaction (
    id SERIAL PRIMARY KEY,
    beneficial BOOLEAN DEFAULT TRUE,
    specie1 INTEGER NOT NULL,
    specie2 INTEGER NOT NULL,
    sources JSON NOT NULL
);
CREATE TABLE IF NOT EXISTS media_item (
    media INTEGER,
    specie INTEGER,
    garden INTEGER,
    experimentation INTEGER
);
CREATE TABLE IF NOT EXISTS favourite_plant (
    plant INTEGER,
    who INTEGER
);
-- création des clé étrangères
ALTER TABLE role ADD CONSTRAINT fk_role_user FOREIGN KEY (who) REFERENCES users (id);
ALTER TABLE role ADD CONSTRAINT fk_role_experimentation FOREIGN KEY (experimentation) REFERENCES experimentation (id);
ALTER TABLE media_item ADD CONSTRAINT fk_media_garden FOREIGN KEY (garden) REFERENCES garden (id);
ALTER TABLE media_item ADD CONSTRAINT fk_media_specie FOREIGN KEY (specie) REFERENCES specie (id);
ALTER TABLE media_item ADD CONSTRAINT fk_media_experimentation FOREIGN KEY (experimentation) REFERENCES experimentation (id);
ALTER TABLE garden ADD CONSTRAINT fk_garden_user FOREIGN KEY (owner) REFERENCES users (id);
ALTER TABLE interaction ADD CONSTRAINT fk_interaction_specie1 FOREIGN KEY (specie1) REFERENCES specie (id);
ALTER TABLE interaction ADD CONSTRAINT fk_interaction_specie2 FOREIGN KEY (specie2) REFERENCES specie (id);
ALTER TABLE favourite_plant ADD CONSTRAINT fk_favourite_plant FOREIGN KEY (plant) REFERENCES specie (id);
ALTER TABLE favourite_plant ADD CONSTRAINT fk_favourite_user FOREIGN KEY (who) REFERENCES users (id);
ALTER TABLE modification ADD CONSTRAINT fk_modification_who FOREIGN KEY (who) REFERENCES users (id);
ALTER TABLE modification ADD CONSTRAINT fk_modification_approver FOREIGN KEY (approved_by) REFERENCES users (id);
