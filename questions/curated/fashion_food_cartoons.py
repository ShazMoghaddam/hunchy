"""Fashion (new subject), more Food & Drink, and Cartoons & Animation (new subject)."""

from . import Category, wiki

f = Category("fashion")

f.choice("Which country does the fashion house Gucci come from?", "Italy", ["France", "Spain", "Switzerland"],
         "Guccio Gucci opened his first shop in Florence in 1921, selling leather goods.",
         wiki("Gucci"), difficulty=1)
f.choice("Which country does Louis Vuitton come from?", "France", ["Italy", "Belgium", "Switzerland"],
         "Louis Vuitton began in Paris in 1854 making flat-topped travel trunks that could be stacked.",
         wiki("Louis Vuitton"), difficulty=1)
f.choice("Which British fashion brand is famous for its trench coat and check pattern?", "Burberry", ["Barbour", "Mulberry", "Paul Smith"],
         "Thomas Burberry invented gabardine, a tough, weatherproof cloth, in 1879. Soldiers wore his trench coats in the First World War.",
         wiki("Burberry"), difficulty=2)
f.choice("Which Italian fashion house uses the head of Medusa as its logo?", "Versace", ["Prada", "Armani", "Fendi"],
         "Gianni Versace chose Medusa because people who looked at her couldn't look away.",
         wiki("Versace"), difficulty=2)
f.choice("In which city is the fashion house Prada based?", "Milan", ["Rome", "Paris", "Florence"],
         "Prada began in Milan in 1913 as a shop selling leather goods.",
         wiki("Prada"), difficulty=2)
f.choice("Which designer launched the famous 'New Look' in 1947, with tiny waists and full skirts?", "Christian Dior", ["Coco Chanel", "Yves Saint Laurent", "Hubert de Givenchy"],
         "After years of wartime rationing, the New Look used huge amounts of fabric.",
         wiki("Christian Dior"), era="classic", difficulty=2)
f.choice("Which London designer made the miniskirt famous in the 1960s?", "Mary Quant", ["Vivienne Westwood", "Zandra Rhodes", "Stella McCartney"],
         "Mary Quant named the miniskirt after her favourite car, the Mini.",
         wiki("Mary Quant"), era="classic", difficulty=2)
f.choice("Which British designer is known as the godmother of punk fashion?", "Vivienne Westwood", ["Mary Quant", "Stella McCartney", "Victoria Beckham"],
         "Vivienne Westwood ran a shop on the King's Road in London with Malcolm McLaren, manager of the Sex Pistols.",
         wiki("Vivienne Westwood"), era="classic", difficulty=2)
f.choice("Who made the first blue jeans with metal rivets, in 1873?", "Levi Strauss and Jacob Davis", ["Calvin Klein", "Ralph Lauren", "Henry Ford"],
         "The rivets stopped the pockets of miners' trousers tearing.",
         wiki("Levi Strauss & Co."), era="classic", difficulty=2)
f.choice("Denim takes its name from which French city?", "Nîmes", ["Paris", "Lyon", "Marseille"],
         "Denim comes from 'serge de Nîmes'. The word jeans comes from Genoa, in Italy.",
         wiki("Denim"), difficulty=3)
f.choice("Which tough leather boots with yellow stitching were first made in England in 1960?", "Dr. Martens", ["Timberland", "Hunter", "Ugg"],
         "The air-cushioned sole was invented by a German doctor, Klaus Märtens, after he hurt his ankle skiing.",
         wiki("Dr. Martens"), era="classic", difficulty=2)
f.choice("Which Spanish fashion chain is famous for getting new designs into shops within weeks?", "Zara", ["Mango", "Desigual", "H&M"],
         "Zara's first shop opened in A Coruña, in Galicia, in 1975.",
         wiki("Zara (retailer)"), era="modern", difficulty=1)
f.choice("Which country does the clothing chain H&M come from?", "Sweden", ["Germany", "The Netherlands", "Denmark"],
         "H&M opened in Västerås in 1947 as Hennes, which means 'hers' in Swedish.",
         wiki("H&M"), difficulty=2)
f.choice("Which country does the clothing brand Uniqlo come from?", "Japan", ["South Korea", "China", "Thailand"],
         "Uniqlo opened in Hiroshima in 1984. The name is short for 'Unique Clothing Warehouse'.",
         wiki("Uniqlo"), era="modern", difficulty=2)
