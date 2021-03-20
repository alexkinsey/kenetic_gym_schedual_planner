# code to set up db
from models.location import Location
from models.trainer import Trainer
from models.customer import Customer

import repositories.location_repo as location_repo
import repositories.trainer_repo as trainer_repo
import repositories.customer_repo as customer_repo

location_repo.delete_all()
trainer_repo.delete_all()
customer_repo.delete_all()

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

customer1 = Customer('Shaun', 'Hodge', 'standard', '2021/01/10', 'EH5 3RU', '07596685374', 'shaun.hodge@email.com')
customer_repo.save(customer1)
customer2 = Customer('Jade', 'Breslin', 'premium', '2020/08/13', 'EH12 1SU', '07759244212', 'jade.breslin@email.com')
customer_repo.save(customer2)
customer3 = Customer('Lucy', 'Atkinson', 'premium', '2019/10/25', 'EH2 6SR', '07321844372', 'lucy.atkinson@email.com')
customer_repo.save(customer3)
customer4 = Customer('James', 'Holden', 'standard', '2019/06/13', 'EH7 9DE', '07538472658', 'james.holden@email.com')
customer_repo.save(customer4)
customer5 = Customer('Gary', 'McDonald', 'standard', '2021/01/14', 'EH15 7ST', '07695844449', 'gary.mcdonals@email.com')
customer_repo.save(customer5)