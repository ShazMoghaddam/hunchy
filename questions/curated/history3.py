"""More history, and more maths, space and nature questions to round out those subjects."""

from . import Category, wiki

history = Category("history", prefix="history3")
maths = Category("maths", prefix="maths2")
space = Category("space", prefix="space3")
nature = Category("nature", prefix="nature3")

# History -------------------------------------------------------------------------------------------
history.choice("Which stone, found in Egypt in 1799, finally let scholars read hieroglyphs?", "The Rosetta Stone", ["The Blarney Stone", "The Stone of Destiny", "The Moonstone"],
               "It has the same message in three scripts. Jean-François Champollion cracked the hieroglyphs in 1822.",
               wiki("Rosetta Stone"), difficulty=2)
history.choice("In which year did the Pilgrims sail from Plymouth to America on the Mayflower?", "1620", ["1492", "1588", "1776"],
               "Their first harvest feast the next year is remembered at Thanksgiving.",
               wiki("Mayflower"), difficulty=3)
history.choice("What was the world's first sticky postage stamp, issued in Britain in 1840?", "The Penny Black", ["The Twopenny Blue", "The Red Penny", "The Victoria Gold"],
               "It shows the head of a young Queen Victoria. Before it, the person receiving a letter usually paid.",
               wiki("Penny Black"), difficulty=2)
history.choice("In which year did Concorde, the supersonic airliner, make its last passenger flight?", "2003", ["1989", "1996", "2010"],
               "Concorde could cross the Atlantic in about three and a half hours, half the time of a normal jet.",
               wiki("Concorde"), difficulty=2)
history.choice("Which giant German airship burst into flames in New Jersey in 1937?", "The Hindenburg", ["The Graf Zeppelin", "The R101", "The Bismarck"],
               "It was filled with hydrogen, which burns easily. It ended the age of airship travel.",
               wiki("Hindenburg disaster"), era="classic", difficulty=2)
history.choice("In which year did the city of Constantinople, now Istanbul, fall to the Ottoman Turks?", "1453", ["1066", "1215", "1666"],
               "Many historians use 1453 to mark the end of the Middle Ages.",
               wiki("Fall of Constantinople"), difficulty=3)
history.choice("At which battle in 1415 did Henry V's archers beat a much larger French army?", "Agincourt", ["Hastings", "Bosworth", "Crécy"],
               "Shakespeare wrote about it in his play Henry V.",
               wiki("Battle of Agincourt"), difficulty=2)
history.choice("Who was the last Tudor monarch?", "Elizabeth I", ["Henry VIII", "Mary I", "James I"],
               "She never married or had children, so the crown passed to her cousin James VI of Scotland in 1603.",
               wiki("Elizabeth I"), difficulty=2)
history.choice("Which huge glass building in London's Hyde Park housed the Great Exhibition of 1851?", "The Crystal Palace", ["The Royal Albert Hall", "The Palm House", "The Glasshouse"],
               "It was moved to south London afterwards and burned down in 1936. The area is still called Crystal Palace.",
               wiki("The Crystal Palace"), difficulty=2)
history.choice("Which ancient trade route linked China with the Mediterranean?", "The Silk Road", ["The Spice Trail", "The Amber Way", "The Jade Highway"],
               "Silk, spices, paper and ideas travelled along it for more than 1,500 years.",
               wiki("Silk Road"), difficulty=1)
history.choice("Which British law of 1807 banned the trade in enslaved people across the British Empire?", "The Slave Trade Act", ["The Magna Carta", "The Reform Act", "The Bill of Rights"],
               "Campaigners such as William Wilberforce and Olaudah Equiano had fought for it for 20 years. Slavery itself was abolished across most of the empire in 1834.",
               wiki("Slave Trade Act 1807"), difficulty=3)
history.choice("In which year did the Model T Ford go on sale, the first car many ordinary people could afford?", "1908", ["1885", "1927", "1946"],
               "Ford's moving assembly line, from 1913, cut the time to build one from about 12 hours to about 90 minutes.",
               wiki("Ford Model T"), difficulty=3)
