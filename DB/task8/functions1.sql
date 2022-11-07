use railways;

DROP FUNCTION IF EXISTS ticket_limit;

DELIMITER $$

CREATE function ticket_limit(userid varchar(20), today date) RETURNS varchar(50) BEGIN DECLARE cnt int;DECLARE msg varchar(50);
set
  cnt = (
    SELECT
      count(*)
    from
      TICKET
    where
      TICKET.user_id = userid
      AND TIMESTAMPDIFF(MONTH, today, TICKET.travel_date) = 0
  );IF cnt = 0 THEN
set
  msg = 'cannot purchase ticker current limit is over';ELSE
set
  msg = 'below limit, can purshase tickets';END IF;RETURN msg;END;$$

SELECT user_id,ticket_limit(TICKET.user_id,"2021-10-22") FROM TICKET;$$