f.choice("In which city did Primark open its first shop, in 1969?", "Dublin", ["Manchester", "London", "Belfast"],
         "In Ireland, Primark still trades under its original name, Penneys.",
         wiki("Primark"), era="classic", difficulty=3)
f.choice("Which tennis player started a clothing brand with a crocodile logo?", "René Lacoste", ["Fred Perry", "Björn Borg", "Andre Agassi"],
         "Lacoste's polo shirt, from 1933, replaced the long-sleeved shirts tennis players wore before.",
         wiki("Lacoste"), era="classic", difficulty=2)
f.yes_no("Did the British tennis champion Fred Perry also start a clothing brand?", True,
         "Its logo is a laurel wreath, based on the old Wimbledon symbol.",
         wiki("Fred Perry (brand)"), era="classic", difficulty=2)
f.choice("Which four cities hold the 'big four' fashion weeks?", "New York, London, Milan and Paris", ["Paris, Rome, Tokyo and Madrid", "London, Berlin, Milan and Sydney", "New York, Los Angeles, Paris and Rome"],
         "They take place twice a year, showing clothes for spring and summer, then autumn and winter.",
         wiki("Fashion week"), difficulty=2)
f.choice("The Hermès Birkin handbag is named after which actress and singer?", "Jane Birkin", ["Audrey Hepburn", "Grace Kelly", "Brigitte Bardot"],
         "Jane Birkin sat next to the head of Hermès on a flight in 1983 and said she couldn't find a good weekend bag.",
         wiki("Birkin bag"), era="classic", difficulty=3)
f.choice("Ray-Ban Aviator sunglasses were first made for whom?", "American military pilots", ["Racing drivers", "Film stars", "Skiers"],
         "They were designed in the 1930s to cut glare for pilots flying at high altitude.",
         wiki("Ray-Ban"), era="classic", difficulty=2)
f.choice("Which famous boots are named after a duke who beat Napoleon?", "Wellington boots", ["Chelsea boots", "Doc Martens", "Hush Puppies"],
         "The first Duke of Wellington asked his shoemaker for a new style of boot in the early 1800s.",
         wiki("Wellington boot"), difficulty=1)
f.choice("Which knitted jacket is named after a British earl who led the Charge of the Light Brigade?", "The cardigan", ["The blazer", "The anorak", "The poncho"],
         "The 7th Earl of Cardigan's troops wore knitted waistcoats in the Crimean War.",
         wiki("Cardigan (sweater)"), difficulty=3)
f.choice("Which swimwear was named after a Pacific atoll in 1946?", "The bikini", ["The tankini", "The burkini", "The monokini"],
         "The French designer Louis Réard named it after Bikini Atoll.",
         wiki("Bikini"), era="classic", difficulty=2)
f.choice("Which country is the kimono from?", "Japan", ["China", "Korea", "Vietnam"],
         "Kimono simply means 'thing to wear'.",
         wiki("Kimono"), difficulty=1)
f.choice("Which country is famous for the kilt?", "Scotland", ["Ireland", "Wales", "Norway"],
         "The patterns, called tartans, are often linked to particular Scottish clans or families.",
         wiki("Kilt"), difficulty=1)
f.choice("Which famous waterproof coat is named after the Scottish chemist who invented its fabric?", "The mackintosh", ["The duffle coat", "The trench coat", "The parka"],
         "Charles Macintosh patented rubberised waterproof cloth in 1823.",
         wiki("Mackintosh"), difficulty=3)
f.choice("Which country does the watch brand Swatch come from?", "Switzerland", ["Japan", "Germany", "Sweden"],
         "Swatch was launched in 1983 to win back customers from cheap Japanese digital watches.",
         wiki("Swatch"), era="classic", difficulty=2)
f.choice("Which German fashion house, famous for men's suits, was founded in Metzingen in 1924?", "Hugo Boss", ["Adidas", "Jil Sander", "Escada"],
         "Metzingen is a small town near Stuttgart. Hugo Boss is now one of the world's best-known names in tailoring.",
         wiki("Hugo Boss"), difficulty=3)
