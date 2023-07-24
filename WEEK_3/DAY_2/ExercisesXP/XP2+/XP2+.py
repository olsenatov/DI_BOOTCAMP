#Exercise_1

class Family:
    def __init__(self, members, last_name):
        self.members = members
        self.last_name = last_name
        
    def add_member(self, member_data):
        self.members.append(member_data)
        
    def born (self, **kwargs):
        new_child = {"name" : kwargs.get("name"), "age" : kwargs.get("age"), "gender" : kwargs.get("gender"), "is_child" : True}
        self.members.append(new_child)
        print(f"Congrats! {kwargs.get('name')} is born into {self.last_name} family")
        
        
    def is_18(self, name):
        for member in self.members:
            if member["name"] == name:
                return member['age'] >= 18
        return False

    def family_presentation(self):
        print(f"Family Name: {self.last_name}")
        for member in self.members:
            print(f" - {member['name']}")
 



initial_members = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False}
]

my_family = Family(initial_members, "Smith")

my_family.born(name='Emma', age = 0, gender='Female')
my_family.family_presentation()

print(my_family.is_18('Michael')) 
print(my_family.is_18('Emma'))  

#Exercise_2
class TheIncredibles(Family):
    def __init__(self, last_name):
        super().__init__(members = [], last_name = last_name)
    

                    
    def born(self, **kwargs): #name, age, gender, is_child, power, nickname
        new_child_data = {"name" : kwargs.get("name"), 
                          "age" : kwargs.get("age"), 
                          "gender" : kwargs.get("gender"), 
                          "is_child" : True, 
                          "power" : kwargs.get('power'),
                          "incredible_name" : kwargs.get("incredible_name")}
        self.add_member(new_child_data)


    def incredible_presentation(self):
        super().family_presentation()
        print("The Incredibles - Names and Powers:  ")
        for member in self.members:
            print(f" - {member['incredible_name']} : {member['power']}")
            
    def use_power(self, member_name):
        for member in self.members:
            if member['name'] == member_name:
                if member['age'] >= 18:
                    print(f"{member_name}'s power : {member['power']} is active")
                else:
                    print("Not Old enough to use the power")
    
    
initial_members_data = [
    {'name': 'Michael', 'age': 35, 'gender': 'Male', 'is_child': False, 'power': 'fly', 'incredible_name': 'MikeFly'},
    {'name': 'Sarah', 'age': 32, 'gender': 'Female', 'is_child': False, 'power': 'read minds', 'incredible_name': 'SuperWoman'}
]


incredibles_family = TheIncredibles(last_name="Incredibles")
for member_data in initial_members_data:
    incredibles_family.add_member(member_data)

incredibles_family.incredible_presentation()

baby_jack = {'name': 'Baby Jack', 'age': 0, 'gender': 'Male', 'power': 'Unknown Power', 'incredible_name' : 'BabyJack'}

incredibles_family.born(**baby_jack)

incredibles_family.use_power("Baby Jack")
incredibles_family.use_power("Michael")