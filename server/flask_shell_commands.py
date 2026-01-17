#!/usr/bin/env python3
"""
Flask Shell Practice Commands
Copy and paste these commands into the Flask shell to practice CRUD operations.

To start the Flask shell:
$ cd server
$ pipenv run flask shell

Then copy and paste the commands below one by one.
"""

# Import necessary modules
from models import db, Pet
from sqlalchemy import func

# CREATE - Add new pets
pet1 = Pet(name="Fido", species="Dog")
pet2 = Pet(name="Whiskers", species="Cat")

# Check attributes before saving
print(f"pet1.name: {pet1.name}")
print(f"pet1.species: {pet1.species}")
print(f"pet1.id: {pet1.id}")  # Should be None

# Add to session and commit
db.session.add(pet1)
db.session.commit()

# Check id after commit
print(f"pet1.id after commit: {pet1.id}")  # Should be 1

# Add second pet
db.session.add(pet2)
db.session.commit()

# READ - Query operations
Pet.query.all()
Pet.query.first()
Pet.query.filter(Pet.species == 'Cat').all()
Pet.query.filter(Pet.name.startswith('F')).all()
Pet.query.filter_by(species='Cat').all()
Pet.query.filter_by(id=1).first()

# Get by primary key
pet = db.session.get(Pet, 1)
print(pet)

# Order by species
Pet.query.order_by('species').all()

# Count pets
db.session.query(func.count(Pet.id)).first()

# UPDATE - Modify a pet
pet1.name = "Fido the Mighty"
db.session.commit()
print(pet1)

# DELETE - Remove a pet
db.session.delete(pet1)
db.session.commit()
Pet.query.all()

# Delete all pets
Pet.query.delete()
db.session.commit()
Pet.query.all()

# Exit the shell
exit()