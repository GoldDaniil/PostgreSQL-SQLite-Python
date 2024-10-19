CREATE DATABASE fibonacci_db;
\c fibonacci_db;

CREATE TABLE numbers (
    id SERIAL PRIMARY KEY,
    num INTEGER,
    description TEXT
);

CREATE INDEX num_hash_idx ON numbers USING hash (num);



INSERT INTO numbers (num, description)
SELECT (RANDOM() * 1000)::INTEGER, 'random number'
FROM generate_series(1, 20);



CREATE OR REPLACE FUNCTION fibonacci(n INTEGER)
RETURNS SETOF INTEGER AS $$
DECLARE
    a INTEGER := 0;
    b INTEGER := 1;
    temp INTEGER;
BEGIN
    IF n <= 0 THEN
        RETURN NEXT 0;
        RETURN;
    ELSIF n = 1 THEN
        RETURN NEXT 1;
        RETURN;
    END IF;
    
    FOR i IN 1..n LOOP
        RETURN NEXT a;
        temp := a;
        a := b;
        b := temp + b;
    END LOOP;
END;
$$ LANGUAGE plpgsql;



WITH fib_sequence AS (
    SELECT fibonacci(num) AS fib_num
    FROM generate_series(1, 10)
)
SELECT n.id, n.num, n.description
FROM numbers n
JOIN fib_sequence f
ON n.num = f.fib_num
ORDER BY f.fib_num;