f.choice("Which designer led Chanel for 36 years, from 1983 until 2019?", "Karl Lagerfeld", ["Tom Ford", "Marc Jacobs", "Valentino"],
         "Lagerfeld was known for his white ponytail, dark glasses and his cat, Choupette.",
         wiki("Karl Lagerfeld"), era="modern", difficulty=2)
f.choice("Which shoe with a rubber toe cap was named after basketball player Chuck Taylor?", "The Converse All Star", ["The Nike Air Jordan", "The Vans Old Skool", "The Adidas Superstar"],
         "Chuck Taylor travelled the United States selling the shoe and running basketball clinics.",
         wiki("Chuck Taylor All-Stars"), era="classic", difficulty=2)
f.higher_lower("Nike's first Air Jordan trainer came out in 1985. Did the Adidas Superstar come out earlier or later?", True,
               "The Adidas Superstar first came out in 1969 as a basketball shoe.",
               wiki("Adidas Superstar"), labels=("Earlier", "Later"), era="classic", difficulty=3)
f.yes_no("Does Primark trade under a different name in Ireland?", True,
         "It's called Penneys there, its original name from 1969.",
         wiki("Primark"), difficulty=2)

food = Category("food", prefix="food2")
food.choice("Which country does Nutella come from?", "Italy", ["France", "Belgium", "Switzerland"],
            "Pietro Ferrero created a hazelnut spread in Alba in 1946, when chocolate was scarce. Nutella itself launched in 1964.",
            wiki("Nutella"), difficulty=1)
food.choice("Which country does Haribo come from?", "Germany", ["Denmark", "Austria", "The Netherlands"],
            "The name comes from its founder and home town: HAns RIegel BOnn.",
            wiki("Haribo"), difficulty=2)
food.choice("In which English city did Cadbury build its chocolate factory and village, Bournville?", "Birmingham", ["York", "Bristol", "Manchester"],
            "George Cadbury built Bournville as a village for his workers, with parks and good homes.",
            wiki("Bournville"), difficulty=2)
food.choice("Which country does Toblerone come from?", "Switzerland", ["Austria", "Belgium", "Germany"],
            "It was created in Bern in 1908. The name joins Tobler, the maker, with torrone, an Italian nougat.",
            wiki("Toblerone"), difficulty=2)
food.yes_no("Was the first Mars bar made in England?", True,
            "Forrest Mars, son of the American Mars family, made the first Mars bars in Slough in 1932.",
            wiki("Mars (chocolate bar)"), era="classic", difficulty=3)
food.choice("In which English city was the KitKat first made, in 1935?", "York", ["Birmingham", "Bristol", "London"],
            "Rowntree's of York created it as a snack workers could take to work.",
            wiki("Kit Kat"), era="classic", difficulty=3)
food.choice("In which American city was Coca-Cola invented, in 1886?", "Atlanta", ["New York", "Chicago", "New Orleans"],
            "It was created by a pharmacist, John Pemberton, and first sold for 5 cents a glass.",
            wiki("Coca-Cola"), difficulty=2)
food.yes_no("Is Häagen-Dazs ice cream from Scandinavia?", False,
            "It was created in New York in 1960. The founders made up the name to sound Danish.",
            wiki("Häagen-Dazs"), difficulty=3)
food.choice("Which famous artist designed the Chupa Chups lollipop logo?", "Salvador Dalí", ["Pablo Picasso", "Joan Miró", "Andy Warhol"],
            "Dalí sketched the daisy logo in about an hour in 1969. Chupa Chups is from Spain.",
            wiki("Chupa Chups"), era="classic", difficulty=3)
food.yes_no("Did a UK court decide that a Jaffa Cake is a cake, not a biscuit?", True,
            "In 1991 a tribunal agreed it was a cake, partly because cakes go hard when stale and biscuits go soft. Jaffa Cakes go hard.",
            wiki("Jaffa Cakes"), era="classic", difficulty=2)
food.choice("What is Marmite made from?", "Yeast left over from brewing beer", ["Burnt sugar", "Soy beans", "Beef stock"],
            "Marmite has been made in Burton upon Trent, a brewing town, since 1902.",
            wiki("Marmite"), difficulty=2)
food.choice("Which country did bubble tea come from?", "Taiwan", ["Japan", "Thailand", "South Korea"],
            "Bubble tea, with chewy tapioca pearls, began in Taiwan in the 1980s.",
            wiki("Bubble tea"), era="modern", difficulty=2)
