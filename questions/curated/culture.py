"""Art & Culture, Food & Drink, and Inventions & Brands."""

from . import Category, wiki

art = Category("art")

art.choice("Who painted the Mona Lisa?", "Leonardo da Vinci", ["Michelangelo", "Raphael", "Vincent van Gogh"],
           "Leonardo worked on it on and off for years from about 1503. It hangs in the Louvre in Paris.",
           wiki("Mona Lisa"), difficulty=1)
art.choice("In which museum does the Mona Lisa hang?", "The Louvre, Paris", ["The Uffizi, Florence", "The National Gallery, London", "The Prado, Madrid"],
           "The painting is behind bulletproof glass. It was stolen in 1911 and missing for two years.",
           wiki("Mona Lisa"), difficulty=1)
art.choice("Who painted the ceiling of the Sistine Chapel?", "Michelangelo", ["Leonardo da Vinci", "Raphael", "Botticelli"],
           "Michelangelo painted it between 1508 and 1512, mostly standing up and leaning back, not lying down.",
           wiki("Sistine Chapel ceiling"), difficulty=2)
art.choice("Which artist painted The Starry Night?", "Vincent van Gogh", ["Claude Monet", "Pablo Picasso", "Paul Cézanne"],
           "Van Gogh painted it in 1889 from the window of his room at an asylum in southern France.",
           wiki("The Starry Night"), difficulty=1)
art.true_false("Vincent van Gogh sold hundreds of paintings during his lifetime.", False,
               "He is thought to have sold very few, perhaps just one. He became famous only after his death in 1890.",
               wiki("Vincent van Gogh"), difficulty=2)
art.choice("Which artist is famous for paintings of water lilies in his garden at Giverny?", "Claude Monet", ["Edgar Degas", "Pierre-Auguste Renoir", "Henri Matisse"],
           "Monet painted about 250 water lily pictures over the last 30 years of his life.",
           wiki("Water Lilies (Monet series)"), difficulty=2)
art.choice("Which Spanish artist helped invent the style called Cubism?", "Pablo Picasso", ["Salvador Dalí", "Joan Miró", "Diego Velázquez"],
           "Picasso and Georges Braque developed Cubism, showing objects from several angles at once.",
           wiki("Cubism"), difficulty=2)
art.choice("Which artist painted melting clocks in The Persistence of Memory?", "Salvador Dalí", ["René Magritte", "Pablo Picasso", "Frida Kahlo"],
           "Dalí painted it in 1931. It's in the Museum of Modern Art in New York.",
           wiki("The Persistence of Memory"), difficulty=2)
art.choice("Which American artist made pictures of Campbell's soup cans?", "Andy Warhol", ["Roy Lichtenstein", "Jackson Pollock", "Keith Haring"],
           "Warhol's 32 Campbell's Soup Cans, from 1962, helped make Pop Art famous.",
           wiki("Campbell's Soup Cans"), era="classic", difficulty=2)
art.choice("Which artist painted The Scream?", "Edvard Munch", ["Vincent van Gogh", "Gustav Klimt", "Egon Schiele"],
           "Munch, from Norway, made several versions of The Scream, starting in 1893.",
           wiki("The Scream"), difficulty=2)
art.choice("Which Mexican artist is famous for her self-portraits?", "Frida Kahlo", ["Georgia O'Keeffe", "Tamara de Lempicka", "Mary Cassatt"],
           "Frida Kahlo painted 55 self-portraits. Her home in Mexico City, the Blue House, is now a museum.",
           wiki("Frida Kahlo"), difficulty=2)
art.choice("Which Dutch artist painted Girl with a Pearl Earring?", "Johannes Vermeer", ["Rembrandt", "Vincent van Gogh", "Frans Hals"],
           "Vermeer painted it around 1665. It's in the Mauritshuis gallery in The Hague.",
           wiki("Girl with a Pearl Earring"), difficulty=3)
art.choice("Which mystery street artist's works appear on walls, mostly in Britain?", "Banksy", ["Stik", "Shepard Fairey", "Invader"],
           "Banksy is from the Bristol area. Nobody has officially confirmed who Banksy is.",
           wiki("Banksy"), era="modern", difficulty=1)
