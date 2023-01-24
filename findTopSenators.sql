select senator, senator_id, count(*) as purchases
from transactions 
where type='Purchase'
group by senator, senator_id
having count(*) > 2
order by purchases desc ; 