food.choice("In which US state did Colonel Sanders start selling his fried chicken?", "Kentucky", ["Texas", "Tennessee", "Georgia"],
            "His secret recipe has 11 herbs and spices.",
            wiki("KFC"), difficulty=1)
food.choice("Where did the first McDonald's restaurant open, in 1940?", "San Bernardino, California", ["New York", "Chicago", "Dallas"],
            "Brothers Richard and Maurice McDonald opened it. Ray Kroc later turned it into a worldwide chain.",
            wiki("McDonald's"), era="classic", difficulty=3)
food.choice("In which city did Starbucks open its first shop, in 1971?", "Seattle", ["San Francisco", "New York", "Boston"],
            "The first shop sold coffee beans to take home, not drinks.",
            wiki("Starbucks"), era="classic", difficulty=2)
food.choice("Which Scottish soft drink is bright orange and famous for its secret recipe?", "Irn-Bru", ["Tango", "Vimto", "Lucozade"],
            "Irn-Bru has been made in Scotland since 1901. Only a few people know the full recipe.",
            wiki("Irn-Bru"), difficulty=1)
food.choice("Which American state does Tabasco sauce come from?", "Louisiana", ["Texas", "New Mexico", "Florida"],
            "Tabasco has been made on Avery Island, Louisiana, since 1868.",
            wiki("Tabasco sauce"), difficulty=3)
food.choice("Which country does the Kinder Surprise egg come from?", "Italy", ["Germany", "Switzerland", "Belgium"],
            "Kinder is made by Ferrero, the same company as Nutella. Kinder means 'children' in German.",
            wiki("Kinder Surprise"), difficulty=2)
food.choice("Which biscuit, first made in 1912, is the world's best-selling cookie?", "The Oreo", ["The Digestive", "The Hobnob", "The Jammie Dodger"],
            "Oreos were first made in New York.",
            wiki("Oreo"), difficulty=2, as_of="2026-11")
food.choice("Which country does Lindt chocolate come from?", "Switzerland", ["Belgium", "Germany", "Austria"],
            "Rodolphe Lindt invented 'conching' in 1879, which made chocolate smooth and melting for the first time.",
            wiki("Lindt & Sprüngli"), difficulty=2)
food.choice("Which country does the yoghurt company Danone come from?", "France", ["Spain", "Switzerland", "Italy"],
            "Danone was started in Barcelona in 1919 and moved to France. Its name comes from Danon, the founder's son's nickname.",
            wiki("Danone"), difficulty=3)
food.choice("Which crisp company started in Leicester?", "Walkers", ["Pringles", "Tyrrells", "McCoy's"],
            "Walkers was started by a butcher, Henry Walker, when meat was rationed after the Second World War.",
            wiki("Walkers (snack foods)"), difficulty=2)
food.higher_lower("Heinz said in 1896 that it had '57 varieties'. Did it really have more or fewer products than that?", True,
                  "Henry Heinz picked 57 because he liked the number. The company already made more than 60 products.",
                  wiki("Heinz"), labels=("More", "Fewer"), era="classic", difficulty=3)
food.yes_no("Did Ben & Jerry's ice cream start in a converted petrol station?", True,
            "Ben Cohen and Jerry Greenfield opened their first shop in an old petrol station in Burlington, Vermont, in 1978.",
            wiki("Ben & Jerry's"), era="classic", difficulty=3)
food.choice("Which French cheese comes in a red wax coat?", "Babybel", ["Brie", "Camembert", "Roquefort"],
            "Babybel is made by the French company Bel, which also makes The Laughing Cow.",
            wiki("Babybel"), difficulty=1)

toon = Category("cartoons")

toon.choice("In which 1928 cartoon did Mickey Mouse first appear with sound?", "Steamboat Willie", ["Fantasia", "The Band Concert", "Plane Crazy"],
            "Walt Disney did Mickey's voice himself for many years.",
            wiki("Steamboat Willie"), era="classic", difficulty=2)
toon.choice("What is the name of Mickey Mouse's dog?", "Pluto", ["Goofy", "Max", "Rover"],
            "Pluto first appeared in 1930. Goofy is also a dog, but he walks and talks.",
            wiki("Pluto (Disney)"), difficulty=1)
