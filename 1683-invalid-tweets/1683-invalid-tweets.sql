/* Write your T-SQL query statement below */
Select tweet_id
from Tweets
where len(content)>15