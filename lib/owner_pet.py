class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)

    # get pet type property 
    @property
    def pet_type(self):
        return self._pet_type

    # validate pet type property to pet  
    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in self.PET_TYPES:
            raise Exception('Please enter a valid pet type!')
        self._pet_type = pet_type
    
    # get owner property 
    @property
    def owner(self):
        return self._owner

    # set owner property to pet 
    @owner.setter
    def owner(self, owner):
        if not (isinstance(owner, Owner) or not owner):
            raise Exception("Owner was not set. Please try again!")
        self._owner = owner
         

class Owner:
    
    def __init__(self, name):
        self.name = name

    # returns all pets that Owner owns 
    def pets(self):
         return [pet for pet in Pet.all if pet.owner == self]

    # add a pet owner 
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Pet was not set. Please try again!")
        pet.owner = self            

    # sort pets 
    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)