art.choice("Which huge steel sculpture with outstretched wings stands near Gateshead?", "The Angel of the North", ["The Kelpies", "The Spirit of Ecstasy", "The Iron Man"],
           "Antony Gormley's Angel of the North went up in 1998. Its wings are 54 metres across, almost as wide as a jumbo jet's.",
           wiki("Angel of the North"), era="modern", difficulty=2)
art.choice("Which museum in London is home to the Rosetta Stone?", "The British Museum", ["The Natural History Museum", "The Science Museum", "The V&A"],
           "The Rosetta Stone has the same text in three scripts, which helped experts finally read Egyptian hieroglyphs.",
           wiki("Rosetta Stone"), difficulty=2)
art.choice("Which London museum has a huge blue whale skeleton hanging in its main hall?", "The Natural History Museum", ["The British Museum", "The Science Museum", "Tate Modern"],
           "The skeleton is nicknamed Hope. It replaced Dippy the dinosaur cast in the main hall in 2017.",
           wiki("Natural History Museum, London"), era="modern", difficulty=2)
art.choice("Which London gallery is in an old power station on the River Thames?", "Tate Modern", ["The National Gallery", "The Saatchi Gallery", "Somerset House"],
           "Tate Modern opened in 2000 in the old Bankside Power Station. Its chimney is 99 metres tall.",
           wiki("Tate Modern"), era="modern", difficulty=2)
art.choice("Which museum is the most visited art museum in the world?", "The Louvre", ["The British Museum", "The Metropolitan Museum of Art", "The Vatican Museums"],
           "The Louvre welcomes around 9 million visitors a year.",
           wiki("List of most-visited art museums"), era="modern", difficulty=2, as_of="2025")
art.choice("Which famous statue by Michelangelo shows a young man about to fight Goliath?", "David", ["The Thinker", "Venus de Milo", "Moses"],
           "Michelangelo carved David from a single block of marble between 1501 and 1504. It's over 5 metres tall.",
           wiki("David (Michelangelo)"), difficulty=2)
art.choice("Who sculpted The Thinker?", "Auguste Rodin", ["Michelangelo", "Donatello", "Henry Moore"],
           "Rodin's Thinker was first designed as part of a huge doorway called The Gates of Hell.",
           wiki("The Thinker"), difficulty=3)
art.choice("What are the three primary colours in traditional painting?", "Red, yellow and blue", ["Red, green and blue", "Orange, green and purple", "Black, white and grey"],
           "Mix any two primaries and you get a secondary colour: orange, green or purple.",
           wiki("Primary color"), difficulty=1)
art.choice("What do you call a painting of a bowl of fruit, flowers or other objects?", "A still life", ["A landscape", "A portrait", "A mural"],
           "Still lifes were hugely popular in the Netherlands in the 1600s.",
           wiki("Still life"), difficulty=2)
art.choice("Which language has the most native speakers in the world?", "Mandarin Chinese", ["English", "Spanish", "Hindi"],
           "Mandarin has more native speakers than any other language. English has the most speakers when you count those who learned it.",
           wiki("List of languages by number of native speakers"), era="modern", difficulty=2, as_of="2025")
art.choice("Which alphabet do Russian, Ukrainian and Bulgarian use?", "Cyrillic", ["Latin", "Greek", "Arabic"],
           "The Cyrillic alphabet is named after Saint Cyril, a Byzantine monk from the 800s.",
           wiki("Cyrillic script"), difficulty=3)
art.choice("In which country do thousands of people throw tomatoes at each other in the La Tomatina festival?", "Spain", ["Italy", "Portugal", "Mexico"],
           "La Tomatina takes place in the town of Buñol, near Valencia, on the last Wednesday of August.",
           wiki("La Tomatina"), difficulty=2)
art.choice("In which country did origami, the art of paper folding, become famous?", "Japan", ["China", "Korea", "India"],
           "The word origami comes from the Japanese words for 'folding' and 'paper'.",
           wiki("Origami"), difficulty=1)
art.choice("Which country gave the world the Day of the Dead festival?", "Mexico", ["Spain", "Brazil", "Peru"],
           "Día de los Muertos is held on 1 and 2 November. Families remember loved ones with bright altars and marigolds.",
           wiki("Day of the Dead"), difficulty=2)
art.choice("Which famous theatre district in London is known for its musicals?", "The West End", ["Broadway", "Soho Square", "The South Bank"],
           "Broadway is New York's equivalent. The West End's longest-running musical is Les Misérables.",
           wiki("West End theatre"), difficulty=2)
