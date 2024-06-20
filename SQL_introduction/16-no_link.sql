-- name is not NULL

SELECT score, name FROM second_table WHERE nams IS NOT NULL AND name != '' ORDER BY score DEC;
