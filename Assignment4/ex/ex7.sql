select foodplaces.place as foodplace, avg(foodratings.food2) as average
from foodratings join foodplaces on foodratings.id = foodplaces.id
 where foodplaces.place = "Soup Bowl"
 group by place;
