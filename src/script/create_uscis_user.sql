-- Role: uscis
-- DROP ROLE IF EXISTS uscis;

CREATE ROLE uscis WITH
  LOGIN
  NOSUPERUSER
  INHERIT
  NOCREATEDB
  NOCREATEROLE
  NOREPLICATION
  ENCRYPTED PASSWORD 'md5ca184541f2a60466cb0756a506cc65c4';

COMMENT ON ROLE uscis IS 'user for uscis tracking app';