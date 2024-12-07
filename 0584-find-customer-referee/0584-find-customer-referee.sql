/* Write your T-SQL query statement below */
SELECT name FROM Customer
WHERE coalesce(referee_id,0)<>2