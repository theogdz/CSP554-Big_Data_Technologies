INSERT OVERWRITE TABLE foodratingspart
PARTITION (name)
SELECT food1, food2, food3, food4, id, name
FROM foodratings;

select name, min(foodratingspart.food2) as minimum, avg(foodratingspart.food2) as average, max(foodratingspart .food2) as maximum
from foodratingspart
 where name = "Mel" or name = "Jill"
 group by name;
