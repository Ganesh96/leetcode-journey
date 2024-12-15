-- /* Write your T-SQL query statement below */
-- select email as "Email"
-- from Person
-- group by email
-- having count(1)>1
/* Write your T-SQL query statement below */
WITH EmailCount as (
    SELECT email, count(*) as eCount from Person
    GROUP BY email
), x as (SELECT email as Email
from EmailCount where eCount > 1) 
select x.Email from x