"""More questions across the other subjects: cartoons, fashion, cars and motorbikes, food, inventions, words,
nature and space. Picked for the 'I never knew that' moment."""

from . import Category, wiki

toon = Category("cartoons", prefix="cartoons4")
fash = Category("fashion", prefix="fashion4")
cars = Category("cars", prefix="cars4")
food = Category("food", prefix="food4")
tech = Category("inventions", prefix="inventions4")
words = Category("words", prefix="words4")
nature = Category("nature", prefix="nature4")
space = Category("space", prefix="space4")

# Cartoons & Animation -----------------------------------------------------------------------------
toon.choice("Who voices Shrek?", "Mike Myers", ["Eddie Murphy", "Jim Carrey", "Adam Sandler"],
            "Myers first recorded the whole part in his normal voice, then asked to redo it in a Scottish accent.",
            wiki("Shrek (character)"), difficulty=2)
toon.choice("Who voices Puss in Boots in the Shrek films?", "Antonio Banderas", ["Javier Bardem", "Enrique Iglesias", "Pedro Pascal"],
            "Puss got his own films in 2011 and 2022.",
            wiki("Puss in Boots (Shrek)"), difficulty=2)
toon.choice("In Toy Story 2, what is the name of Woody's horse?", "Bullseye", ["Trigger", "Silver", "Champion"],
            "Bullseye joined in Toy Story 2, along with Jessie the cowgirl and Stinky Pete the prospector.",
            wiki("Toy Story 2"), difficulty=2)
toon.choice("In Toy Story, what's the name of the boy who owns Woody and Buzz?", "Andy", ["Sid", "Bonnie", "Al"],
            "Sid is the toy-wrecking boy next door. Andy passes his toys on to Bonnie in Toy Story 3.",
            wiki("Toy Story"), difficulty=1)
toon.choice("Which of these Pixar films came out first?", "Monsters, Inc.", ["Finding Nemo", "The Incredibles", "Up"],
            "Monsters, Inc. (2001), then Finding Nemo (2003), The Incredibles (2004) and Up (2009).",
            wiki("List of Pixar films"), difficulty=3)
toon.choice("In which city is Pixar's Ratatouille set?", "Paris", ["Lyon", "Rome", "Marseille"],
            "Remy the rat dreams of being a chef, and secretly cooks by pulling a young man's hair.",
            wiki("Ratatouille (film)"), difficulty=1)
toon.choice("In WALL-E, what's the name of the sleek white robot WALL-E falls for?", "EVE", ["AUTO", "MO", "BB-8"],
            "AUTO is the spaceship's autopilot. BB-8 is a droid from Star Wars.",
            wiki("WALL-E"), difficulty=2)
toon.choice("In Zootopia, called Zootropolis in Britain, what animal is the police officer Judy Hopps?", "A rabbit", ["A fox", "A hare", "A mouse"],
            "Her partner, Nick Wilde, is a fox. The film won the Oscar for Best Animated Feature.",
            wiki("Zootopia"), era="modern", difficulty=1)
toon.choice("Which Studio Ghibli film has a huge furry forest spirit waiting at a bus stop?", "My Neighbour Totoro", ["Spirited Away", "Ponyo", "Kiki's Delivery Service"],
            "Totoro became Studio Ghibli's logo.",
            wiki("My Neighbor Totoro"), difficulty=2)
toon.choice("In Spirited Away, what happens to Chihiro's parents after they eat the spirits' food?", "They turn into pigs", ["They turn into frogs", "They fall asleep for 100 years", "They turn into dragons"],
            "Chihiro has to work in a bathhouse for spirits to free them.",
            wiki("Spirited Away"), difficulty=2)
toon.choice("In The Lion King, what kind of animal is Timon?", "A meerkat", ["A mongoose", "A warthog", "A lemur"],
            "Pumbaa is the warthog. Together they sing 'Hakuna Matata'.",
            wiki("Timon and Pumbaa"), difficulty=1)
toon.choice("In The Lion King, what's the name of Simba's wicked uncle?", "Scar", ["Zazu", "Rafiki", "Shenzi"],
            "Zazu is the hornbill, Rafiki the wise old monkey and Shenzi one of the hyenas.",
            wiki("Scar (The Lion King)"), difficulty=1)
toon.choice("In Aladdin, what's the name of Princess Jasmine's pet tiger?", "Rajah", ["Abu", "Iago", "Sultan"],
            "Abu is Aladdin's monkey and Iago is Jafar's parrot.",
            wiki("Aladdin (1992 Disney film)"), difficulty=2)
toon.choice("In Beauty and the Beast, what is Lumière?", "A candlestick", ["A clock", "A teapot", "A wardrobe"],
            "Cogsworth is the clock, Mrs Potts the teapot and her son Chip a teacup.",
            wiki("List of Disney's Beauty and the Beast characters"), difficulty=1)
toon.choice("In Frozen, what's the name of Kristoff's reindeer?", "Sven", ["Olaf", "Hans", "Rudolph"],
            "Olaf is the snowman and Hans is the prince who turns out to be the villain.",
            wiki("Frozen (2013 film)"), difficulty=1)
toon.choice("In Bluey, what's the name of Bluey's little sister?", "Bingo", ["Muffin", "Socks", "Chilli"],
            "Muffin and Socks are their cousins, and Chilli is their mum.",
            wiki("Bluey (2018 TV series)"), era="modern", difficulty=1)
toon.choice("Which country do the Smurfs come from?", "Belgium", ["France", "The Netherlands", "Switzerland"],
            "The Belgian artist Peyo created them in 1958. Their name in French is les Schtroumpfs.",
            wiki("The Smurfs"), difficulty=2)
toon.choice("Which Belgian comic hero travels the world with his white dog, Snowy?", "Tintin", ["Asterix", "Lucky Luke", "Spirou"],
            "Hergé created Tintin in 1929. Snowy's name in French is Milou.",
            wiki("The Adventures of Tintin"), difficulty=1)
toon.choice("In the Asterix books, where is Asterix's little village?", "Gaul", ["Britain", "Rome", "Greece"],
            "It's in what is now Brittany, in France. Obelix fell into the magic potion as a baby, so he's always strong.",
            wiki("Asterix"), difficulty=2)