art.choice("Which ballet tells the story of a princess who is turned into a swan?", "Swan Lake", ["The Nutcracker", "Giselle", "Sleeping Beauty"],
           "Tchaikovsky wrote the music for Swan Lake, first performed in Moscow in 1877.",
           wiki("Swan Lake"), difficulty=1)
art.choice("Which author created Sherlock Holmes?", "Arthur Conan Doyle", ["Agatha Christie", "Charles Dickens", "H. G. Wells"],
           "Sherlock Holmes first appeared in A Study in Scarlet in 1887. He lived at 221B Baker Street.",
           wiki("Sherlock Holmes"), difficulty=2)
art.choice("Which crime writer is the best-selling novelist of all time?", "Agatha Christie", ["Arthur Conan Doyle", "Stephen King", "Ian Fleming"],
           "Guinness World Records says her books have sold around 2 billion copies.",
           wiki("Agatha Christie"), difficulty=2, as_of="2026-11")
art.choice("Which designer is famous for the 'little black dress' and the perfume No. 5?", "Coco Chanel", ["Christian Dior", "Vivienne Westwood", "Yves Saint Laurent"],
           "Chanel No. 5 was launched in 1921.",
           wiki("Coco Chanel"), era="classic", difficulty=2)
art.choice("Which famous London Underground design, first printed in 1933, shows lines as straight colours?", "Harry Beck's Tube map", ["The Oyster card", "The roundel", "The Routemaster"],
           "Harry Beck drew it like an electrical circuit, ignoring real distances. Metro maps around the world copied the idea.",
           wiki("Tube map"), era="classic", difficulty=3)
art.choice("Which tall red vehicle, designed in London, became a symbol of the city?", "The Routemaster bus", ["The black cab", "The Mini", "The Tube train"],
           "The Routemaster entered service in 1956 and had an open platform at the back.",
           wiki("AEC Routemaster"), era="classic", difficulty=2)
art.choice("Which ancient people built the pyramids and wrote in hieroglyphs?", "The Ancient Egyptians", ["The Romans", "The Greeks", "The Aztecs"],
           "Hieroglyphs used more than 700 different pictures and symbols.",
           wiki("Egyptian hieroglyphs"), difficulty=1)

food = Category("food")

food.choice("Which country did pizza Margherita come from?", "Italy", ["Greece", "France", "The United States"],
            "The story goes that it was named after Queen Margherita in Naples in 1889. Its colours match the Italian flag.",
            wiki("Pizza Margherita"), difficulty=1)
food.choice("What is the main ingredient of guacamole?", "Avocado", ["Peas", "Cucumber", "Lime"],
            "Guacamole was first made by the Aztecs in what is now Mexico.",
            wiki("Guacamole"), difficulty=1)
food.choice("What is the main ingredient of hummus?", "Chickpeas", ["Lentils", "Broad beans", "Rice"],
            "Hummus is chickpeas blended with tahini (sesame paste), lemon juice and garlic.",
            wiki("Hummus"), difficulty=1)
food.choice("Which country is the home of sushi?", "Japan", ["China", "Thailand", "Korea"],
            "Sushi began as a way of keeping fish in fermented rice. Today the word refers to the vinegared rice, not the fish.",
            wiki("Sushi"), difficulty=1)
food.choice("What is paella's main ingredient?", "Rice", ["Pasta", "Potatoes", "Bread"],
            "Paella comes from Valencia, in Spain. It is named after the wide, flat pan it's cooked in.",
            wiki("Paella"), difficulty=1)
food.choice("Which nut is used to make marzipan?", "Almonds", ["Peanuts", "Walnuts", "Cashews"],
            "Marzipan is ground almonds mixed with sugar. It's the layer under the icing on a traditional Christmas cake.",
            wiki("Marzipan"), difficulty=2)
food.choice("What makes bread dough rise?", "Gas made by yeast", ["Salt", "Steam from the oven", "Sugar crystals"],
            "Yeast feeds on sugars in the flour and gives off carbon dioxide, which makes bubbles in the dough.",
            wiki("Baker's yeast"), difficulty=2)
food.yes_no("Does white chocolate contain cocoa solids?", False,
            "White chocolate is made from cocoa butter, sugar and milk, but no cocoa solids. That's why it isn't brown.",
            wiki("White chocolate"), difficulty=2)
