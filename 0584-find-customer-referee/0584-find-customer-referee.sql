/* Write your T-SQL query statement below */
SELECT name FROM Customer
WHERE isnull(referee_id,0)<>2