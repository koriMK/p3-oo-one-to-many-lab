class Owner:
    def __init__(self, name):
        self.name = name
    
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Pet must be an instance of Pet class")
        pet.owner = self
    
    def get_sorted_pets(self):
        pets = self.pets()
        return sorted(pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Pet type must be one of: {', '.join(self.PET_TYPES)}")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        self.__class__.all.append(self)