food.choice("Which country produces the most cocoa beans?", "Côte d'Ivoire", ["Brazil", "Switzerland", "Belgium"],
            "Côte d'Ivoire (Ivory Coast) and Ghana grow more than half of the world's cocoa.",
            wiki("Cocoa bean"), era="modern", difficulty=3, as_of="2025")
food.choice("Which fruit is dried to make raisins?", "Grapes", ["Plums", "Apricots", "Figs"],
            "Dried plums are prunes.",
            wiki("Raisin"), difficulty=1)
food.choice("What is the spicy heat in chilli peppers measured in?", "Scoville units", ["Celsius", "Calories", "Decibels"],
            "The scale is named after Wilbur Scoville, an American chemist, who came up with it in 1912.",
            wiki("Scoville scale"), difficulty=2)
food.choice("Which drink is made from fermented apples?", "Cider", ["Perry", "Mead", "Kombucha"],
            "Perry is made from pears and mead from honey.",
            wiki("Cider"), difficulty=2)
food.choice("Which country drinks the most tea per person?", "Turkey", ["The United Kingdom", "China", "India"],
            "People in Turkey drink about 3 kg of tea per person each year, more than anywhere else.",
            wiki("Tea in Turkey"), era="modern", difficulty=3, as_of="2025")
food.choice("Which British dish is battered fish served with chips?", "Fish and chips", ["Bangers and mash", "Toad in the hole", "Shepherd's pie"],
            "Fish and chips became popular in the 1860s. It was one of the few foods not rationed in the Second World War.",
            wiki("Fish and chips"), difficulty=1)
food.choice("What is toad in the hole?", "Sausages in batter", ["A frog dish", "A jacket potato", "Egg on toast"],
            "The sausages are baked in Yorkshire pudding batter.",
            wiki("Toad in the hole"), difficulty=1)
food.choice("Which vegetable is used to make traditional chips and crisps?", "Potato", ["Parsnip", "Carrot", "Sweet potato"],
            "Potatoes came to Europe from South America in the late 1500s.",
            wiki("Potato"), difficulty=1)
food.choice("Which country did the croissant become famous in?", "France", ["Italy", "Belgium", "Switzerland"],
            "The croissant is French but takes its idea from the kipferl, an Austrian crescent-shaped bread.",
            wiki("Croissant"), difficulty=1)
food.choice("Which cheese is traditionally used on a pizza Margherita?", "Mozzarella", ["Cheddar", "Parmesan", "Brie"],
            "Proper mozzarella is made from the milk of water buffalo or cows.",
            wiki("Mozzarella"), difficulty=1)
food.choice("Which country is famous for Gouda and Edam cheese?", "The Netherlands", ["Switzerland", "Denmark", "Belgium"],
            "Both are named after Dutch towns.",
            wiki("Gouda cheese"), difficulty=2)
food.choice("Which spice is the most expensive by weight?", "Saffron", ["Vanilla", "Cinnamon", "Cardamom"],
            "Saffron comes from the tiny threads inside crocus flowers. It takes about 150 flowers to make one gram.",
            wiki("Saffron"), difficulty=2, as_of="2026-11")
food.choice("Which grain is used to make most beer?", "Barley", ["Rice", "Oats", "Corn"],
            "Barley is malted: soaked so it starts to sprout, then dried.",
            wiki("Beer"), difficulty=3)
food.choice("What is tofu made from?", "Soya beans", ["Rice", "Chickpeas", "Wheat"],
            "Tofu is made by curdling soya milk, a bit like making cheese.",
            wiki("Tofu"), difficulty=2)
food.choice("Which is the traditional main course for a British Christmas dinner?", "Roast turkey", ["Roast beef", "Roast goose", "Salmon"],
            "Turkey became the favourite in the 20th century. In Victorian times, goose was more common.",
            wiki("Christmas dinner"), difficulty=1)
food.choice("What are Brussels sprouts named after?", "Brussels, the capital of Belgium", ["A chef called Mr Brussels", "A kind of carpet", "Bristol"],
            "Sprouts have been grown around Brussels since at least the 1500s.",
            wiki("Brussels sprout"), difficulty=1)
food.choice("Which American city is famous for the deep-dish pizza?", "Chicago", ["New York", "Boston", "Detroit"],
            "Chicago deep-dish pizza is baked in a tall pan, with the sauce on top of the cheese.",
            wiki("Chicago-style pizza"), difficulty=2)
