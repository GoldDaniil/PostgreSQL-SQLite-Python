CREATE OR REPLACE FUNCTION login_user(username VARCHAR, password VARCHAR)
RETURNS TEXT AS $$
DECLARE
    stored_password TEXT;
BEGIN
    SELECT password_hash INTO stored_password
    FROM users
    WHERE username = username;

    IF NOT FOUND THEN
        RETURN 'error';
    END IF;

    IF stored_password = crypt(password, stored_password) THEN
        RETURN 'log ++';
    ELSE
        RETURN 'error enter';
    END IF;
END;
$$ LANGUAGE plpgsql;