toon.choice("What are the names of Donald Duck's three nephews?", "Huey, Dewey and Louie", ["Chip, Dale and Pete", "Larry, Curly and Moe", "Timmy, Tommy and Teddy"],
            "They first appeared in 1937.",
            wiki("Huey, Dewey, and Louie"), difficulty=2)
toon.choice("In Disney's 1973 film Robin Hood, what kind of animal is Robin?", "A fox", ["A wolf", "A cat", "A rabbit"],
            "Little John is a bear and Prince John is a lion who sucks his thumb.",
            wiki("Robin Hood (1973 film)"), era="classic", difficulty=1)
toon.choice("In Disney's Robin Hood, what kind of animal is the greedy Prince John?", "A lion", ["A snake", "A wolf", "A bear"],
            "His sidekick, Sir Hiss, is a snake.",
            wiki("Robin Hood (1973 film)"), era="classic", difficulty=2)
toon.choice("In The Jungle Book, what kind of animal is Baloo?", "A bear", ["A panther", "A tiger", "An orangutan"],
            "Bagheera is the panther, Shere Khan the tiger and King Louie the orangutan.",
            wiki("The Jungle Book (1967 film)"), difficulty=1)
toon.choice("Which actor voiced the Genie in Disney's 1992 Aladdin?", "Robin Williams", ["Will Smith", "Eddie Murphy", "Jim Carrey"],
            "Robin Williams made up so many lines that the film had hours of extra recordings.",
            wiki("Aladdin (1992 Disney film)"), era="classic", difficulty=2)
toon.choice("In The Little Mermaid, what kind of animal is Sebastian?", "A crab", ["A lobster", "A fish", "A seahorse"],
            "Sebastian sings 'Under the Sea', which won the Oscar for Best Original Song.",
            wiki("Sebastian (The Little Mermaid)"), difficulty=1)
toon.yes_no("Was Beauty and the Beast the first animated film nominated for the Oscar for Best Picture?", True,
            "The 1991 film was nominated before there was an Oscar just for animated films.",
            wiki("Beauty and the Beast (1991 film)"), era="classic", difficulty=3)
toon.choice("In Finding Nemo, what kind of fish is Nemo?", "A clownfish", ["A goldfish", "A pufferfish", "A blue tang"],
            "His forgetful friend Dory is a blue tang.",
            wiki("Finding Nemo"), difficulty=1)
toon.choice("In Monsters, Inc., what powers the city of Monstropolis?", "Children's screams", ["Lightning", "Monster sweat", "Laughter only"],
            "By the end of the film they find laughter works even better.",
            wiki("Monsters, Inc."), difficulty=2)
toon.choice("In the Pixar film Up, how does Carl make his house fly?", "With thousands of balloons", ["With a rocket", "With a giant kite", "With a hot-air engine"],
            "Lifting a real house would take millions of balloons. The film shows thousands.",
            wiki("Up (2009 film)"), era="modern", difficulty=1)
toon.choice("What is the name of the red racing car in Pixar's Cars?", "Lightning McQueen", ["Mater", "Doc Hudson", "Francesco Bernoulli"],
            "His race number is 95, a nod to 1995, the year Toy Story came out.",
            wiki("Lightning McQueen"), era="modern", difficulty=1)
toon.choice("Which of these is not one of the five main emotions in the first Inside Out film?", "Anxiety", ["Joy", "Sadness", "Disgust"],
            "The five are Joy, Sadness, Anger, Fear and Disgust. Anxiety arrives in Inside Out 2.",
            wiki("Inside Out (2015 film)"), era="modern", difficulty=2)
toon.choice("In Encanto, which family member does nobody talk about?", "Bruno", ["Mirabel", "Luisa", "Isabela"],
            "Bruno can see the future, and his song became a huge hit in 2022.",
            wiki("Encanto (film)"), era="modern", difficulty=1)
toon.choice("In Moana, who is the shape-shifting demigod voiced by Dwayne Johnson?", "Maui", ["Tamatoa", "Te Kā", "Heihei"],
            "Heihei is the very silly chicken.",
            wiki("Moana (2016 film)"), era="modern", difficulty=1)
toon.choice("Which Pixar film is set during Mexico's Day of the Dead?", "Coco", ["Encanto", "Luca", "Elemental"],
            "A boy called Miguel ends up in the Land of the Dead, chasing his dream of playing music.",
            wiki("Coco (2017 film)"), era="modern", difficulty=2)