toon.choice("Who created The Simpsons, naming several of the family after his own?", "Matt Groening", ["Seth MacFarlane", "Trey Parker", "Mike Judge"],
            "Groening's father was called Homer, his mother Margaret, and his sisters Lisa and Maggie.",
            wiki("Matt Groening"), difficulty=2)
toon.choice("What is Homer Simpson's job?", "Safety inspector at a nuclear power plant", ["Bus driver", "Bartender", "Police officer"],
            "He works in Sector 7G of the Springfield Nuclear Power Plant, for Mr Burns.",
            wiki("Homer Simpson"), difficulty=1)
toon.choice("What number is painted on Thomas the Tank Engine?", "1", ["4", "7", "10"],
            "Gordon is number 4. The stories began as books by the Reverend W. Awdry in 1945.",
            wiki("Thomas the Tank Engine"), difficulty=2)
toon.choice("In the 1950s BBC programme, what are Bill and Ben made of?", "Flowerpots", ["Wooden spoons", "Socks", "Pine cones"],
            "The Flower Pot Men lived at the bottom of a garden, with their friend Little Weed.",
            wiki("Flower Pot Men"), era="classic", difficulty=2)
toon.choice("What colour is the Teletubby Tinky Winky?", "Purple", ["Green", "Yellow", "Red"],
            "Dipsy is green, Laa-Laa is yellow and Po is red.",
            wiki("Teletubbies"), difficulty=2)
toon.choice("What is the name of Danger Mouse's nervous hamster sidekick?", "Penfold", ["Pinky", "Baron Greenback", "Stiletto"],
            "Baron Greenback is his toad enemy. David Jason was the voice of Danger Mouse.",
            wiki("Danger Mouse (1981 TV series)"), era="classic", difficulty=2)
toon.choice("Which Wallace & Gromit film won the Oscar for Best Animated Feature?", "The Curse of the Were-Rabbit", ["A Close Shave", "A Grand Day Out", "Vengeance Most Fowl"],
            "It won in 2006. Wallace's favourite cheese is Wensleydale.",
            wiki("Wallace & Gromit: The Curse of the Were-Rabbit"), difficulty=3)
toon.choice("Which of these is NOT one of the Teenage Mutant Ninja Turtles?", "Caravaggio", ["Donatello", "Raphael", "Leonardo"],
            "They are named after Renaissance artists. The fourth is Michelangelo.",
            wiki("Teenage Mutant Ninja Turtles"), difficulty=2)
toon.choice("What does Popeye eat to become super strong?", "Spinach", ["Broccoli", "Carrots", "Beans"],
            "Popeye first appeared in a newspaper comic strip in 1929.",
            wiki("Popeye"), era="classic", difficulty=1)
toon.choice("Which cartoon cat loves lasagne and hates Mondays?", "Garfield", ["Sylvester", "Top Cat", "Felix"],
            "Jim Davis created Garfield in 1978.",
            wiki("Garfield"), difficulty=1)
toon.choice("Which little yellow bird does Sylvester the cat keep trying to catch?", "Tweety", ["Road Runner", "Woody Woodpecker", "Daffy Duck"],
            "Sylvester's famous line is 'Sufferin' succotash!'",
            wiki("Tweety"), difficulty=1)
toon.yes_no("Did Walt Disney himself do the original voice of Mickey Mouse?", True,
            "He voiced Mickey from 1928 until 1947.",
            wiki("Mickey Mouse"), difficulty=2)
toon.higher_lower("Shrek came out in 2001. Did Shrek 2 take more or less money at cinemas?", True,
                  "More: Shrek 2 (2004) became the highest-earning animated film ever at the time.",
                  wiki("Shrek 2"), labels=("More", "Less"), difficulty=2)

# Fashion ------------------------------------------------------------------------------------------
fash.choice("Which French fashion house started out in 1837 making harnesses and saddles for horses?", "Hermès", ["Louis Vuitton", "Chanel", "Dior"],
            "That's why Hermès's logo is a horse and carriage.",
            wiki("Hermès"), difficulty=2)
fash.choice("What did Louis Vuitton first make his name with?", "Travel trunks", ["Horse saddles", "Hats", "Perfume"],
            "He opened his trunk workshop in Paris in 1854. His flat-topped trunks could be stacked, unlike the rounded ones of the time.",
            wiki("Louis Vuitton (designer)"), difficulty=2)
fash.choice("Whose fashion logo is two interlocking Gs?", "Gucci", ["Givenchy", "Guess", "Goyard"],
            "The Gs stand for Guccio Gucci, who founded the house in Florence in 1921.",
            wiki("Gucci"), difficulty=2)
fash.choice("Which designer, the daughter of a Beatle, refuses to use leather or fur?", "Stella McCartney", ["Mary McCartney", "Stella Tennant", "Victoria Beckham"],
            "Mary McCartney, her sister, is a photographer.",
            wiki("Stella McCartney"), difficulty=2)
fash.choice("Which former Spice Girl now runs her own fashion label?", "Victoria Beckham", ["Geri Halliwell", "Emma Bunton", "Melanie C"],
            "She showed her first collection at New York Fashion Week in 2008.",
            wiki("Victoria Beckham"), difficulty=1)
fash.choice("Which American designer's polo shirts have a polo player on horseback as the logo?", "Ralph Lauren", ["Tommy Hilfiger", "Calvin Klein", "Michael Kors"],
            "He was born Ralph Lifshitz, in the Bronx in New York, and started by selling ties.",
            wiki("Ralph Lauren"), difficulty=2)
fash.choice("How much was the student who designed Nike's 'swoosh' first paid, in 1971?", "35 dollars", ["350 dollars", "3,500 dollars", "35,000 dollars"],
            "Carolyn Davidson was a design student. Nike later gave her a gold ring and shares in the company.",
            wiki("Swoosh"), difficulty=3)
fash.choice("Adidas and Puma were founded by two people who fell out. Who were they?", "Two brothers", ["Two cousins", "A father and son", "Two school friends"],
            "Adi and Rudolf Dassler split up in 1948 and set up rival firms on opposite sides of the river in their German town.",
            wiki("Adidas"), difficulty=2)
