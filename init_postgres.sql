CREATE TABLE IF NOT EXISTS public_table
(
    id     SERIAL PRIMARY KEY,
    name   TEXT,
    amount NUMERIC(7,2),
    period INTEGER
);

TRUNCATE public_table;

INSERT INTO public_table (name, amount, period)
VALUES ('Foo Bar', 5000.0, 10),
       ('Spongebob Square Pants', 15000.0, 6),
       ('Patrick The Star', 500.0, 3);

CREATE SCHEMA IF NOT EXISTS non_public;

CREATE TABLE IF NOT EXISTS non_public.non_public_table
(
    id          SERIAL PRIMARY KEY,
    external_id TEXT,
    result      TEXT
);

TRUNCATE non_public.non_public_table;

INSERT INTO non_public.non_public_table (external_id, result)
VALUES ('acca406a-0f87-4ef8-b5f8-3e4917563588', 'approved'),
       ('b0dbe45f-45c9-4ae4-80ea-79133b9e54fd', 'approved'),
       ('cf2d7c5e-36c7-4385-b8bf-e9b8266525d0', 'denied');