toon.choice("What kind of animal is Shrek's talkative best friend?", "A donkey", ["A horse", "A dragon", "A cat"],
            "Eddie Murphy voiced Donkey. Puss in Boots joined in Shrek 2.",
            wiki("Shrek"), era="modern", difficulty=1)
toon.choice("What kind of animal is Po in Kung Fu Panda?", "A giant panda", ["A red panda", "A bear cub", "A koala"],
            "His kung fu teacher, Master Shifu, is a red panda.",
            wiki("Kung Fu Panda"), era="modern", difficulty=1)
toon.choice("What colour are the Minions?", "Yellow", ["Green", "Blue", "Orange"],
            "The Minions first appeared in Despicable Me in 2010 and speak a jumble of languages.",
            wiki("Minions (Despicable Me)"), era="modern", difficulty=1)
toon.choice("Where does SpongeBob SquarePants live?", "In a pineapple under the sea", ["In a shell on the beach", "In a coconut", "In a sunken ship"],
            "His town is called Bikini Bottom. His creator, Stephen Hillenburg, was a marine biology teacher.",
            wiki("SpongeBob SquarePants"), era="modern", difficulty=1)
toon.choice("What is the name of Peppa Pig's little brother?", "George", ["Richard", "Danny", "Pedro"],
            "George loves his toy dinosaur. Peppa Pig was first shown in 2004.",
            wiki("Peppa Pig"), era="modern", difficulty=1)
toon.choice("Which country is the cartoon Bluey from?", "Australia", ["New Zealand", "Canada", "The United Kingdom"],
            "Bluey is a Blue Heeler puppy from Brisbane.",
            wiki("Bluey (TV series)"), era="modern", difficulty=1)
toon.choice("In Tom and Jerry, which one is the cat?", "Tom", ["Jerry", "Both", "Neither"],
            "Tom and Jerry first appeared in 1940 and won seven Oscars.",
            wiki("Tom and Jerry"), era="classic", difficulty=1)
toon.choice("What breed of dog is Scooby-Doo?", "A Great Dane", ["A Labrador", "A Bloodhound", "A Boxer"],
            "Scooby-Doo first appeared in 1969.",
            wiki("Scooby-Doo (character)"), era="classic", difficulty=2)
toon.choice("Which cartoon rabbit's catchphrase is 'What's up, Doc'?", "Bugs Bunny", ["Roger Rabbit", "Peter Rabbit", "Brer Rabbit"],
            "Bugs Bunny first appeared in 1940, eating a carrot.",
            wiki("Bugs Bunny"), era="classic", difficulty=1)
toon.choice("Which cartoon character keeps trying, and failing, to catch the Road Runner?", "Wile E. Coyote", ["Sylvester", "Taz", "Daffy Duck"],
            "He gets most of his gadgets from the Acme company.",
            wiki("Wile E. Coyote and the Road Runner"), era="classic", difficulty=2)
toon.choice("In which town do the Flintstones live?", "Bedrock", ["Springfield", "Quahog", "Rockville"],
            "The Flintstones, first shown in 1960, was the first animated series on prime-time American TV.",
            wiki("The Flintstones"), era="classic", difficulty=2)
toon.choice("What type of Pokémon is Pikachu?", "Electric", ["Fire", "Water", "Grass"],
            "Pikachu's name mixes the Japanese for an electric crackle, pika, with a mouse's squeak, chu.",
            wiki("Pikachu"), era="modern", difficulty=1)
toon.choice("Which Japanese animated film won the Oscar for Best Animated Feature in 2003?", "Spirited Away", ["My Neighbour Totoro", "Princess Mononoke", "Akira"],
            "It was directed by Hayao Miyazaki of Studio Ghibli.",
            wiki("Spirited Away"), era="modern", difficulty=3)
toon.choice("What breed of dog is Gromit?", "A beagle", ["A terrier", "A spaniel", "A greyhound"],
            "Gromit never speaks. He just raises an eyebrow.",
            wiki("Wallace & Gromit"), difficulty=2)
toon.choice("What breed of dog is Snoopy?", "A beagle", ["A dachshund", "A poodle", "A border collie"],
            "Snoopy belongs to Charlie Brown in Charles Schulz's Peanuts, which began in 1950.",
            wiki("Snoopy"), era="classic", difficulty=2)
