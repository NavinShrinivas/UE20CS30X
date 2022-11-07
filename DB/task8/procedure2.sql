use railways;

DELIMITER $$

CREATE procedure generate_age(IN dob date, IN userid varchar(20)) BEGIN
UPDATE
  USER
SET
  age = FLOOR(DATEDIFF(NOW(), dob) / 365)
WHERE
  user_id = userid;END;$$

UPDATE USER SET age=NULL;$$
CALL generate_age("1989-04-14", "ADM_001");$$
SELECT * FROM USER WHERE user_id="ADM_001";$$
