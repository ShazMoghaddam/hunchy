"""Cars & Motorbikes: where the makers come from, and the stories behind them."""

import random

from . import Category, wiki

c = Category("cars")

# Where each maker comes from: (brand, country, wrong answers, fact, Wikipedia page, difficulty)
ORIGINS = [
    ("Lamborghini", "Italy", ["Germany", "Spain", "France"], "Ferruccio Lamborghini made tractors before he made supercars.", "Lamborghini", 1),
    ("Porsche", "Germany", ["Austria", "Italy", "Switzerland"], "Porsche is based in Stuttgart. Ferdinand Porsche also designed the original Volkswagen Beetle.", "Porsche", 1),
    ("BMW", "Germany", ["Austria", "Switzerland", "The Netherlands"], "BMW stands for Bayerische Motoren Werke: Bavarian Motor Works. It's based in Munich.", "BMW", 1),
    ("Audi", "Germany", ["Austria", "Italy", "Belgium"], "Audi's four rings stand for four car makers that joined together in 1932 as Auto Union.", "Audi", 1),
    ("Rolls-Royce", "The United Kingdom", ["Germany", "The United States", "Italy"], "Its cars are built at Goodwood in West Sussex, though the company is now owned by BMW.", "Rolls-Royce Motor Cars", 1),
    ("Aston Martin", "The United Kingdom", ["Italy", "Germany", "The United States"], "Aston Martin is James Bond's car of choice, starting with the DB5 in Goldfinger in 1964.", "Aston Martin", 2),
    ("Jaguar", "The United Kingdom", ["The United States", "Italy", "Sweden"], "Jaguar began in Blackpool in 1922 making motorbike sidecars, as the Swallow Sidecar Company.", "Jaguar Cars", 2),
    ("McLaren", "The United Kingdom", ["New Zealand", "Italy", "Germany"], "McLaren is based in Woking, Surrey. Its founder, Bruce McLaren, was a racing driver from New Zealand.", "McLaren Automotive", 2),
    ("Lotus", "The United Kingdom", ["Japan", "Italy", "Sweden"], "Lotus is based at Hethel in Norfolk. Its founder Colin Chapman's motto was 'simplify, then add lightness'.", "Lotus Cars", 3),
    ("Koenigsegg", "Sweden", ["Norway", "Germany", "Finland"], "Christian von Koenigsegg started the company at the age of 22, in 1994.", "Koenigsegg", 3),
    ("Škoda", "Czechia", ["Poland", "Slovakia", "Hungary"], "Škoda began in 1895 as Laurin & Klement, making bicycles.", "Škoda Auto", 2),
    ("SEAT", "Spain", ["Italy", "Portugal", "France"], "SEAT is based near Barcelona. The name stands for Sociedad Española de Automóviles de Turismo.", "SEAT", 2),
    ("Renault", "France", ["Belgium", "Italy", "Spain"], "Renault was founded by three brothers, Louis, Marcel and Fernand Renault, in 1899.", "Renault", 1),
    ("Peugeot", "France", ["Italy", "Belgium", "Switzerland"], "Long before cars, Peugeot made pepper mills, and it still does.", "Peugeot", 1),
    ("Citroën", "France", ["Belgium", "Italy", "Spain"], "André Citroën brought mass production to Europe's car industry in 1919.", "Citroën", 2),
    ("Fiat", "Italy", ["Spain", "France", "Portugal"], "FIAT stands for Fabbrica Italiana Automobili Torino: the Italian car factory of Turin.", "Fiat", 1),
    ("Alfa Romeo", "Italy", ["Spain", "Argentina", "France"], "Alfa Romeo won the very first Formula One world championship race, at Silverstone in 1950.", "Alfa Romeo", 2),
    ("Maserati", "Italy", ["France", "Spain", "Germany"], "Maserati's trident badge comes from the statue of Neptune in Bologna, where the company began.", "Maserati", 2),
    ("Honda", "Japan", ["South Korea", "China", "Taiwan"], "Soichiro Honda's company began by fitting small engines to bicycles after the Second World War.", "Honda", 1),
    ("Nissan", "Japan", ["South Korea", "China", "Thailand"], "The Nissan Leaf, launched in 2010, was one of the first mass-market electric cars.", "Nissan", 1),
    ("Subaru", "Japan", ["South Korea", "China", "Sweden"], "Subaru's badge shows the Pleiades star cluster, which is called Subaru in Japanese.", "Subaru", 2),
    ("Hyundai", "South Korea", ["Japan", "China", "Vietnam"], "Hyundai means 'modern' in Korean.", "Hyundai Motor Company", 2),
    ("Kia", "South Korea", ["Japan", "China", "India"], "Kia started out making steel tubing and bicycle parts in 1944.", "Kia", 2),
    ("BYD", "China", ["Japan", "South Korea", "Taiwan"], "BYD started out making batteries and became one of the world's biggest makers of electric cars.", "BYD Auto", 3),
    ("Ford", "The United States", ["The United Kingdom", "Canada", "Germany"], "Henry Ford's moving assembly line, started in 1913, made cars affordable for millions.", "Ford Motor Company", 1),
    ("Jeep", "The United States", ["Canada", "The United Kingdom", "Australia"], "The Jeep began as a small, tough vehicle for the US Army in the Second World War.", "Jeep", 2),
    ("Ducati", "Italy", ["Spain", "Germany", "Japan"], "Ducati is based in Bologna. It started in 1926 making radio parts.", "Ducati", 1),
    ("Harley-Davidson", "The United States", ["Canada", "The United Kingdom", "Germany"], "William Harley and Arthur Davidson built their first motorbike in a shed in Milwaukee in 1903.", "Harley-Davidson", 1),
    ("Triumph motorcycles", "The United Kingdom", ["The United States", "Italy", "Germany"], "Triumph is based in Hinckley, Leicestershire, and is Britain's biggest motorbike maker.", "Triumph Motorcycles Ltd", 2),
    ("Kawasaki", "Japan", ["South Korea", "China", "Taiwan"], "Kawasaki also builds ships, trains and aircraft parts.", "Kawasaki Motors", 2),
    ("KTM", "Austria", ["Germany", "Switzerland", "Czechia"], "KTM's orange bikes have won the Dakar Rally many times.", "KTM", 3),
    ("Vespa scooters", "Italy", ["France", "Spain", "Japan"], "Vespa means 'wasp' in Italian, after the buzzing sound and the scooter's shape.", "Vespa", 2),
    ("Aprilia", "Italy", ["Spain", "Japan", "Austria"], "Aprilia started out making bicycles after the Second World War.", "Aprilia", 3),
]
TURNED = ["Which of these brands comes from {}?", "Which of these makers is based in {}?",
          "Which of these was founded in {}?", "Which of these companies started in {}?"]