fash.choice("Which brand makes the white tennis trainer called the Stan Smith?", "Adidas", ["Nike", "Puma", "Reebok"],
            "Stan Smith was an American tennis player who won Wimbledon in 1972.",
            wiki("Adidas Stan Smith"), difficulty=2)
fash.choice("Which fabric comes from the cocoons of a caterpillar?", "Silk", ["Satin", "Velvet", "Linen"],
            "The silkworm spins its cocoon from one thread up to about a kilometre long. China kept how silk was made a secret for centuries.",
            wiki("Silk"), difficulty=1)
fash.choice("Cashmere wool comes from which animal?", "Goats", ["Sheep", "Alpacas", "Rabbits"],
            "It's the soft undercoat of cashmere goats, from the mountains of Asia.",
            wiki("Cashmere wool"), difficulty=2)
fash.choice("Mohair comes from the Angora goat. Where does angora wool come from?", "The Angora rabbit", ["The Angora goat", "The Angora sheep", "The Angora cat"],
            "Confusing but true: the Angora goat gives us mohair, and the fluffy Angora rabbit gives us angora.",
            wiki("Angora wool"), difficulty=3)
fash.choice("Linen is made from which plant?", "Flax", ["Cotton", "Hemp", "Bamboo"],
            "Linen is one of the oldest fabrics. Ancient Egyptians wrapped mummies in it.",
            wiki("Linen"), difficulty=2)
fash.choice("Where are Panama hats really made?", "Ecuador", ["Panama", "Colombia", "Peru"],
            "They got the name because they were shipped through Panama, and workers building the Panama Canal wore them.",
            wiki("Panama hat"), difficulty=3)
fash.choice("What kind of hat does Indiana Jones wear?", "A fedora", ["A trilby", "A Stetson", "A bowler"],
            "A trilby has a narrower brim. Indy's hat was made by a London hatmaker, Herbert Johnson.",
            wiki("Fedora"), difficulty=2)
fash.choice("Which shoe designer's shoes have famous red soles?", "Christian Louboutin", ["Jimmy Choo", "Manolo Blahnik", "Salvatore Ferragamo"],
            "In 1993 he painted a shoe's sole with an assistant's red nail varnish, and kept it.",
            wiki("Christian Louboutin"), difficulty=2)
fash.choice("Which shoe designer, born in Malaysia, made shoes for Princess Diana?", "Jimmy Choo", ["Manolo Blahnik", "Christian Louboutin", "Patrick Cox"],
            "He studied in London and opened his first workshop in Hackney.",
            wiki("Jimmy Choo"), difficulty=3)
fash.choice("Which 1960s model was nicknamed 'The Twig'?", "Twiggy", ["Jean Shrimpton", "Kate Moss", "Naomi Campbell"],
            "Her real name is Lesley Hornby. She was named 'The Face of 1966' at 16.",
            wiki("Twiggy"), era="classic", difficulty=1)
fash.choice("Which supermodel from Croydon was spotted at a New York airport at 14?", "Kate Moss", ["Naomi Campbell", "Twiggy", "Cara Delevingne"],
            "She was discovered at JFK airport in 1988 by the founder of Storm model agency.",
            wiki("Kate Moss"), difficulty=2)
fash.choice("Anna Wintour was editor of which fashion magazine for over 35 years?", "Vogue (American edition)", ["Harper's Bazaar", "Elle", "Cosmopolitan"],
            "She took over American Vogue in 1988 and handed over the editor's job in 2025.",
            wiki("Anna Wintour"), difficulty=2)
fash.choice("Which designer invented the wrap dress in 1974?", "Diane von Fürstenberg", ["Coco Chanel", "Mary Quant", "Donna Karan"],
            "She sold millions of them within a couple of years.",
            wiki("Diane von Fürstenberg"), era="classic", difficulty=3)
fash.choice("What does 'haute couture' mean?", "High sewing", ["Expensive clothes", "Paris fashion", "Made to measure"],
            "In France, only fashion houses that meet strict rules may call their work haute couture.",
            wiki("Haute couture"), difficulty=3)
fash.higher_lower("Was Chanel No. 5 perfume launched before or after 1930?", True,
                  "Before: Coco Chanel launched it in 1921. The number is said to be because she chose the fifth sample.",
                  wiki("Chanel No. 5"), labels=("Before", "After"), difficulty=2)

# Cars & Motorbikes --------------------------------------------------------------------------------
cars.choice("Which car maker's badge is a prancing horse?", "Ferrari", ["Porsche", "Lamborghini", "Maserati"],
            "Careful: Porsche has a horse too, from the coat of arms of Stuttgart. Ferrari's came from a First World War fighter pilot's plane.",
            wiki("Ferrari"), difficulty=1)
cars.choice("Which car maker's name is Latin for 'listen'?", "Audi", ["Volvo", "Lexus", "Acura"],
            "Its founder was August Horch, and Horch means 'listen' in German. Volvo is Latin too: it means 'I roll'.",
            wiki("Audi"), difficulty=3)
cars.choice("What does BMW stand for?", "Bavarian Motor Works", ["British Motor Works", "Berlin Motor Works", "Bavarian Metal Workshop"],
            "In German it's Bayerische Motoren Werke. BMW made aircraft engines before it made cars.",
            wiki("BMW"), difficulty=2)
cars.choice("Which car maker's name means 'three diamonds' in Japanese?", "Mitsubishi", ["Subaru", "Mazda", "Daihatsu"],
            "The three diamonds in its badge come from the family crests of the founder and his first employer.",
            wiki("Mitsubishi"), difficulty=2)
cars.choice("Which Italian car maker's badge is a trident?", "Maserati", ["Alfa Romeo", "Lamborghini", "Ferrari"],
            "It's based on the statue of Neptune in Bologna, the city where the Maserati brothers started out.",
            wiki("Maserati"), difficulty=2)
cars.choice("What kind of car is Herbie, in The Love Bug films?", "A Volkswagen Beetle", ["A Mini", "A Fiat 500", "A Citroën 2CV"],
            "Herbie wears the racing number 53.",
            wiki("Herbie"), era="classic", difficulty=1)
cars.choice("Where was the DeLorean, the time machine in Back to the Future, built?", "Northern Ireland", ["Detroit", "Italy", "Japan"],
            "It was made in a factory in Dunmurry, near Belfast, in 1981 and 1982, with gull-wing doors and a steel body.",
            wiki("DMC DeLorean"), difficulty=3)