history.choice("In which year did scientists describe the double-helix shape of DNA?", "1953", ["1903", "1929", "1979"],
               "James Watson and Francis Crick announced it in Cambridge, helped by Rosalind Franklin's X-ray photos.",
               wiki("Nucleic acid double helix"), difficulty=3)
history.choice("Which ship carried Charles Darwin round the world from 1831 to 1836?", "HMS Beagle", ["HMS Victory", "The Endeavour", "The Golden Hind"],
               "The voyage was meant to last two years but took almost five.",
               wiki("Second voyage of HMS Beagle"), difficulty=2)
history.choice("Which English sailor captained the Golden Hind round the world from 1577 to 1580?", "Francis Drake", ["Walter Raleigh", "James Cook", "Horatio Nelson"],
               "He was the first captain to sail round the world and survive the whole trip. Magellan died on the way.",
               wiki("Francis Drake"), difficulty=2)
history.choice("Which famous ship, Henry VIII's favourite, sank in 1545 and was raised from the sea in 1982?", "The Mary Rose", ["The Victory", "The Cutty Sark", "The Golden Hind"],
               "About 60 million people around the world watched it come up on TV. It's now in a museum in Portsmouth.",
               wiki("Mary Rose"), difficulty=2)
history.yes_no("Did the Great Wall of China start as many separate walls?", True,
               "Different kingdoms built walls from the 7th century BC. China's first emperor, Qin Shi Huang, began joining them up.",
               wiki("Great Wall of China"), difficulty=3)
history.choice("Which Mayan creation, carved on stone, led to rumours that the world would end in 2012?", "A calendar", ["A map", "A list of kings", "A star chart"],
               "A long cycle of the Maya Long Count calendar ended in December 2012. To the Maya, it simply meant the start of a new one.",
               wiki("2012 phenomenon"), era="modern", difficulty=2)
history.choice("In which year did the world's first inter-city railway, between Liverpool and Manchester, open?", "1830", ["1780", "1855", "1901"],
               "It was the first line to use only steam engines, with timetables and tickets.",
               wiki("Liverpool and Manchester Railway"), era="classic", difficulty=3)

# Maths ---------------------------------------------------------------------------------------------
maths.yes_no("Is 1 a prime number?", False,
             "A prime has exactly two different factors: 1 and itself. 1 has only one, so it doesn't count.",
             wiki("Prime number"), difficulty=2)
maths.yes_no("Is 2 the only even prime number?", True,
             "Every other even number can be divided by 2, so it can't be prime.",
             wiki("Prime number"), difficulty=2)
maths.choice("What is a googol?", "1 followed by 100 zeros", ["The biggest number there is", "1 followed by a million zeros", "A number that never ends"],
             "The name was made up by a nine-year-old boy in 1920. Google's name is a play on it.",
             wiki("Googol"), difficulty=2)
maths.choice("Pi, the distance round a circle divided by the distance across, starts with which digits?", "3.14", ["3.41", "2.71", "1.61"],
             "Pi goes on for ever without repeating. Computers have worked out trillions of its digits.",
             wiki("Pi"), difficulty=1)
maths.yes_no("Was the year 1900 a leap year?", False,
             "Years ending in 00 are only leap years if they divide by 400. So 2000 was a leap year, but 1900 wasn't.",
             wiki("Leap year"), difficulty=3)
maths.choice("On an ordinary dice, what do the numbers on opposite faces always add up to?", "7", ["6", "8", "10"],
             "1 is opposite 6, 2 is opposite 5, and 3 is opposite 4.",
             wiki("Dice"), difficulty=2)
maths.higher_lower("In a room of 23 people, is the chance that two share a birthday more or less than 50%?", True,
                   "It's just over 50%. It feels too high, which is why it's called the birthday paradox. With 70 people it's over 99.9%.",
                   wiki("Birthday problem"), labels=("More", "Less"), difficulty=3)
maths.choice("Who invented the equals sign (=), in 1557?", "Robert Recorde, from Wales", ["Isaac Newton, from England", "Leonhard Euler, from Switzerland", "Pythagoras, from Greece"],
             "He chose two parallel lines because 'no two things can be more equal'.",
             wiki("Robert Recorde"), era="classic", difficulty=3)
