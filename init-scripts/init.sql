-- init.sql - Database initialization script for PostgreSQL

-- Enable PostGIS extension
CREATE EXTENSION IF NOT EXISTS postgis;
CREATE EXTENSION IF NOT EXISTS postgis_topology;

-- Create schemas
CREATE SCHEMA IF NOT EXISTS raw;
CREATE SCHEMA IF NOT EXISTS staging;
CREATE SCHEMA IF NOT EXISTS marts;

-- Grant permissions
GRANT ALL PRIVILEGES ON SCHEMA raw TO f1user;
GRANT ALL PRIVILEGES ON SCHEMA staging TO f1user;
GRANT ALL PRIVILEGES ON SCHEMA marts TO f1user;

-- Create raw tables (example for drivers)
CREATE TABLE IF NOT EXISTS raw.drivers (
    driverId INTEGER PRIMARY KEY,
    driverRef VARCHAR(100),
    number INTEGER,
    code VARCHAR(10),
    forename VARCHAR(100),
    surname VARCHAR(100),
    dob DATE,
    nationality VARCHAR(50),
    url TEXT,
    loaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create indexes
CREATE INDEX idx_drivers_ref ON raw.drivers(driverRef);
CREATE INDEX idx_drivers_nationality ON raw.drivers(nationality);

-- Create comments
COMMENT ON SCHEMA raw IS 'Raw data from Kaggle F1 dataset';
COMMENT ON SCHEMA staging IS 'Cleaned and standardized data';
COMMENT ON SCHEMA marts IS 'Star schema dimensional model';
COMMENT ON TABLE raw.drivers IS 'F1 drivers master data';

-- Create schema_migrations table
CREATE TABLE IF NOT EXISTS public.schema_migrations (
    version VARCHAR(10) PRIMARY KEY,
    description TEXT,
    executed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Log initialization
INSERT INTO public.schema_migrations (version, description, executed_at)
VALUES ('001', 'Initial schema setup', CURRENT_TIMESTAMP)
ON CONFLICT (version) DO NOTHING;