food.choice("What is wasabi?", "A hot green paste served with sushi", ["A Japanese noodle", "A kind of seaweed", "A rice wine"],
            "Real wasabi is a root. Most wasabi outside Japan is actually horseradish coloured green.",
            wiki("Wasabi"), difficulty=2)
food.yes_no("Is a peanut a nut?", False,
            "Peanuts are legumes, like peas and beans. They grow underground.",
            wiki("Peanut"), difficulty=2)
food.yes_no("Is a strawberry, scientifically speaking, a berry?", False,
            "Botanists don't count strawberries as berries, but bananas, grapes and even tomatoes are.",
            wiki("Strawberry"), difficulty=3)
food.choice("Which food never goes off if it's sealed and kept dry?", "Honey", ["Bread", "Cheese", "Milk"],
            "Archaeologists have found pots of honey in ancient Egyptian tombs that were still edible.",
            wiki("Honey"), difficulty=2)
food.choice("Which country invented the hamburger, named after a German city?", "The United States", ["Germany", "The United Kingdom", "Austria"],
            "The burger as we know it was created in America in the late 1800s. The name comes from Hamburg in Germany.",
            wiki("Hamburger"), difficulty=3)
food.choice("Which vitamin do oranges have a lot of?", "Vitamin C", ["Vitamin D", "Vitamin B12", "Vitamin K"],
            "Sailors once ate citrus fruit on long voyages to stop scurvy, a disease caused by a lack of vitamin C.",
            wiki("Vitamin C"), difficulty=1)
food.choice("Which country drinks the most coffee per person?", "Finland", ["Italy", "The United States", "Brazil"],
            "Finns drink around 12 kg of coffee per person a year, more than anywhere else.",
            wiki("Coffee in Finland"), era="modern", difficulty=3, as_of="2025")
food.choice("Which famous dessert is named after a Russian ballerina?", "Pavlova", ["Tiramisu", "Crème brûlée", "Baked Alaska"],
            "Pavlova was created in honour of Anna Pavlova during her tour of Australia and New Zealand in the 1920s. Both countries claim it.",
            wiki("Pavlova (cake)"), difficulty=2)
food.choice("What is a Yorkshire pudding made from?", "Batter of eggs, flour and milk", ["Mashed potato", "Bread and butter", "Rice"],
            "Yorkshire puddings were first served before the meat, to fill people up.",
            wiki("Yorkshire pudding"), difficulty=1)
food.choice("Which country is the world's biggest producer of olive oil?", "Spain", ["Italy", "Greece", "Turkey"],
            "Spain usually makes far more olive oil than any other country, often close to half the world's supply.",
            wiki("Olive oil"), era="modern", difficulty=2, as_of="2025")

tech = Category("inventions")

tech.choice("Who invented the telephone, patenting it in 1876?", "Alexander Graham Bell", ["Thomas Edison", "Nikola Tesla", "Guglielmo Marconi"],
            "Bell's first words on the phone were to his assistant: 'Mr. Watson, come here, I want to see you.'",
            wiki("Alexander Graham Bell"), difficulty=1)
tech.choice("Which Scottish inventor first showed a working television in 1926?", "John Logie Baird", ["James Watt", "Alexander Fleming", "Alexander Graham Bell"],
            "Baird demonstrated moving pictures on television in London on 26 January 1926.",
            wiki("John Logie Baird"), era="classic", difficulty=2)
tech.choice("In which year did Apple launch the first iPhone?", "2007", ["2004", "2010", "2001"],
            "Steve Jobs unveiled the iPhone in January 2007, calling it 'an iPod, a phone and an internet communicator'.",
            wiki("IPhone (1st generation)"), era="modern", difficulty=2)
tech.choice("Who founded Apple with Steve Wozniak in 1976?", "Steve Jobs", ["Bill Gates", "Elon Musk", "Jeff Bezos"],
            "Apple started in a garage in California. Its first product was the Apple I computer.",
            wiki("Apple Inc."), difficulty=1)
tech.choice("Who founded Microsoft with Paul Allen?", "Bill Gates", ["Steve Jobs", "Mark Zuckerberg", "Larry Page"],
            "Microsoft was founded in 1975. Its Windows software runs on most of the world's personal computers.",
            wiki("Microsoft"), difficulty=1)
