#!/usr/bin/env python3
"""
Flask-SQLAlchemy CRUD Operations Demo
This script demonstrates the key CRUD operations covered in the lesson.
"""

from app import app
from models import db, Pet
from sqlalchemy import func

def demo_crud_operations():
    """Demonstrate CRUD operations with Flask-SQLAlchemy"""
    
    with app.app_context():
        print("=== Flask-SQLAlchemy CRUD Demo ===\n")
        
        # CREATE - Adding new pets
        print("1. CREATE Operations:")
        print("Creating pets...")
        
        pet1 = Pet(name="Fido", species="Dog")
        pet2 = Pet(name="Whiskers", species="Cat")
        pet3 = Pet(name="Buddy", species="Dog")
        
        db.session.add(pet1)
        db.session.add(pet2)
        db.session.add(pet3)
        db.session.commit()
        
        print(f"Added: {pet1}")
        print(f"Added: {pet2}")
        print(f"Added: {pet3}")
        print()
        
        # READ - Querying pets
        print("2. READ Operations:")
        
        # Query all pets
        all_pets = Pet.query.all()
        print(f"All pets: {all_pets}")
        
        # Query first pet
        first_pet = Pet.query.first()
        print(f"First pet: {first_pet}")
        
        # Filter by species
        cats = Pet.query.filter(Pet.species == 'Cat').all()
        print(f"All cats: {cats}")
        
        # Filter by name starting with 'F'
        f_names = Pet.query.filter(Pet.name.startswith('F')).all()
        print(f"Names starting with 'F': {f_names}")
        
        # Filter by species using filter_by
        dogs = Pet.query.filter_by(species='Dog').all()
        print(f"All dogs (using filter_by): {dogs}")
        
        # Get by primary key
        pet_by_id = db.session.get(Pet, 1)
        print(f"Pet with id=1: {pet_by_id}")
        
        # Order by species
        ordered_pets = Pet.query.order_by('species').all()
        print(f"Pets ordered by species: {ordered_pets}")
        
        # Count pets using func
        pet_count = db.session.query(func.count(Pet.id)).first()
        print(f"Total number of pets: {pet_count[0]}")
        print()
        
        # UPDATE - Modifying a pet
        print("3. UPDATE Operations:")
        pet1.name = "Fido the Mighty"
        db.session.commit()
        print(f"Updated pet1: {pet1}")
        print()
        
        # DELETE - Removing a pet
        print("4. DELETE Operations:")
        print(f"Deleting: {pet2}")
        db.session.delete(pet2)
        db.session.commit()
        
        remaining_pets = Pet.query.all()
        print(f"Remaining pets: {remaining_pets}")
        print()
        
        # Clean up - delete all remaining pets
        print("Cleaning up - deleting all pets...")
        deleted_count = Pet.query.delete()
        db.session.commit()
        print(f"Deleted {deleted_count} pets")
        
        final_pets = Pet.query.all()
        print(f"Final pet count: {len(final_pets)}")

if __name__ == "__main__":
    demo_crud_operations()