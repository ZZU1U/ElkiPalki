from .models import User, Animal, Role


animals = [
    {'name': 'Jack', 'species': 'Dog', 'age': 5, 'description': 'nice dog', 'image': 'https://pettownsendvet.com/wp-content/uploads/2023/01/iStock-1052880600-1024x683.jpg'},
    {'name': 'Whiskers', 'species': 'Cat', 'age': 3, 'description': 'playful kitty', 'image': 'https://wallpapercrafter.com/desktop/293518-cat-pet-striped-kitten-young-white-background.jpg'},
    {'name': 'Buddy', 'species': 'Dog', 'age': 7, 'description': 'friendly companion'},
    {'name': 'Mittens', 'species': 'Cat', 'age': 1, 'description': 'curious kitten'},
    {'name': 'Sammy', 'species': 'Hamster', 'age': 2, 'description': 'quick little guy'},
    {'name': 'Luna', 'species': 'Rabbit', 'age': 4, 'description': 'gentle giant'},
    {'name': 'Rocky', 'species': 'Dog', 'age': 9, 'description': 'energetic runner'},
    {'name': 'Snowball', 'species': 'Rabbit', 'age': 6, 'description': 'fluffy friend'},
    {'name': 'Tiger', 'species': 'Cat', 'age': 8, 'description': 'sassy feline'},
    {'name': 'Daisy', 'species': 'Guinea Pig', 'age': 3, 'description': 'social butterfly'},
    {'name': 'Baxter', 'species': 'Dog', 'age': 11, 'description': 'loyal companion'},
    {'name': 'Coco', 'species': 'Hamster', 'age': 1, 'description': 'tiny but mighty'},
    {'name': 'Finn', 'species': 'Rabbit', 'age': 5, 'description': 'hoppy guy'},
    {'name': 'Lola', 'species': 'Cat', 'age': 6, 'description': 'sassy kitty'},
    {'name': 'Max', 'species': 'Dog', 'age': 10, 'description': 'active adventurer'},
    {'name': 'Oliver', 'species': 'Guinea Pig', 'age': 4, 'description': 'gentle soul'},
    {'name': 'Penny', 'species': 'Hamster', 'age': 2, 'description': 'quick and quiet'},
    {'name': 'Rufus', 'species': 'Dog', 'age': 8, 'description': 'happy-go-lucky'},
    {'name': 'Sasha', 'species': 'Cat', 'age': 9, 'description': 'regal feline', 'image': ''},
    {'name': 'Toby', 'species': 'Rabbit', 'age': 7, 'description': 'friendly fellow', 'image': 'https://cdn.britannica.com/20/194520-050-DCAE62F1/New-World-Sylvilagus-cottontail-rabbits.jpg'},
]

users = [
    {'name': 'NOTANADMIN', 'role': Role.admin},
    {'name': 'ADMIN', 'role': Role.user},
    {'name': 'volunteer', 'role': Role.volunteer},
]


async def test():
    for animal in map(lambda a: Animal(**a), animals):
        await Animal.add(animal)
    for user in users:
        await User.add(User(**user))