for i, (brand, country, wrong, fact, page, level) in enumerate(ORIGINS):
    if i % 3 == 2:
        # Every third question is turned round: name the country, pick the brand
        others = [b for b, cn, *_ in ORIGINS if cn != country]
        decoys = random.Random(i).sample(others, 3)  # seeded, so the same every time
        place = "the " + country[4:] if country.startswith("The ") else country
        asked = [q["prompt"] for q in c.questions]
        prompt = next(t.format(place) for t in TURNED if t.format(place) not in asked)
        c.choice(prompt, brand, decoys, fact, wiki(page), difficulty=level)
    else:
        c.choice(f"Which country does {brand} come from?", country, wrong, fact, wiki(page), difficulty=level)

# Stories and firsts
c.choice("Who built what is usually called the first true car, in 1885 to 1886?", "Karl Benz", ["Henry Ford", "Gottlieb Daimler", "Enzo Ferrari"],
         "Karl Benz's three-wheeled Patent-Motorwagen was patented in January 1886. His wife Bertha took it on the first long drive.",
         wiki("Benz Patent-Motorwagen"), era="classic", difficulty=2)
c.choice("Which car did Henry Ford say you could have 'in any colour, so long as it is black'?", "The Model T", ["The Mustang", "The Thunderbird", "The Model A"],
         "Black paint dried fastest, which helped the assembly line move quickly.",
         wiki("Ford Model T"), era="classic", difficulty=2)
c.yes_no("Is the Mercedes car brand named after a girl?", True,
         "Mercedes was the daughter of Emil Jellinek, who sold Daimler cars and raced them under her name.",
         wiki("Mercedes-Benz"), difficulty=2)
c.yes_no("Is BMW's round blue and white badge officially meant to show a spinning propeller?", False,
         "BMW says the blue and white come from the flag of Bavaria. The propeller idea came from an advert in 1929.",
         wiki("BMW"), difficulty=3)
c.choice("Which car maker's badge is a charging bull?", "Lamborghini", ["Ferrari", "Maserati", "Pagani"],
         "Ferruccio Lamborghini's star sign was Taurus, the bull, and many of his cars are named after fighting bulls.",
         wiki("Lamborghini"), difficulty=1)
c.choice("What is the name of the winged lady on the bonnet of a Rolls-Royce?", "The Spirit of Ecstasy", ["The Flying Lady of Speed", "Victory", "The Silver Angel"],
         "The sculptor Charles Sykes designed her in 1911.",
         wiki("Spirit of Ecstasy"), era="classic", difficulty=3)
c.choice("Which car, launched in 1966, has become the best-selling car name of all time?", "The Toyota Corolla", ["The Volkswagen Golf", "The Ford Fiesta", "The Honda Civic"],
         "More than 50 million Corollas have been sold around the world.",
         wiki("Toyota Corolla"), difficulty=3, as_of="2026-11")
c.yes_no("The Porsche 911 was first shown in 1963. Is it still being made today?", True,
         "The 911 has been made for more than 60 years, though every part has changed many times.",
         wiki("Porsche 911"), difficulty=2, as_of="2026-11")
c.choice("In which US city is the famous Indianapolis 500 race held?", "Indianapolis", ["Detroit", "Daytona", "Le Mans"],
         "It's been run at the Indianapolis Motor Speedway since 1911. The winner drinks a bottle of milk.",
         wiki("Indianapolis 500"), difficulty=1)
c.choice("Le Mans in France is famous for a race lasting how long?", "24 hours", ["12 hours", "6 hours", "48 hours"],
         "Teams of drivers take turns through the day and night. The first race was in 1923.",
         wiki("24 Hours of Le Mans"), difficulty=1)
c.yes_no("Is a Formula One car allowed to refuel during a race today?", False,
         "Refuelling during races has been banned since 2010. Cars start with all the fuel they need.",
         wiki("Formula One regulations"), era="modern", difficulty=3)
c.choice("Which country does the Formula One team Red Bull Racing's parent company come from?", "Austria", ["Germany", "The United Kingdom", "Switzerland"],
         "Red Bull is an Austrian company, though the team itself is based in Milton Keynes, England.",
         wiki("Red Bull Racing"), era="modern", difficulty=3)