cars.choice("Which car did Sean Connery's Bond drive in Goldfinger (1964)?", "An Aston Martin DB5", ["A Jaguar E-Type", "A Lotus Esprit", "A Bentley Continental"],
            "It came with an ejector seat and machine guns. The Lotus Esprit turned into a submarine in The Spy Who Loved Me.",
            wiki("Aston Martin DB5"), era="classic", difficulty=2)
cars.choice("The first Land Rover was sketched in 1947 in a surprising place. Where?", "In the sand on a beach in Anglesey", ["On a napkin in a pub", "On a factory wall", "On the back of a cigarette packet"],
            "Maurice Wilks drew it on the beach at Red Wharf Bay to show his brother the idea.",
            wiki("Land Rover Series"), difficulty=3)
cars.choice("Which car maker invented the modern three-point seatbelt, then let every other car maker use it for free?", "Volvo", ["Mercedes-Benz", "Saab", "Ford"],
            "Nils Bohlin designed it in 1959. Volvo gave away the patent to save lives.",
            wiki("Nils Bohlin"), difficulty=2)
cars.choice("Which Swedish car maker started out building aircraft?", "Saab", ["Volvo", "Koenigsegg", "Scania"],
            "Saab stands for Svenska Aeroplan AB, the Swedish Aeroplane Company.",
            wiki("Saab Automobile"), difficulty=2)
cars.choice("What did Ferruccio Lamborghini make before his supercars?", "Tractors", ["Fridges", "Motorbikes", "Aeroplanes"],
            "The story goes that he started making cars after Enzo Ferrari brushed off his complaints about his Ferrari's clutch.",
            wiki("Ferruccio Lamborghini"), difficulty=2)
cars.choice("Enzo Ferrari raced for which team before starting his own company?", "Alfa Romeo", ["Maserati", "Fiat", "Lancia"],
            "He ran Alfa Romeo's racing team in the 1930s, before founding Ferrari.",
            wiki("Enzo Ferrari"), difficulty=3)
cars.yes_no("Are Rolls-Royce cars and Rolls-Royce jet engines made by the same company?", False,
            "They split in the 1970s. The cars are now made by BMW at Goodwood, and the engines by Rolls-Royce Holdings.",
            wiki("Rolls-Royce Motor Cars"), difficulty=3)
cars.choice("Which car group owns Bentley?", "Volkswagen", ["BMW", "Mercedes-Benz", "Tata"],
            "BMW owns Rolls-Royce cars, and Tata owns Jaguar Land Rover.",
            wiki("Bentley"), difficulty=3, as_of="2026")
cars.choice("Which was the first mass-produced hybrid car?", "The Toyota Prius", ["The Honda Insight", "The Tesla Roadster", "The Nissan Leaf"],
            "The Prius went on sale in Japan in 1997. The name is Latin for 'before'.",
            wiki("Toyota Prius"), era="modern", difficulty=2)
cars.choice("What does SUV stand for?", "Sport utility vehicle", ["Super urban vehicle", "Safe utility van", "Standard utility vehicle"],
            "SUVs now make up nearly half of all new cars sold around the world.",
            wiki("Sport utility vehicle"), era="modern", difficulty=1)
cars.choice("Which car made history in 2019 by going over 300 miles an hour?", "A Bugatti Chiron", ["A Koenigsegg Agera RS", "A McLaren Speedtail", "A Hennessey Venom F5"],
            "It reached 304.77 mph on a test track in Germany, with the racing driver Andy Wallace at the wheel.",
            wiki("Bugatti Chiron"), era="modern", difficulty=3)
cars.choice("How many wheels does a Reliant Robin have?", "3", ["4", "2", "6"],
            "With one wheel at the front, it was famous for tipping over on corners.",
            wiki("Reliant Robin"), difficulty=1)
cars.choice("Which international code goes on cars from Germany?", "D", ["G", "DE", "GE"],
            "D is for Deutschland. Spain uses E, for España.",
            wiki("International vehicle registration code"), difficulty=2)
cars.choice("What is the international car code for Switzerland?", "CH", ["SW", "SZ", "S"],
            "It stands for Confoederatio Helvetica, the Latin name for Switzerland. S is Sweden.",
            wiki("International vehicle registration code"), difficulty=2)
cars.choice("Which tyre maker's mascot is a man made of tyres, called Bibendum?", "Michelin", ["Pirelli", "Dunlop", "Goodyear"],
            "He was created in 1898, which makes him one of the oldest trademarks in the world.",
            wiki("Michelin Man"), difficulty=1)
cars.choice("Which Scottish vet made the first practical air-filled tyre in 1888, for his son's tricycle?", "John Boyd Dunlop", ["Charles Goodyear", "André Michelin", "Harvey Firestone"],
            "Another Scot, Robert William Thomson, had patented the idea in 1845, but it never caught on.",
            wiki("John Boyd Dunlop"), difficulty=3)
cars.choice("Which Italian motorbike maker makes a model called the Monster?", "Ducati", ["Aprilia", "MV Agusta", "Moto Guzzi"],
            "The Monster was first shown in 1992, designed by Miguel Galluzzi, and made naked bikes popular.",
            wiki("Ducati Monster"), difficulty=2)
cars.choice("Ducati engines use 'desmodromic' valves. What's special about them?", "They are closed by a cam, not a spring", ["They are made of glass", "They spin instead of opening", "They open by air pressure"],
            "Ducati calls it 'Desmo' for short, and has used it since the 1950s. It lets the engine rev very high without valves floating.",
            wiki("Desmodromic valve"), difficulty=3)
cars.choice("Which British motorbike maker builds the Bonneville?", "Triumph", ["Norton", "BSA", "Royal Enfield"],
            "It's named after the Bonneville Salt Flats in Utah, where Triumph-powered bikes set speed records.",
            wiki("Triumph Bonneville"), difficulty=2)
cars.choice("Royal Enfield, the oldest motorbike brand still making bikes, began in England. Where are its bikes made today?", "India", ["China", "Thailand", "England"],
            "Royal Enfield's Bullet has been made in India since the 1950s.",
            wiki("Royal Enfield"), difficulty=3)
