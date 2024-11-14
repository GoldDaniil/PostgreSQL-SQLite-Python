CREATE EXTENSION IF NOT EXISTS pgcrypto;

CREATE OR REPLACE FUNCTION register_user(username VARCHAR, password VARCHAR)
RETURNS TEXT AS $$
DECLARE
    hashed_password TEXT;
BEGIN
    hashed_password := crypt(password, gen_salt('bf'));

    IF EXISTS (SELECT 1 FROM users WHERE username = username) THEN
        RETURN 'user --';
    END IF;

    INSERT INTO users (username, password_hash)
    VALUES (username, hashed_password);

    RETURN 'user ++ ';
END;
$$ LANGUAGE plpgsql;
