# code to set up db
from models.location import Location
from models.location import Location
from models.trainer import Trainer

import repositories.location_repo as location_repo
import repositories.trainer_repo as trainer_repo

location_repo.delete_all()
trainer_repo.delete_all()

location1 = Location('Studio 1')
location_repo.save(location1)
location2 = Location('Studio 2')
location_repo.save(location2)
location3 = Location('Fitness Arena')
location_repo.save(location3)

trainer1 = Trainer('Zack', 'Black')
trainer_repo.save(trainer1)
trainer2 = Trainer('Kirsty', 'Whitehall')
trainer_repo.save(trainer2)
trainer3 = Trainer('Jamie', 'Gray')
trainer_repo.save(trainer3)
