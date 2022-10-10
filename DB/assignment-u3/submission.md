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

# DBMS Unit-3 Assignment 

## Deatails : 

- Name : P K Navin Shrinivas
- SRN : PES2UG20CS237
- Section : D

## Question A : 

### Sub question 1 : 

Answer : 
```sql
SELECT * FROM Boxed WHERE value>150
```

### Sub question 2 : 

Answer : 
```sql
SELECT * FROM Warehouse WHERE code=warehouse_code 
FROM Boxes GROUP BY warehouse_code HAVING avg(value)>150
```

### Sub question 3:

Answer : 
```sql
SELECT * FROM (count(*) FROM Boxes GROUP BY warehouse_code) WHERE 
(SELECT capacity FROM Warehouse WHERE code=warehouse_code)<count
```

### Sub question 4 : 

Answer : 
```sql
SELECT code FROM RIGHT JOIN(Warehouse, Boxes ON Warehouse.warehouse_code=Boxes.code)
WHERE location="Chicago"
```

## Question B : 

```sql
CREATE TRIGGER trig
AFTER UPDATE on Highschooler WHEN 
new.grade>12
BEGIN
  DELETE FROM Highschooler WHERE id=new.id
END
```


