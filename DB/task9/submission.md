---
stylesheet: https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/2.10.0/github-markdown.min.css
body_class: markdown-body
css: |-
  .page-break { page-break-after: always; }
  .markdown-body { font-size: 14px; }
  .markdown-body pre > code { white-space: pre-wrap; }
pdf_options:
  margins : 25mm
  printBackground: true
---
# Lab-9 Triggers:

## Details : 
- SRN : PES2UG20CS237
- Name : P K Navin Shrinivas 
- Section : D

## Question 1 : 

Commands : 
```sql
CREATE TRIGGER before_insert_comp BEFORE INSERT ON COMPARTMENT FOR EACH ROW BEGIN DECLARE error_msg varchar(256);DECLARE cnt int;
     set
       error_msg = "4 compartment already exist for the given train, cant add more";
     SET
       cnt = (
         SELECT
           count(*)
         FROM
           COMPARTMENT
         where
           train_no = new.train_no
       );IF cnt >= 4 THEN SIGNAL SQLSTATE '45000'
     SET
       MESSAGE_TEXT = error_msg;END IF;END;$$
insert into COMPARTMENT values ("I class", 16, 6, 62621, "A12");
```

Screenshots : 
![image](./1_1.png)
![image](./1_2.png)

## Question 2 : 

Command : 
```sql
CREATE TRIGGER after_delete_ticket BEFORE DELETE ON PAYMENT_INFO FOR EACH ROW BEGIN
INSERT INTO
  BACKUP_PAYMENTS
SELECT
  *
FROM
  PAYMENT_INFO
WHERE
  pnr = old.pnr;END;$$
```

Screenshots : 
![image](./2_2.png)