cars.choice("Vespa means 'wasp' in Italian. What is Piaggio's three-wheeled van called?", "Ape, which means 'bee'", ["Mosca, which means 'fly'", "Formica, which means 'ant'", "Zanzara, which means 'mosquito'"],
            "Piaggio makes both. The Vespa was named for its buzzing sound and narrow waist.",
            wiki("Piaggio Ape"), difficulty=3)
cars.choice("What does TT stand for in the Isle of Man TT motorbike races?", "Tourist Trophy", ["Time Trial", "Twin Track", "Top Throttle"],
            "The races began in 1907 and run on ordinary island roads, closed for the event.",
            wiki("Isle of Man TT"), difficulty=2)
cars.higher_lower("Could the original 1959 Mini go faster or slower than 100 miles an hour?", False,
                  "Slower: the first Mini topped out at about 72 mph. The later Mini Cooper S could reach nearly 100.",
                  wiki("Mini"), labels=("Faster", "Slower"), era="classic", difficulty=2)

# Food & Drink -------------------------------------------------------------------------------------
food.choice("Why did the tyre company Michelin start its famous guide in 1900?", "To get people driving more", ["To sell tyres to restaurants", "To rate hotels for the army", "To win a bet"],
            "More trips meant more worn-out tyres. The guide first gave restaurants stars in the 1920s.",
            wiki("Michelin Guide"), difficulty=2)
food.choice("What is the highest number of stars the Michelin Guide gives a restaurant?", "3", ["5", "4", "10"],
            "Three stars means 'exceptional cuisine, worth a special journey'.",
            wiki("Michelin Guide"), difficulty=2)
food.choice("Which country is feta cheese from?", "Greece", ["Turkey", "Cyprus", "Bulgaria"],
            "Since 2002, only cheese made in parts of Greece may be called feta in the European Union.",
            wiki("Feta"), difficulty=1)
food.choice("Which country is halloumi from?", "Cyprus", ["Greece", "Turkey", "Lebanon"],
            "It's squeaky because of its tight, stretchy texture, and it doesn't melt when grilled.",
            wiki("Halloumi"), difficulty=2)
food.choice("Stilton can only be made in three English counties. Which village can't make it, despite the name?", "Stilton", ["Melton Mowbray", "Colston Bassett", "Hartington"],
            "Stilton is in Cambridgeshire, outside the three counties allowed: Derbyshire, Leicestershire and Nottinghamshire.",
            wiki("Stilton cheese"), difficulty=3)
food.choice("Which Italian cheese is named after the city of Parma?", "Parmigiano-Reggiano", ["Grana Padano", "Pecorino Romano", "Asiago"],
            "It's aged for at least 12 months. Grana Padano is a similar cheese, made in a bigger area.",
            wiki("Parmigiano Reggiano"), difficulty=1)
food.choice("Which country is kimchi from?", "Korea", ["Japan", "China", "Thailand"],
            "Kimchi is usually fermented cabbage with chilli. It's served with almost every Korean meal.",
            wiki("Kimchi"), difficulty=1)
food.choice("Which country does the noodle soup pho come from?", "Vietnam", ["Thailand", "Laos", "Cambodia"],
            "It's usually made with beef or chicken, rice noodles and fresh herbs.",
            wiki("Pho"), difficulty=2)
food.choice("What are the main ingredients of a Spanish tortilla?", "Potatoes and eggs", ["Flour and water", "Corn and beans", "Rice and chicken"],
            "Don't mix it up with a Mexican tortilla, which is a flat bread made of maize or wheat.",
            wiki("Spanish omelette"), difficulty=2)
food.choice("What kind of fruit is a Granny Smith?", "An apple", ["A pear", "A plum", "A grape"],
            "The first one grew in Australia in 1868, from a seedling found by Maria Ann Smith.",
            wiki("Granny Smith"), difficulty=1)
food.true_false("Bananas are very slightly radioactive.", True,
                "They contain potassium, and a tiny part of all potassium is radioactive. You'd need to eat millions at once to be harmed.",
                wiki("Banana equivalent dose"), difficulty=2)
food.yes_no("Is a tomato a fruit?", True,
            "To a botanist, yes, because it grows from a flower and holds seeds. Cooks treat it as a vegetable.",
            wiki("Tomato"), difficulty=1)
food.choice("Which country grows the most coffee?", "Brazil", ["Colombia", "Vietnam", "Ethiopia"],
            "Brazil grows around a third of the world's coffee. Vietnam is second.",
            wiki("List of countries by coffee production"), difficulty=2, as_of="2026")
food.choice("Which country grows the most tea?", "China", ["India", "Kenya", "Sri Lanka"],
            "China grows around half of the world's tea. India is second.",
            wiki("List of countries by tea production"), difficulty=2, as_of="2026")
food.choice("What gives Earl Grey tea its flavour?", "Bergamot orange", ["Lemon", "Lavender", "Vanilla"],
            "It's named after Earl Grey, the British prime minister in the 1830s.",
            wiki("Earl Grey tea"), difficulty=2)
food.choice("Which spice gives most curries their yellow colour?", "Turmeric", ["Saffron", "Paprika", "Cumin"],
            "Saffron colours food yellow too, but it's far more expensive.",
            wiki("Turmeric"), difficulty=1)
food.choice("Which spice is the bark of a tree?", "Cinnamon", ["Nutmeg", "Cloves", "Black pepper"],
            "The inner bark is peeled off and curls up as it dries, making cinnamon sticks.",
            wiki("Cinnamon"), difficulty=2)
food.choice("What are cloves?", "Dried flower buds", ["Seeds", "Roots", "Dried berries"],
            "They come from a tree first grown on a few islands in Indonesia, once known as the Spice Islands.",
            wiki("Clove"), difficulty=3)
food.choice("Nutmeg comes from a seed. Which other spice comes from the red net wrapped around that seed?", "Mace", ["Allspice", "Cardamom", "Star anise"],
            "One fruit gives you two spices.",
            wiki("Nutmeg"), difficulty=3)
food.choice("The machine that made candy floss popular was co-invented by what kind of person?", "A dentist", ["A doctor", "A baker", "A sweet shop owner"],
            "William Morrison, a dentist, and John C. Wharton sold it as 'Fairy Floss' at the 1904 World's Fair.",
            wiki("Cotton candy"), difficulty=2)