maths.choice("How many is a 'score'?", "20", ["12", "50", "100"],
             "Abraham Lincoln's Gettysburg Address begins 'Four score and seven years ago', meaning 87.",
             wiki("Score (unit)"), era="classic", difficulty=2)
maths.choice("How many is a 'gross'?", "144", ["100", "120", "1,000"],
             "A gross is a dozen dozens: 12 × 12.",
             wiki("Gross (unit)"), era="classic", difficulty=3)
maths.choice("Which ancient Greek gave his name to the rule about the sides of a right-angled triangle?", "Pythagoras", ["Archimedes", "Euclid", "Plato"],
             "The square on the longest side equals the squares on the other two sides added together.",
             wiki("Pythagorean theorem"), difficulty=1)
maths.choice("Which country's mathematicians first treated zero as a number in its own right?", "India", ["Egypt", "Greece", "China"],
             "The mathematician Brahmagupta wrote rules for using zero in the year 628.",
             wiki("0"), difficulty=3)
maths.choice("Which shape do bees use for the cells in a honeycomb?", "The hexagon", ["The square", "The triangle", "The circle"],
             "Hexagons fit together with no gaps and use the least wax to hold the most honey.",
             wiki("Honeycomb conjecture"), difficulty=1)
maths.choice("What is the name for a triangle with all three sides the same length?", "Equilateral", ["Isosceles", "Scalene", "Right-angled"],
             "All three of its angles are 60°.",
             wiki("Equilateral triangle"), difficulty=2)
maths.choice("How many edges does a cube have?", "12", ["6", "8", "24"],
             "A cube has 6 faces, 8 corners and 12 edges.",
             wiki("Cube"), difficulty=2)

# Space ---------------------------------------------------------------------------------------------
space.choice("What mostly causes the tides in Earth's seas?", "The pull of the Moon", ["The wind", "The Earth's spin alone", "Underwater volcanoes"],
             "The Sun's pull helps too. When they line up, we get extra-high 'spring tides'.",
             wiki("Tide"), difficulty=1)
space.higher_lower("Is the Sun more or less than 100 times wider than the Earth?", True,
                   "It's about 109 times as wide. About 1.3 million Earths would fit inside it.",
                   wiki("Sun"), labels=("More", "Less"), difficulty=2)
space.yes_no("Is a day on Venus longer than a year on Venus?", True,
             "Venus takes 243 Earth days to spin round once, but only 225 days to go round the Sun. It also spins backwards.",
             wiki("Venus"), difficulty=2)
space.choice("How many moons does Mars have?", "2", ["0", "1", "4"],
             "They're called Phobos and Deimos, which mean fear and dread. They're small and shaped like potatoes.",
             wiki("Moons of Mars"), difficulty=2)
space.choice("Which planet was found by maths before anyone saw it through a telescope, in 1846?", "Neptune", ["Uranus", "Pluto", "Saturn"],
             "Uranus wasn't moving quite as expected. Astronomers worked out that another planet must be pulling on it.",
             wiki("Discovery of Neptune"), difficulty=3)
space.choice("What causes the Northern Lights?", "Particles from the Sun hitting our atmosphere", ["Sunlight bouncing off polar ice", "Lightning high in the sky", "Light from distant galaxies"],
             "The particles are steered towards the poles by the Earth's magnetic field and make the air glow.",
             wiki("Aurora"), difficulty=2)
space.choice("In 2019, astronomers released the first ever picture of what?", "A black hole", ["A planet outside our Solar System", "The Big Bang", "The far side of the Moon"],
             "It showed a dark centre ringed by glowing gas, in a galaxy 55 million light years away.",
             wiki("Messier 87"), era="modern", difficulty=2)
space.choice("Which is the biggest moon in the Solar System?", "Ganymede, a moon of Jupiter", ["Our Moon", "Titan, a moon of Saturn", "Europa, a moon of Jupiter"],
             "Ganymede is even bigger than the planet Mercury.",
             wiki("Ganymede (moon)"), difficulty=2)