toon.choice("In which Welsh town does Fireman Sam work?", "Pontypandy", ["Greendale", "Balamory", "Trumpton"],
            "Greendale is where Postman Pat delivers the post.",
            wiki("Fireman Sam"), era="classic", difficulty=2)
toon.choice("What is the name of Postman Pat's cat?", "Jess", ["Tiddles", "Bagpuss", "Felix"],
            "Jess is a black and white cat who rides in Pat's red van.",
            wiki("Postman Pat"), era="classic", difficulty=2)
toon.choice("How many dwarfs are there in Snow White and the Seven Dwarfs?", "Seven", ["Six", "Eight", "Twelve"],
            "Doc, Grumpy, Happy, Sleepy, Bashful, Sneezy and Dopey.",
            wiki("Seven Dwarfs"), difficulty=1)
toon.choice("Which villain wants a coat made of puppies in 101 Dalmatians?", "Cruella de Vil", ["Ursula", "Maleficent", "Lady Tremaine"],
            "Dodie Smith wrote the original book in 1956.",
            wiki("Cruella de Vil"), difficulty=1)
toon.choice("What is the name of the snowman in Frozen who loves warm hugs?", "Olaf", ["Sven", "Kristoff", "Marshmallow"],
            "Sven is Kristoff's reindeer. Marshmallow is the giant snow monster.",
            wiki("Olaf (Frozen)"), era="modern", difficulty=1)
toon.choice("How does Dumbo the elephant learn to fly?", "With his huge ears", ["With a magic feather only", "With a rocket", "On a crow's back"],
            "The crows give Dumbo a 'magic' feather, but it turns out he never needed it.",
            wiki("Dumbo"), era="classic", difficulty=1)
toon.choice("What happens to Pinocchio's nose when he tells a lie?", "It grows", ["It turns red", "It shrinks", "It sneezes"],
            "Disney's Pinocchio came out in 1940, based on an Italian book by Carlo Collodi.",
            wiki("Pinocchio (1940 film)"), era="classic", difficulty=1)
toon.choice("Which Disney princess has very long magic hair?", "Rapunzel", ["Merida", "Aurora", "Mulan"],
            "Tangled, from 2010, tells Rapunzel's story. Her hair is about 21 metres long.",
            wiki("Tangled"), era="modern", difficulty=1)
toon.choice("In which country is the Pixar film Brave set?", "Scotland", ["Ireland", "Norway", "Wales"],
            "Merida, the heroine, is an expert with a bow and arrow.",
            wiki("Brave (2012 film)"), era="modern", difficulty=1)
toon.higher_lower("Snow White came out in 1937. Did Toy Story come out more or less than 50 years later?", True,
                  "Toy Story came out in 1995, 58 years after Snow White.",
                  wiki("Toy Story"), labels=("More", "Less"), difficulty=2)
toon.yes_no("Is Goofy a dog?", True,
            "Goofy is a dog, just like Pluto, though Goofy walks on two legs and talks.",
            wiki("Goofy"), difficulty=1)
toon.yes_no("Is Winnie-the-Pooh a Disney invention?", False,
            "Pooh was created by the English writer A. A. Milne in 1926. Disney made its first Pooh film in 1966.",
            wiki("Winnie-the-Pooh"), difficulty=2)
toon.yes_no("Was Bluey's family of dogs named after real breeds?", True,
            "Bluey and her family are Blue Heelers and Red Heelers, Australian cattle dogs.",
            wiki("Bluey (TV series)"), era="modern", difficulty=2)
toon.choice("Which studio made the films Toy Story, Up and Inside Out?", "Pixar", ["DreamWorks", "Illumination", "Studio Ghibli"],
            "Pixar began as a computer graphics team at Lucasfilm. Steve Jobs bought it in 1986.",
            wiki("Pixar"), difficulty=1)
toon.choice("Which studio made Shrek and Kung Fu Panda?", "DreamWorks Animation", ["Pixar", "Disney", "Aardman"],
            "DreamWorks was started in 1994 by Steven Spielberg, Jeffrey Katzenberg and David Geffen.",
            wiki("DreamWorks Animation"), era="modern", difficulty=2)