food.choice("The sandwich is named after the Earl of where?", "Sandwich", ["Bread", "Bristol", "Kent"],
            "The 4th Earl of Sandwich liked to eat meat between bread so he didn't have to leave his desk or card table.",
            wiki("John Montagu, 4th Earl of Sandwich"), difficulty=1)
food.choice("Peach Melba is named after whom?", "An Australian opera singer", ["A Russian ballerina", "A French queen", "An American actress"],
            "The chef Auguste Escoffier made it for Nellie Melba at the Savoy in London. Pavlova is the one named after a ballerina.",
            wiki("Peach Melba"), difficulty=2)
food.choice("Which TV chef campaigned to improve school dinners in 2005?", "Jamie Oliver", ["Gordon Ramsay", "Delia Smith", "Nigella Lawson"],
            "His series Jamie's School Dinners led to new rules on what schools could serve.",
            wiki("Jamie's School Dinners"), difficulty=1)
food.choice("Which TV chef played football for Rangers as a teenager, until an injury?", "Gordon Ramsay", ["Jamie Oliver", "Marco Pierre White", "Heston Blumenthal"],
            "He then trained as a chef, and has held 17 Michelin stars over his career.",
            wiki("Gordon Ramsay"), difficulty=2)
food.choice("Which chef serves snail porridge at The Fat Duck?", "Heston Blumenthal", ["Gordon Ramsay", "Marco Pierre White", "Tom Kerridge"],
            "He's famous for science in the kitchen, like bacon and egg ice cream.",
            wiki("Heston Blumenthal"), difficulty=2)
food.choice("Who judged The Great British Bake Off with Paul Hollywood for its first seven series?", "Mary Berry", ["Prue Leith", "Delia Smith", "Nigella Lawson"],
            "Prue Leith took over when the show moved to Channel 4 in 2017.",
            wiki("Mary Berry"), difficulty=1)
food.choice("Which TV cook became joint majority shareholder of Norwich City football club in 1996?", "Delia Smith", ["Nigella Lawson", "Mary Berry", "Prue Leith"],
            "She and her husband, Michael Wynn-Jones, are lifelong fans. Her cookery books have sold over 21 million copies.",
            wiki("Delia Smith"), difficulty=3)
food.choice("What does 'al dente' mean when cooking pasta?", "To the tooth", ["With butter", "Fresh from the pan", "Well done"],
            "It means cooked until it's still slightly firm when you bite it.",
            wiki("Al dente"), difficulty=2)
food.choice("Which pasta's name means 'little tongues'?", "Linguine", ["Vermicelli", "Farfalle", "Orecchiette"],
            "Vermicelli means 'little worms', farfalle 'butterflies' and orecchiette 'little ears'.",
            wiki("Linguine"), difficulty=3)
food.higher_lower("In its whole life, does a worker honeybee make more or less than a teaspoon of honey?", False,
                  "Much less: about a twelfth of a teaspoon. A jar of honey takes the work of hundreds of bees.",
                  wiki("Honey bee"), labels=("More", "Less"), difficulty=2)
food.choice("Which fruit came from a cross between a pomelo and a sweet orange?", "The grapefruit", ["The lemon", "The lime", "The tangerine"],
            "It was first found in Barbados in the 1700s. It's called a grapefruit because it grows in clusters, like grapes.",
            wiki("Grapefruit"), difficulty=3)

# Inventions & Brands ------------------------------------------------------------------------------
tech.choice("Which programming language is named after a comedy group?", "Python", ["Ruby", "Java", "Perl"],
            "Guido van Rossum named it after Monty Python's Flying Circus, not the snake.",
            wiki("Python (programming language)"), difficulty=2)
tech.choice("What was Bubble Wrap first meant to be?", "Wallpaper", ["Packaging", "Insulation for houses", "A toy"],
            "Its inventors sealed two shower curtains together in 1957, hoping for textured wallpaper.",
            wiki("Bubble wrap"), difficulty=2)
tech.choice("What was Play-Doh first sold as?", "A wallpaper cleaner", ["A modelling clay for artists", "A bread dough", "A glue"],
            "When fewer homes had coal fires, there was less soot to clean, so it was turned into a toy in 1956.",
            wiki("Play-Doh"), difficulty=2)
tech.choice("Post-it Notes came from a failed attempt to make what?", "A super-strong glue", ["A paper towel", "A sticky tape", "A wallpaper paste"],
            "Spencer Silver at 3M made a weak glue in 1968. A colleague later used it to stop bookmarks falling out of his hymn book.",
            wiki("Post-it Note"), difficulty=2)
tech.choice("Which invention came about when a chocolate bar melted in an engineer's pocket near radar equipment?", "The microwave oven", ["The toaster", "The electric kettle", "The dishwasher"],
            "Percy Spencer noticed it in 1945. The first microwave ovens were nearly as tall as a person.",
            wiki("Microwave oven"), difficulty=2)
tech.choice("Which toy was invented by a naval engineer who saw a spring fall off a shelf?", "The Slinky", ["The yo-yo", "The Frisbee", "The pogo stick"],
            "Richard James saw it in 1943. His wife Betty picked the name from a dictionary.",
            wiki("Slinky"), difficulty=2)
tech.choice("What gave George de Mestral the idea for Velcro?", "Burrs stuck to his dog's fur", ["A bird's nest", "A spider's web", "A lizard's feet"],
            "He looked at the burrs under a microscope after a walk in the Alps, and saw tiny hooks.",
            wiki("Velcro"), difficulty=2)
tech.choice("What did the world's first webcam watch?", "A coffee pot", ["A fish tank", "A busy road", "A bird box"],
            "Scientists at Cambridge University set it up in 1991 so they didn't walk to an empty pot.",
            wiki("Trojan Room coffee pot"), difficulty=2)
tech.choice("What was the first thing sold on eBay, in 1995?", "A broken laser pointer", ["A signed baseball", "A Beanie Baby", "A second-hand book"],
            "It sold for 14 dollars and 83 cents. The buyer said he collected broken laser pointers.",
            wiki("eBay"), difficulty=3)
tech.choice("Which company was first called BackRub?", "Google", ["Yahoo", "Amazon", "Facebook"],
            "Larry Page and Sergey Brin started it at Stanford University. The new name came from 'googol', a 1 with 100 zeros.",
            wiki("History of Google"), difficulty=2)
