select name, min(food1) as minimum,  avg(food1) as average, max(food1) as maximum
from mydb.foodratings
group by name;