tech.choice("In which year was Google founded?", "1998", ["1994", "2004", "2001"],
            "Larry Page and Sergey Brin started Google in a friend's garage. The name comes from 'googol', a 1 followed by 100 zeros.",
            wiki("Google"), era="modern", difficulty=2)
tech.choice("Which Danish company makes plastic building bricks?", "LEGO", ["Mega Bloks", "K'Nex", "Meccano"],
            "The name comes from the Danish 'leg godt', meaning 'play well'. The company began in 1932.",
            wiki("Lego"), difficulty=1)
tech.choice("Which Japanese company makes Mario and the Switch?", "Nintendo", ["Sony", "Sega", "Capcom"],
            "Nintendo was founded in 1889 to make playing cards.",
            wiki("Nintendo"), difficulty=1)
tech.yes_no("Did Nintendo start out making playing cards?", True,
            "Nintendo began in Kyoto in 1889, making hanafuda cards. It only moved into video games in the 1970s.",
            wiki("Nintendo"), difficulty=2)
tech.choice("Which country do Volvo cars come from?", "Sweden", ["Germany", "Norway", "Finland"],
            "Volvo means 'I roll' in Latin. The first Volvo car was built in 1927.",
            wiki("Volvo Cars"), difficulty=2)
tech.choice("Which country is the car maker Ferrari from?", "Italy", ["Germany", "France", "Spain"],
            "Ferrari is based in Maranello. Its prancing horse badge was first used on a First World War pilot's plane.",
            wiki("Ferrari"), difficulty=1)
tech.choice("Which country is Toyota from?", "Japan", ["South Korea", "China", "The United States"],
            "Toyota is one of the world's biggest car makers. The company began by making weaving looms.",
            wiki("Toyota"), difficulty=1)
tech.choice("Which German car maker's name means 'people's car'?", "Volkswagen", ["Mercedes-Benz", "Audi", "Porsche"],
            "Its most famous model, the Beetle, was made from 1938 to 2003.",
            wiki("Volkswagen"), difficulty=2)
tech.choice("Which British car, launched in 1959, had its wheels pushed right into the corners to save space?", "The Mini", ["The Jaguar E-Type", "The Ford Escort", "The Land Rover"],
            "Alec Issigonis designed the Mini. It starred in the 1969 film The Italian Job.",
            wiki("Mini"), era="classic", difficulty=2)
tech.choice("Which company makes the electric cars Model 3 and Model Y?", "Tesla", ["Rivian", "BYD", "Polestar"],
            "Tesla is named after the inventor Nikola Tesla.",
            wiki("Tesla, Inc."), era="modern", difficulty=1)
tech.choice("Who invented the light bulb that became a commercial success, in 1879?", "Thomas Edison", ["Alexander Graham Bell", "Nikola Tesla", "Benjamin Franklin"],
            "Edison didn't invent the first electric light, but his long-lasting bulb was the one that caught on. Joseph Swan made a similar bulb in England.",
            wiki("Incandescent light bulb"), difficulty=2)
tech.choice("Which Scottish engineer improved the steam engine so much that a unit of power is named after him?", "James Watt", ["George Stephenson", "Isambard Kingdom Brunel", "Richard Trevithick"],
            "A watt measures power. A typical LED light bulb uses about 10 watts.",
            wiki("James Watt"), difficulty=2)
tech.choice("Which steam locomotive, built by George and Robert Stephenson, won the Rainhill Trials in 1829?", "Rocket", ["The Flying Scotsman", "Mallard", "Puffing Billy"],
            "Rocket reached about 30 mph, an astonishing speed at the time.",
            wiki("Stephenson's Rocket"), era="classic", difficulty=3)
tech.choice("Which steam locomotive holds the world speed record for steam, set in 1938?", "Mallard", ["The Flying Scotsman", "Rocket", "Tornado"],
            "Mallard reached 126 mph on 3 July 1938. The record still stands.",
            wiki("LNER Class A4 4468 Mallard"), era="classic", difficulty=3)
tech.choice("Which engineer designed the Clifton Suspension Bridge and built the Great Western Railway?", "Isambard Kingdom Brunel", ["Thomas Telford", "George Stephenson", "James Watt"],
            "Brunel also designed the SS Great Britain, the first iron-hulled ship driven by a propeller to cross the Atlantic.",
            wiki("Isambard Kingdom Brunel"), era="classic", difficulty=3)
