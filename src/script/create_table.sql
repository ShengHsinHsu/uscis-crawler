-- Table: public.case_status

-- DROP TABLE IF EXISTS public.case_status;

CREATE TABLE IF NOT EXISTS public.case_status
(
    update_date date NOT NULL,
    status text COLLATE pg_catalog."C",
    description text COLLATE pg_catalog."C",
    case_no character(13) COLLATE pg_catalog."default" NOT NULL,
    service_center character varying(3) COLLATE pg_catalog."default",
    form character varying COLLATE pg_catalog."default",
    CONSTRAINT "Primary Key" PRIMARY KEY (case_no, update_date)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.case_status
    OWNER to postgres;

GRANT ALL ON TABLE public.case_status TO postgres;

GRANT ALL ON TABLE public.case_status TO uscis;

COMMENT ON COLUMN public.case_status.update_date
    IS 'Date of the update time';

COMMENT ON COLUMN public.case_status.description
    IS 'description of the case status';

COMMENT ON COLUMN public.case_status.case_no
    IS 'case number';