tech.choice("Which company was nearly called Cadabra, until people misheard it as 'cadaver'?", "Amazon", ["eBay", "Google", "Netflix"],
            "Jeff Bezos chose Amazon, after the biggest river, which also put it near the top of alphabetical lists.",
            wiki("History of Amazon"), difficulty=2)
tech.choice("What did Alexander Graham Bell want people to say when answering the phone?", "Ahoy", ["Hello", "Who's there?", "Good day"],
            "Thomas Edison pushed for 'Hello', and Edison won.",
            wiki("Ahoy (greeting)"), difficulty=2)
tech.yes_no("Was the tin can invented before the tin opener?", True,
            "By decades. Cans were patented in 1810, and people opened them with hammers and chisels until openers came along in the 1850s.",
            wiki("Can opener"), difficulty=2)
tech.choice("Which company launched the Walkman in 1979?", "Sony", ["Panasonic", "Philips", "Toshiba"],
            "It was the first cheap personal stereo you could carry around. Sony sold around 200 million cassette Walkmans.",
            wiki("Walkman"), era="classic", difficulty=2)
tech.choice("Sony developed the compact disc with which other company?", "Philips", ["Panasonic", "Toshiba", "Pioneer"],
            "CDs went on sale in 1982. A CD was made to hold 74 minutes, said to be long enough for Beethoven's Ninth Symphony.",
            wiki("Compact disc"), difficulty=3)
tech.choice("Which country did the Rubik's Cube come from?", "Hungary", ["Japan", "Austria", "Czechoslovakia"],
            "Ernő Rubik, an architecture lecturer, made the first one in 1974. It took him about a month to solve it himself.",
            wiki("Rubik's Cube"), difficulty=2)
tech.choice("What inspired Percy Shaw to invent cat's eyes for roads?", "A cat's eyes shining in his headlights", ["Reflections in a puddle", "A lighthouse", "Stars in the sky"],
            "He was driving home in fog near Halifax. He patented them in 1934.",
            wiki("Cat's eye (road)"), difficulty=2)
tech.choice("Who invented the hovercraft?", "Christopher Cockerell", ["Frank Whittle", "Barnes Wallis", "Isambard Kingdom Brunel"],
            "He tested the idea using two tin cans and a hairdryer. A hovercraft crossed the Channel in 1959.",
            wiki("Christopher Cockerell"), difficulty=3)

# Words & Language ---------------------------------------------------------------------------------
words.choice("What was Oxford's Word of the Year for 2024?", "Brain rot", ["Rizz", "Goblin mode", "Vax"],
             "All four are real winners: rizz was 2023, goblin mode 2022 and vax 2021.",
             wiki("Brain rot"), era="modern", difficulty=2)
words.choice("What does 'rizz' mean?", "Charm", ["Money", "Anger", "Laziness"],
             "It probably comes from the middle of 'charisma', and was Oxford's Word of the Year for 2023.",
             wiki("Rizz"), era="modern", difficulty=2)
words.choice("How many syllables does a traditional haiku have?", "17", ["14", "12", "21"],
             "Five in the first line, seven in the second and five in the third.",
             wiki("Haiku"), difficulty=2)
words.choice("What does SOS stand for?", "Nothing: it was chosen because it's easy in Morse code", ["Save Our Souls", "Save Our Ship", "Send Out Support"],
             "Three dots, three dashes, three dots. 'Save Our Souls' was made up afterwards.",
             wiki("SOS"), difficulty=3)
words.choice("Where does 'OK' probably come from?", "A jokey misspelling of 'all correct'", ["A Native American word", "A French phrase", "A Greek word"],
             "In 1839, Boston newspapers had a craze for funny abbreviations, and 'oll korrect' was one of them.",
             wiki("OK"), difficulty=3)
words.choice("Which letter doesn't appear in the name of any US state?", "Q", ["Z", "X", "J"],
             "Z is in Arizona, X in Texas and New Mexico, and J in New Jersey.",
             wiki("U.S. state"), difficulty=3)
words.choice("What do you call an abbreviation said as a word, like NASA?", "An acronym", ["An initialism", "An anagram", "A palindrome"],
             "When you say each letter, like BBC, it's an initialism.",
             wiki("Acronym"), difficulty=2)
words.choice("What is a 'portmanteau' word, like 'brunch'?", "Two words blended into one", ["A word borrowed from French", "A word that sounds like its meaning", "A word spelt the same backwards"],
             "Brunch is breakfast and lunch. Lewis Carroll first used 'portmanteau' this way in Through the Looking-Glass.",
             wiki("Blend word"), difficulty=2)
words.choice("Which two words were blended to make 'smog'?", "Smoke and fog", ["Smell and fog", "Smoke and grime", "Smudge and fog"],
             "The word was coined in the early 1900s, when coal smoke mixed with fog in big cities.",
             wiki("Smog"), difficulty=1)
words.choice("What is a group of jellyfish called?", "A smack", ["A wobble", "A sting", "A swarm"],
             "A large group can also be called a bloom.",
             wiki("List of animal names"), difficulty=3)
words.choice("What is a swirling flock of starlings called?", "A murmuration", ["A murder", "A parliament", "A charm"],
             "A murder is crows, a parliament is owls and a charm is goldfinches.",
             wiki("Common starling"), difficulty=2)
words.choice("What does the Danish word 'hygge' describe?", "A cosy, contented feeling", ["A kind of pastry", "A winter storm", "A type of boat"],
             "Think candles, blankets and hot drinks with friends.",
             wiki("Hygge"), era="modern", difficulty=2)
words.choice("What is a 'cwtch' in Welsh English?", "A cuddle", ["A cup of tea", "A small dog", "A rain shower"],
             "It can also mean a cosy little cupboard or hiding place.",
             wiki("Welsh English"), difficulty=2)
words.choice("Where is the village with Europe's longest place name, 58 letters long?", "Anglesey, Wales", ["The Scottish Highlands", "County Kerry, Ireland", "Iceland"],
             "Llanfairpwllgwyngyll and so on. The long version was made up in the 1860s to attract tourists.",
             wiki("Llanfairpwllgwyngyll"), difficulty=2)