tech.choice("What did Johannes Gutenberg invent in Germany in the 1400s?", "A printing press with movable type", ["The telescope", "The mechanical clock", "Paper"],
            "Gutenberg's press made books much cheaper and faster to produce. His Bible was printed around 1455.",
            wiki("Printing press"), difficulty=2)
tech.choice("What does 'www' stand for in a web address?", "World Wide Web", ["Wide World Website", "Web Within Web", "World Web Window"],
            "Tim Berners-Lee published the first website in 1991. A copy of it is still online.",
            wiki("World Wide Web"), era="modern", difficulty=1)
tech.choice("What does 'USB' stand for?", "Universal Serial Bus", ["United System Board", "Universal Storage Box", "Ultra Speed Bus"],
            "The first USB standard came out in 1996.",
            wiki("USB"), era="modern", difficulty=3)
tech.choice("Which company created the PlayStation?", "Sony", ["Nintendo", "Microsoft", "Sega"],
            "The first PlayStation came out in Japan in December 1994.",
            wiki("PlayStation (console)"), era="modern", difficulty=1)
tech.choice("Which company makes the Xbox?", "Microsoft", ["Sony", "Nintendo", "Apple"],
            "The first Xbox came out in 2001.",
            wiki("Xbox"), era="modern", difficulty=1)
tech.choice("Which game, about placing and breaking blocks, is the best-selling video game of all time?", "Minecraft", ["Tetris", "Grand Theft Auto V", "Fortnite"],
            "Minecraft has sold more than 300 million copies since it came out in 2011.",
            wiki("Minecraft"), era="modern", difficulty=1, as_of="2026-11")
tech.choice("Which Soviet video game has falling blocks called tetrominoes?", "Tetris", ["Pac-Man", "Space Invaders", "Snake"],
            "Alexey Pajitnov created Tetris in Moscow in 1984.",
            wiki("Tetris"), era="classic", difficulty=2)
tech.choice("Which yellow character eats dots and is chased by ghosts?", "Pac-Man", ["Sonic", "Kirby", "Mario"],
            "Pac-Man came out in Japan in 1980. Its designer said he got the idea from a pizza with a slice taken out.",
            wiki("Pac-Man"), era="classic", difficulty=1)
tech.choice("Which British inventor came up with the bagless vacuum cleaner?", "James Dyson", ["Clive Sinclair", "Trevor Baylis", "Alan Sugar"],
            "James Dyson made 5,127 prototypes over five years before getting it right.",
            wiki("James Dyson"), era="modern", difficulty=2)
tech.choice("Which was invented first?", "The bicycle", ["The car", "The aeroplane", "The television"],
            "The first pedal bicycles appeared in the 1860s. Karl Benz's car came in 1885, and the Wright brothers flew in 1903.",
            wiki("History of the bicycle"), difficulty=2)
tech.higher_lower("The first text message was sent in 1992. Was the first email sent before or after that?", True,
                  "Ray Tomlinson sent the first networked email in 1971, more than 20 years earlier.",
                  wiki("Email"), labels=("Before", "After"), era="classic", difficulty=2)
tech.choice("What were the words of the first text message, sent in 1992?", "Merry Christmas", ["Hello world", "Can you hear me?", "Testing, testing"],
            "Engineer Neil Papworth sent it from a computer to a Vodafone phone on 3 December 1992.",
            wiki("SMS"), era="classic", difficulty=3)
tech.choice("Which company's logo is a bitten apple?", "Apple", ["BlackBerry", "Android", "Orange"],
            "The bite was added so the apple wouldn't be mistaken for a cherry.",
            wiki("Apple Inc."), difficulty=1)
tech.choice("Which social network's founder, Mark Zuckerberg, started it at university in 2004?", "Facebook", ["Twitter", "Instagram", "Snapchat"],
            "Facebook began at Harvard University. Its parent company is now called Meta.",
            wiki("Facebook"), era="modern", difficulty=1)
tech.choice("Which NASA rover has been exploring Mars since 2021?", "Perseverance", ["Curiosity", "Sojourner", "Spirit"],
            "Perseverance landed in February 2021, carrying a small helicopter called Ingenuity.",
            wiki("Perseverance (rover)"), era="modern", difficulty=3)

assert (len(art.questions), len(food.questions), len(tech.questions)) == (35, 35, 35), (len(art.questions), len(food.questions), len(tech.questions))