space.yes_no("Does the Moon always show the same face to the Earth?", True,
             "It spins exactly once each time it goes round us. Nobody saw the far side until a Soviet probe photographed it in 1959.",
             wiki("Far side of the Moon"), difficulty=2)
space.choice("Which planet has winds faster than any other, at over 2,000 km/h?", "Neptune", ["Jupiter", "Earth", "Mercury"],
             "That's faster than the speed of sound on Earth.",
             wiki("Neptune"), difficulty=3)
space.choice("Which mission flew four astronauts round the Moon and back in April 2026, the first crew to go there since 1972?", "Artemis II", ["Apollo 18", "Orion I", "Gateway 1"],
             "Christina Koch became the first woman to travel to the Moon, and the crew went further from Earth than any people before them.",
             ("collectSPACE: Artemis II crew is back on Earth after flyby of the moon", "https://www.collectspace.com/news/news-041026a-artemis-ii-splashdown-landing-recovery.html"), era="modern", difficulty=2)

# Nature --------------------------------------------------------------------------------------------
nature.choice("What colour are the river dolphins of the Amazon?", "Pink", ["Blue", "Yellow", "Black"],
              "They often get pinker as they get older.",
              wiki("Amazon river dolphin"), difficulty=1)
nature.choice("Which is the largest rodent in the world?", "The capybara", ["The beaver", "The porcupine", "The giant rat"],
              "It lives near rivers and swamps in South America and can weigh more than 60 kg.",
              wiki("Capybara"), difficulty=2)
nature.choice("Which is the heaviest snake in the world?", "The green anaconda", ["The reticulated python", "The king cobra", "The black mamba"],
              "It lives in the swamps and rivers of South America. Big females can weigh as much as an adult person.",
              wiki("Green anaconda"), difficulty=2)
nature.yes_no("Is the electric eel actually an eel?", False,
              "It's a kind of knifefish. It can give a shock of up to about 860 volts.",
              wiki("Electric eel"), difficulty=3)
nature.choice("In emperor penguins, which parent keeps the egg warm through the Antarctic winter?", "The father", ["The mother", "Both, taking turns each day", "Neither, it's buried in snow"],
              "He balances it on his feet for about two months, without eating, while the mother feeds at sea.",
              wiki("Emperor penguin"), difficulty=2)
nature.choice("What is a narwhal's long 'horn' really?", "A tooth", ["A bone", "A fin", "Its nose"],
              "It's a tusk that grows through the narwhal's lip and can reach about 3 metres.",
              wiki("Narwhal"), difficulty=2)
nature.choice("Which bird makes the longest migration of any animal?", "The Arctic tern", ["The swallow", "The albatross", "The Canada goose"],
              "It flies from the Arctic to the Antarctic and back every year, seeing two summers.",
              wiki("Arctic tern"), difficulty=2)
nature.choice("What colour does the Arctic fox's coat turn in winter?", "White", ["Black", "Red", "Grey-blue stripes"],
              "In summer it's brown or grey, to match the rocks and plants.",
              wiki("Arctic fox"), difficulty=1)
nature.choice("Which tiny creatures, shaped like shrimps, are the main food of many whales in Antarctica?", "Krill", ["Plankton worms", "Sea snails", "Sardines"],
              "A blue whale can eat around 4 tonnes of krill in a day.",
              wiki("Antarctic krill"), difficulty=2)
nature.choice("Which animal is the slowest mammal on Earth?", "The sloth", ["The koala", "The tortoise", "The panda"],
              "Sloths move so slowly that green algae grow in their fur. The tortoise is slow too, but it's a reptile.",
              wiki("Sloth"), difficulty=1)
nature.yes_no("Do poison dart frogs make their own poison?", False,
              "They get it from the ants and other insects they eat in the wild. Frogs raised in zoos are harmless.",
              wiki("Poison dart frog"), difficulty=3)
nature.choice("How long can a walrus's tusks grow?", "About 1 metre", ["About 10 cm", "About 3 metres", "About 5 metres"],
              "Walruses use their tusks to haul themselves out of the water onto the ice.",
              wiki("Walrus"), difficulty=3)