words.choice("The word 'boomerang' comes from which language?", "An Aboriginal Australian language", ["Māori", "Hawaiian", "Zulu"],
             "It comes from Dharug, spoken around Sydney.",
             wiki("Boomerang"), difficulty=3)
words.higher_lower("Are more or fewer than 500 languages spoken in Papua New Guinea?", True,
                   "More: about 840, the most of any country in the world.",
                   wiki("Languages of Papua New Guinea"), labels=("More", "Fewer"), difficulty=3)
words.choice("Which plural do most dictionaries prefer for 'octopus'?", "Octopuses", ["Octopi", "Octopodes", "Octopus"],
             "'Octopi' is common, but it treats the word as Latin when it actually comes from Greek.",
             wiki("Octopus"), difficulty=3)

# Nature & Animals ---------------------------------------------------------------------------------
nature.choice("Which animal does cube-shaped poo?", "The wombat", ["The koala", "The kangaroo", "The platypus"],
              "Wombats use the cubes to mark their territory, and the flat sides stop them rolling away.",
              wiki("Wombat"), difficulty=2)
nature.choice("How do sea otters stop drifting apart while they sleep?", "They hold hands", ["They sleep in burrows", "They tie themselves to rocks", "They take turns to stay awake"],
              "They also wrap themselves in seaweed so they don't float away.",
              wiki("Sea otter"), difficulty=2)
nature.choice("Which animal has the biggest eyes?", "The colossal squid", ["The blue whale", "The ostrich", "The owl"],
              "Its eyes are about the size of a football.",
              wiki("Colossal squid"), difficulty=3)
nature.choice("Which animal can sleep up to 22 hours a day?", "The koala", ["The sloth", "The cat", "The lion"],
              "Eucalyptus leaves give koalas very little energy, so they rest most of the time.",
              wiki("Koala"), difficulty=2)
nature.yes_no("Have sharks been around for longer than trees?", True,
              "Sharks go back about 450 million years. The first trees appeared about 385 million years ago.",
              wiki("Shark"), difficulty=3)
nature.choice("Which tiny animal has survived being sent into open space?", "The tardigrade", ["The cockroach", "The ant", "The flea"],
              "Also called water bears, they survived in space on a European mission in 2007.",
              wiki("Tardigrade"), difficulty=3)
nature.choice("Which flightless bird is a national symbol of New Zealand?", "The kiwi", ["The emu", "The kākāpō", "The ostrich"],
              "New Zealanders are nicknamed Kiwis after it. The kākāpō, a rare flightless parrot, is from New Zealand too.",
              wiki("Kiwi (bird)"), difficulty=1)
nature.choice("Hippos make their own sunscreen. What colour is it?", "Red", ["White", "Blue", "Green"],
              "It's an oily red liquid from their skin, sometimes called 'blood sweat', but it isn't blood or sweat.",
              wiki("Hippopotamus"), difficulty=3)
nature.choice("What is the hippo's closest living relative?", "Whales and dolphins", ["Pigs", "Rhinos", "Elephants"],
              "Hippos and whales share an ancestor that lived around 55 million years ago.",
              wiki("Whippomorpha"), difficulty=3)
nature.choice("Which of these is the closest living relative of the Tyrannosaurus rex?", "The chicken", ["The crocodile", "The Komodo dragon", "The iguana"],
              "Birds are living dinosaurs. Proteins from a T. rex bone are most like those of chickens and ostriches.",
              wiki("Tyrannosaurus"), difficulty=2)
nature.choice("Which kind of tree can live the longest?", "The bristlecone pine", ["The oak", "The yew", "The giant sequoia"],
              "One in California is thought to be over 4,800 years old. Its exact location is kept secret to protect it.",
              wiki("Pinus longaeva"), difficulty=3, as_of="2026")
nature.choice("Which plant can grow nearly a metre in a single day?", "Bamboo", ["Ivy", "Sunflower", "Oak"],
              "Some kinds of bamboo grow so fast you can almost watch it happen.",
              wiki("Bamboo"), difficulty=2)
nature.choice("What colour is a giraffe's tongue?", "Dark blue-purple", ["Pink", "Black and white spotted", "Bright red"],
              "The dark colour may protect it from sunburn while it eats leaves all day.",
              wiki("Giraffe"), difficulty=2)

# Space ---------------------------------------------------------------------------------------------
space.yes_no("Would Saturn float, if you could find a bath big enough?", True,
             "It's mostly gas, so it's less dense than water.",
             wiki("Saturn"), difficulty=2)
space.choice("Which planet has the coldest temperature ever measured in the Solar System?", "Uranus", ["Neptune", "Pluto", "Mercury"],
             "A surprise, since Neptune is further from the Sun. Uranus has reached about minus 224 degrees.",
             wiki("Uranus"), difficulty=3)
space.choice("What is at the centre of the Milky Way?", "A supermassive black hole", ["A giant star", "The Sun", "Nothing at all"],
             "It's called Sagittarius A*, and is about 4 million times as heavy as the Sun.",
             wiki("Sagittarius A*"), difficulty=2)
space.choice("Which planet has a moon called Titan, with lakes of liquid methane?", "Saturn", ["Jupiter", "Uranus", "Neptune"],
             "Titan is the only moon with a thick atmosphere. NASA plans to send a flying drone called Dragonfly there in the 2030s.",
             wiki("Titan (moon)"), difficulty=2)
space.choice("What colour are sunsets on Mars?", "Blue", ["Red", "Green", "Purple"],
             "Fine Martian dust scatters blue light near the Sun as it sets. NASA's rovers have photographed it.",
             wiki("Mars"), difficulty=3)
space.choice("Who was the first woman to walk in space, in 1984?", "Svetlana Savitskaya", ["Valentina Tereshkova", "Sally Ride", "Kathryn Sullivan"],
             "Valentina Tereshkova was the first woman in space, in 1963. Kathryn Sullivan was the first American woman to do a spacewalk, later in 1984.",
             wiki("Svetlana Savitskaya"), difficulty=3)
space.choice("Roughly how many times a day does the International Space Station go round the Earth?", "16", ["1", "4", "100"],
             "It travels at about 28,000 km an hour, so astronauts see about 16 sunrises a day.",
             wiki("International Space Station"), difficulty=2)
