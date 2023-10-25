CREATE TABLE IF NOT EXISTS disbursals
(
    id     UUID PRIMARY KEY,
    name   TEXT,
    street_name TEXT,
    period INTEGER,
    amount numeric(7,2)
);

TRUNCATE disbursals;

INSERT INTO disbursals (id, name, street_name, period, amount)
VALUES ('6b645cc2-09df-46e5-b8e1-fa99061ec0ac', 'Foo Bar', 'Rua 1', 10, 3390.90),
       ('bff143e2-cbb2-4039-92b0-29733709a2e9', 'Spongebob Square Pants', 'Rua 2', 6, 15000.0),
       ('ad97a9bf-9224-4f48-9cd7-3e9272fbd10b', 'Patrick The Star', 'Rua 3', 3, 500.0);
