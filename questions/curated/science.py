"""Science, Space, and Nature & Animals (the hand-written part)."""

from . import Category, wiki

sci = Category("science")

sci.choice("What is H₂O better known as?", "Water", ["Salt", "Hydrogen peroxide", "Oxygen"],
           "Each water molecule is two hydrogen atoms joined to one oxygen atom.",
           wiki("Properties of water"), difficulty=1)
sci.choice("Which gas do plants take in from the air to make their food?", "Carbon dioxide", ["Oxygen", "Nitrogen", "Helium"],
           "In photosynthesis, plants use sunlight to turn carbon dioxide and water into sugar, and give off oxygen.",
           wiki("Photosynthesis"), difficulty=1)
sci.choice("Which gas makes up most of the air we breathe?", "Nitrogen", ["Oxygen", "Carbon dioxide", "Hydrogen"],
           "Air is about 78% nitrogen and 21% oxygen.",
           wiki("Atmosphere of Earth"), difficulty=2)
sci.choice("At what temperature does pure water boil at sea level?", "100 °C", ["90 °C", "212 °C", "120 °C"],
           "Water boils at 100 °C, or 212 °F. High up a mountain the air pressure is lower, so it boils at a lower temperature.",
           wiki("Boiling point"), difficulty=1)
sci.choice("What is the hardest natural material?", "Diamond", ["Gold", "Granite", "Steel"],
           "Diamond is pure carbon, the same element as the graphite in a pencil, just arranged differently.",
           wiki("Diamond"), difficulty=1)
sci.choice("How many bones does an adult human body have?", "206", ["106", "300", "256"],
           "Babies are born with nearer 300, but some join together as they grow.",
           wiki("Human skeleton"), difficulty=2)
sci.choice("What is the largest organ of the human body?", "The skin", ["The liver", "The brain", "The lungs"],
           "An adult's skin weighs about 4 kg and covers about 2 m².",
           wiki("Human skin"), difficulty=2)
sci.choice("Which part of the body pumps blood around it?", "The heart", ["The lungs", "The liver", "The kidneys"],
           "An adult heart beats around 100,000 times a day.",
           wiki("Heart"), difficulty=1)
sci.choice("Where in the body is the smallest bone?", "The ear", ["The finger", "The nose", "The toe"],
           "The stapes, or stirrup, in the middle ear is about 3 mm long.",
           wiki("Stapes"), difficulty=2)
sci.higher_lower("Sound travels at about 343 metres per second in air. Does light travel faster or slower?", True,
                 "Light travels at nearly 300,000 km per second, almost a million times faster than sound. That's why you see lightning before you hear thunder.",
                 wiki("Speed of light"), labels=("Faster", "Slower"), difficulty=1)
sci.choice("How long does sunlight take to reach the Earth?", "About 8 minutes", ["About 8 seconds", "About 8 hours", "About 8 days"],
           "The Sun is about 150 million km away, so its light takes about 8 minutes and 20 seconds to reach us.",
           wiki("Sunlight"), difficulty=2)
sci.choice("Which scientist's name is used for the unit of force?", "Isaac Newton", ["Albert Einstein", "James Watt", "Alessandro Volta"],
           "One newton is about the force of a small apple pressing down in your hand.",
           wiki("Newton (unit)"), difficulty=3)
sci.choice("What do bees collect from flowers to make honey?", "Nectar", ["Pollen", "Sap", "Dew"],
           "Bees turn sugary nectar into honey. They also carry pollen, which helps plants make seeds.",
           wiki("Honey"), difficulty=1)
sci.choice("What colour do you get by mixing blue and yellow paint?", "Green", ["Purple", "Orange", "Brown"],
           "Blue and yellow paint make green. Mixing coloured light works differently: red and green light make yellow.",
           wiki("Color mixing"), difficulty=1)
sci.choice("How many colours are traditionally named in a rainbow?", "Seven", ["Five", "Six", "Nine"],
           "Red, orange, yellow, green, blue, indigo and violet. Isaac Newton chose seven names.",
           wiki("Rainbow"), difficulty=1)
sci.true_false("A magnet's north pole pulls towards another magnet's north pole.", False,
               "Like poles push apart. A north pole pulls towards a south pole.",
               wiki("Magnet"), difficulty=1)
sci.choice("What does DNA carry?", "The instructions for building living things", ["Oxygen around the body", "Electricity in the brain", "Food to cells"],
           "DNA is a long molecule, shaped like a twisted ladder, found in nearly every cell.",
           wiki("DNA"), difficulty=2)
sci.choice("Which famous shape is the DNA molecule?", "A double helix", ["A pyramid", "A cube", "A ring"],
           "James Watson and Francis Crick described the double helix in 1953, using X-ray images made by Rosalind Franklin.",
           wiki("DNA"), era="classic", difficulty=2)
sci.choice("Who discovered penicillin, the first antibiotic, in 1928?", "Alexander Fleming", ["Louis Pasteur", "Edward Jenner", "Joseph Lister"],
           "Fleming noticed that mould on a dish had killed the bacteria around it.",
           wiki("Penicillin"), difficulty=2)
sci.choice("Who made the first vaccine, against smallpox, in 1796?", "Edward Jenner", ["Louis Pasteur", "Alexander Fleming", "Jonas Salk"],
           "Jenner used cowpox to protect people against smallpox. The word vaccine comes from vacca, Latin for cow.",
           wiki("Edward Jenner"), difficulty=3)
sci.yes_no("Is a tomato a fruit, scientifically speaking?", True,
           "A fruit is the part of a plant that holds the seeds, so tomatoes, cucumbers and peppers are all fruits.",
           wiki("Tomato"), difficulty=1)
sci.choice("What is the freezing point of water in Fahrenheit?", "32 °F", ["0 °F", "100 °F", "-32 °F"],
           "Water freezes at 0 °C, which is 32 °F.",
           wiki("Fahrenheit"), difficulty=2)
sci.higher_lower("Normal human body temperature is about 37 °C. Is the boiling point of water higher or lower than three times that?", False,
                 "Three times 37 is 111 °C, and water boils at 100 °C.",
                 wiki("Human body temperature"), difficulty=2)
sci.choice("What force keeps us on the ground?", "Gravity", ["Magnetism", "Friction", "Electricity"],
           "Gravity pulls everything with mass towards everything else. The Earth is so big that its pull holds us down.",
           wiki("Gravity"), difficulty=1)
sci.choice("Which metal is used in most electrical wires?", "Copper", ["Iron", "Gold", "Lead"],
           "Copper carries electricity very well and is much cheaper than silver, which is even better.",
           wiki("Copper"), difficulty=2)
sci.choice("What is the name for the scientist who studies rocks?", "A geologist", ["A biologist", "An astronomer", "A meteorologist"],
           "Geologists study rocks, earthquakes and volcanoes. Meteorologists study the weather.",
           wiki("Geologist"), difficulty=2)

space = Category("space")

space.choice("Which is the largest planet in our Solar System?", "Jupiter", ["Saturn", "Neptune", "Earth"],
             "Jupiter is so big that more than 1,300 Earths could fit inside it.",
             wiki("Jupiter"), difficulty=1)
space.choice("Which planet is closest to the Sun?", "Mercury", ["Venus", "Mars", "Earth"],
             "Mercury takes just 88 days to go round the Sun.",
             wiki("Mercury (planet)"), difficulty=1)
space.choice("Which planet is known as the Red Planet?", "Mars", ["Jupiter", "Venus", "Mercury"],
             "Mars looks red because its soil is full of iron oxide: rust.",
             wiki("Mars"), difficulty=1)
space.choice("How many planets are there in our Solar System?", "Eight", ["Nine", "Seven", "Ten"],
             "There were nine until 2006, when astronomers reclassified Pluto as a dwarf planet.",
             wiki("Solar System"), difficulty=1)
space.choice("In which year was Pluto reclassified as a dwarf planet?", "2006", ["1999", "2012", "1990"],
             "The International Astronomical Union agreed a new definition of a planet in August 2006.",
             wiki("Pluto"), era="modern", difficulty=3)
space.choice("Which planet is famous for its big, bright rings?", "Saturn", ["Jupiter", "Uranus", "Neptune"],
             "All four giant planets have rings, but Saturn's are by far the brightest and biggest.",
             wiki("Rings of Saturn"), difficulty=1)
space.choice("Who was the first person to travel into space?", "Yuri Gagarin", ["Neil Armstrong", "Buzz Aldrin", "Valentina Tereshkova"],
             "The Soviet cosmonaut orbited the Earth once on 12 April 1961, in a flight lasting 108 minutes.",
             wiki("Yuri Gagarin"), era="classic", difficulty=2)
space.choice("Who was the first woman in space?", "Valentina Tereshkova", ["Sally Ride", "Helen Sharman", "Mae Jemison"],
             "Valentina Tereshkova flew on Vostok 6 in June 1963 and orbited the Earth 48 times.",
             wiki("Valentina Tereshkova"), era="classic", difficulty=3)
space.choice("Who was the first British astronaut?", "Helen Sharman", ["Tim Peake", "Michael Foale", "Richard Branson"],
             "Helen Sharman went to the Mir space station in 1991, when she was 27.",
             wiki("Helen Sharman"), era="classic", difficulty=3)
space.choice("What was the name of the first artificial satellite, launched in 1957?", "Sputnik 1", ["Apollo 1", "Explorer 1", "Hubble"],
             "Sputnik 1 was launched by the Soviet Union on 4 October 1957. It was about the size of a beach ball.",
             wiki("Sputnik 1"), era="classic", difficulty=2)
space.choice("What was the name of the spacecraft that first landed people on the Moon?", "Apollo 11", ["Apollo 13", "Gemini 4", "Voyager 1"],
             "Apollo 11's lunar module was called Eagle. Its famous message: 'The Eagle has landed.'",
             wiki("Apollo 11"), era="classic", difficulty=1)
space.choice("How many people have walked on the Moon?", "12", ["2", "6", "24"],
             "Twelve astronauts walked on the Moon between 1969 and 1972, on six Apollo missions.",
             wiki("List of Apollo astronauts"), era="classic", difficulty=2, as_of="2026-11")
space.choice("Which space telescope, launched in 2021, is the biggest ever sent into space?", "James Webb", ["Hubble", "Kepler", "Spitzer"],
             "The James Webb Space Telescope's gold-covered mirror is 6.5 metres across.",
             wiki("James Webb Space Telescope"), era="modern", difficulty=2)
space.choice("What is the name of our galaxy?", "The Milky Way", ["Andromeda", "The Whirlpool", "Orion"],
             "The Milky Way holds somewhere between 100 and 400 billion stars.",
             wiki("Milky Way"), difficulty=1)
space.choice("What is the Sun?", "A star", ["A planet", "A comet", "A moon"],
             "The Sun is a fairly ordinary star. It holds 99.8% of all the mass in the Solar System.",
             wiki("Sun"), difficulty=1)
space.higher_lower("The Moon is about 384,000 km from the Earth. Is the Sun more or less than 100 times further away?", True,
                   "The Sun is about 150 million km away, roughly 390 times further than the Moon.",
                   wiki("Sun"), labels=("More", "Less"), difficulty=3)
space.choice("Which planet spins on its side, almost lying down?", "Uranus", ["Neptune", "Saturn", "Venus"],
             "Uranus is tilted by about 98 degrees, probably after a huge crash long ago.",
             wiki("Uranus"), difficulty=3)
space.choice("Which is the closest star to the Sun?", "Proxima Centauri", ["Sirius", "Polaris", "Betelgeuse"],
             "Proxima Centauri is about 4.2 light years away. Its light takes over four years to reach us.",
             wiki("Proxima Centauri"), difficulty=3)
space.choice("What is the brightest star in the night sky?", "Sirius", ["Polaris", "Betelgeuse", "Vega"],
             "Sirius is also called the Dog Star. It's about 8.6 light years away.",
             wiki("Sirius"), difficulty=3)
space.true_false("The North Star, Polaris, is the brightest star in the night sky.", False,
                 "Polaris isn't even in the top 40. It's famous because it stays almost still above the North Pole.",
                 wiki("Polaris"), difficulty=2)
space.choice("What is a light year?", "A distance", ["A length of time", "A speed", "A brightness"],
             "A light year is how far light travels in a year: about 9.46 trillion km.",
             wiki("Light-year"), difficulty=2)
space.choice("Which planet has the Great Red Spot, a storm bigger than the Earth?", "Jupiter", ["Mars", "Saturn", "Neptune"],
             "The Great Red Spot has been swirling for at least 150 years and possibly much longer.",
             wiki("Great Red Spot"), difficulty=2)
space.choice("What is the name of the space station where astronauts have lived since 2000?", "The International Space Station", ["Mir", "Skylab", "Tiangong-1"],
             "The ISS has had people on board continuously since November 2000. It goes round the Earth about every 90 minutes.",
             wiki("International Space Station"), era="modern", difficulty=1)
space.choice("Which British astronaut walked in space from the International Space Station in 2016?", "Tim Peake", ["Helen Sharman", "Chris Hadfield", "Michael Foale"],
             "Tim Peake spent six months on the ISS. He also ran the London Marathon on a treadmill in space.",
             wiki("Tim Peake"), era="modern", difficulty=2)
space.yes_no("Is there a footprint on the Moon that could still be there in a million years?", True,
             "There's no wind or rain on the Moon to wash footprints away, so the Apollo footprints could last for millions of years.",
             wiki("Moon"), difficulty=2)
space.choice("Which was the first spacecraft to leave the Solar System's bubble of solar wind, in 2012?", "Voyager 1", ["Apollo 11", "Hubble", "Pioneer 10"],
             "Voyager 1 was launched in 1977 and is the most distant human-made object.",
             wiki("Voyager 1"), difficulty=3)
space.choice("What causes the seasons on Earth?", "The tilt of the Earth", ["How close the Earth is to the Sun", "The Moon", "The Sun getting hotter and cooler"],
             "The Earth is tilted by about 23.4 degrees. Summer is when your half of the planet leans towards the Sun.",
             wiki("Season"), difficulty=2)
space.choice("Roughly how long does the Moon take to go round the Earth?", "About a month", ["About a day", "About a week", "About a year"],
             "The Moon takes about 27.3 days to orbit the Earth. The word month comes from Moon.",
             wiki("Orbit of the Moon"), difficulty=1)
space.choice("What do we call a rock from space that lands on Earth?", "A meteorite", ["A comet", "An asteroid", "A satellite"],
             "While it streaks through the sky it's a meteor, or shooting star. If it reaches the ground it's a meteorite.",
             wiki("Meteorite"), difficulty=2)

nature = Category("nature")

nature.choice("What is the largest animal ever known to have lived?", "The blue whale", ["The African elephant", "Argentinosaurus", "The megalodon"],
              "Blue whales can be about 30 metres long and weigh more than any dinosaur known.",
              wiki("Blue whale"), difficulty=1)
nature.choice("What is the fastest land animal?", "The cheetah", ["The lion", "The greyhound", "The pronghorn"],
              "A cheetah can reach about 100 km/h in short bursts.",
              wiki("Cheetah"), difficulty=1)
nature.choice("What is the fastest bird in a dive?", "The peregrine falcon", ["The golden eagle", "The swift", "The ostrich"],
              "A diving peregrine falcon can reach more than 300 km/h, faster than any other animal.",
              wiki("Peregrine falcon"), difficulty=2)
nature.choice("What is the tallest animal?", "The giraffe", ["The elephant", "The ostrich", "The moose"],
              "A male giraffe can be about 5.5 metres tall. Its neck has seven bones, the same as ours.",
              wiki("Giraffe"), difficulty=1)
nature.yes_no("Does a giraffe have the same number of neck bones as a human?", True,
              "Almost all mammals have seven neck bones. A giraffe's are just much longer: each one can be over 25 cm.",
              wiki("Giraffe"), difficulty=2)
nature.choice("How many hearts does an octopus have?", "Three", ["One", "Two", "Eight"],
              "Two hearts pump blood to the gills, and one pumps it round the rest of the body. Its blood is blue.",
              wiki("Octopus"), difficulty=2)
nature.choice("How many legs does a spider have?", "Eight", ["Six", "Ten", "Twelve"],
              "Spiders have eight legs. Insects, like ants and beetles, have six.",
              wiki("Spider"), difficulty=1)
nature.true_false("A spider is an insect.", False,
                  "Spiders are arachnids, like scorpions. Insects have six legs and three body parts. Spiders have eight legs and two.",
                  wiki("Spider"), difficulty=2)
nature.choice("Which is the largest living bird?", "The ostrich", ["The emu", "The albatross", "The condor"],
              "An ostrich can stand about 2.7 metres tall. It can't fly, but it can run at about 70 km/h.",
              wiki("Common ostrich"), difficulty=1)
nature.choice("What is a baby kangaroo called?", "A joey", ["A kit", "A cub", "A calf"],
              "A newborn joey is about the size of a jellybean and grows in its mother's pouch.",
              wiki("Kangaroo"), difficulty=1)
nature.choice("What is a group of lions called?", "A pride", ["A pack", "A herd", "A school"],
              "Lions are the only big cats that live in groups.",
              wiki("Lion"), difficulty=1)
nature.choice("What is a group of crows called?", "A murder", ["A pod", "A gaggle", "A parliament"],
              "A group of crows is called a murder. A group of owls is a parliament.",
              wiki("List of English terms of venery, by animal"), era="classic", difficulty=3)
nature.choice("Which animal's diet is almost all bamboo?", "The giant panda", ["The koala", "The red squirrel", "The sloth"],
              "A giant panda can spend up to 14 hours a day eating bamboo.",
              wiki("Giant panda"), difficulty=1)
nature.choice("What do koalas eat?", "Eucalyptus leaves", ["Bamboo", "Insects", "Grass"],
              "Eucalyptus leaves are tough and low in energy, which is why koalas sleep up to about 20 hours a day.",
              wiki("Koala"), difficulty=1)
nature.yes_no("Is a whale a fish?", False,
              "Whales are mammals. They breathe air, have warm blood and feed their babies on milk.",
              wiki("Whale"), difficulty=1)
nature.yes_no("Is a bat a bird?", False,
              "Bats are mammals: the only mammals that can truly fly.",
              wiki("Bat"), difficulty=1)
nature.choice("Which bird can fly backwards?", "The hummingbird", ["The swallow", "The robin", "The parrot"],
              "Hummingbirds beat their wings so fast, up to about 80 times a second, that they can hover and fly backwards.",
              wiki("Hummingbird"), difficulty=2)
nature.choice("Which animal has black and white stripes and lives in Africa?", "The zebra", ["The okapi", "The tapir", "The skunk"],
              "No two zebras have exactly the same stripes.",
              wiki("Zebra"), difficulty=1)
nature.choice("Where do penguins live in the wild?", "The Southern Hemisphere", ["The Arctic", "Only in Antarctica", "Northern Europe"],
              "All wild penguins live south of the Equator, apart from the Galápagos penguin, which just crosses it. None live in the Arctic.",
              wiki("Penguin"), difficulty=2)
nature.true_false("Polar bears and penguins live together in the wild.", False,
                  "Polar bears live in the Arctic, at the top of the world, and penguins in the south. They never meet in the wild.",
                  wiki("Polar bear"), difficulty=1)
nature.choice("Under its white fur, what colour is a polar bear's skin?", "Black", ["White", "Pink", "Grey"],
              "Black skin soaks up the Sun's heat. Its fur is actually see-through, not white.",
              wiki("Polar bear"), difficulty=2)
nature.choice("Which is the largest land animal?", "The African bush elephant", ["The hippopotamus", "The white rhino", "The giraffe"],
              "A large male can weigh about 6 tonnes.",
              wiki("African bush elephant"), difficulty=1)
nature.higher_lower("An elephant is pregnant for about 22 months. Is a human pregnancy longer or shorter?", False,
                    "A human pregnancy lasts about 9 months. The elephant's is the longest of any land mammal.",
                    wiki("Elephant"), labels=("Longer", "Shorter"), difficulty=2)
nature.choice("What does a caterpillar turn into?", "A butterfly or moth", ["A beetle", "A dragonfly", "A bee"],
              "Inside its chrysalis or cocoon, the caterpillar's body completely rebuilds itself.",
              wiki("Caterpillar"), difficulty=1)
nature.choice("What is a baby frog called?", "A tadpole", ["A cygnet", "A pup", "A nymph"],
              "Tadpoles live in water and breathe through gills before they grow legs.",
              wiki("Tadpole"), difficulty=1)
nature.choice("Which animal is known for changing colour?", "The chameleon", ["The iguana", "The gecko", "The tortoise"],
              "Chameleons change colour mostly to signal to each other and control their temperature, not just to hide.",
              wiki("Chameleon"), difficulty=1)
nature.choice("What is the world's largest fish?", "The whale shark", ["The great white shark", "The blue whale", "The sunfish"],
              "Whale sharks can grow to about 18 metres, but they eat tiny plankton.",
              wiki("Whale shark"), difficulty=2)
nature.choice("Which is the tallest type of tree?", "The coast redwood", ["The oak", "The baobab", "The giant sequoia"],
              "The tallest known tree, a coast redwood in California nicknamed Hyperion, is about 116 metres tall.",
              wiki("Hyperion (tree)"), difficulty=3)
nature.choice("Which animal has the longest lifespan of any vertebrate known?", "The Greenland shark", ["The giant tortoise", "The elephant", "The bowhead whale"],
              "Scientists estimate Greenland sharks can live for at least 270 years, and possibly more than 400.",
              wiki("Greenland shark"), difficulty=3)
nature.choice("What do you call an animal that eats only plants?", "A herbivore", ["A carnivore", "An omnivore", "A predator"],
              "Cows, rabbits and elephants are herbivores. Humans are omnivores, eating plants and meat.",
              wiki("Herbivore"), difficulty=1)
nature.choice("How many legs does an insect have?", "Six", ["Four", "Eight", "Ten"],
              "Every adult insect has six legs, joined to the middle part of its body.",
              wiki("Insect"), difficulty=1)
nature.choice("What is the national animal of Scotland?", "The unicorn", ["The red deer", "The golden eagle", "The Highland cow"],
              "The unicorn has been a symbol of Scotland for centuries, and it appears on the royal coat of arms.",
              wiki("National symbols of Scotland"), difficulty=2)
nature.choice("Which mammal lays eggs?", "The platypus", ["The beaver", "The otter", "The kangaroo"],
              "The platypus and the echidnas are the only mammals that lay eggs.",
              wiki("Platypus"), difficulty=2)
nature.choice("What do you call a scientist who studies animals?", "A zoologist", ["A botanist", "A geologist", "A chemist"],
              "Botanists study plants. Zoologists study animals.",
              wiki("Zoology"), difficulty=2)
nature.choice("Which British bird has a red breast and is a symbol of Christmas?", "The robin", ["The blue tit", "The wren", "The sparrow"],
              "Robins appeared on Victorian Christmas cards because postmen wore red jackets and were nicknamed robins.",
              wiki("European robin"), difficulty=1)
nature.yes_no("Do all owls hunt only at night?", False,
              "Many owls hunt at night, but some, like the snowy owl and the short-eared owl, also hunt in daylight.",
              wiki("Owl"), difficulty=2)
nature.choice("Where would you find a coral reef?", "In warm, shallow seas", ["In deep freezing seas", "In rivers", "In lakes"],
              "Most reef-building corals need clear, warm water. The Great Barrier Reef is the largest, off Australia.",
              wiki("Coral reef"), difficulty=1)
nature.choice("What is the largest coral reef system in the world?", "The Great Barrier Reef", ["The Belize Barrier Reef", "The Red Sea Reef", "The Florida Reef"],
              "It stretches about 2,300 km along the coast of Queensland and can be seen from space.",
              wiki("Great Barrier Reef"), difficulty=1)
nature.choice("Which is the world's largest rainforest?", "The Amazon", ["The Congo", "The Daintree", "Borneo"],
              "The Amazon covers about 5.5 million km², mostly in Brazil.",
              wiki("Amazon rainforest"), difficulty=1)
nature.choice("What does a camel store in its hump?", "Fat", ["Water", "Milk", "Air"],
              "The hump stores fat, which the camel can use for energy when food is scarce.",
              wiki("Camel"), difficulty=2)
nature.choice("How many eyes does a bee have?", "Five", ["Two", "Four", "Eight"],
              "Bees have two large compound eyes and three small simple eyes on top of the head.",
              wiki("Bee"), difficulty=3)
nature.choice("Which sea creature has no brain, no heart and no blood?", "The jellyfish", ["The starfish", "The crab", "The squid"],
              "Jellyfish are about 95% water. They have a simple net of nerves instead of a brain.",
              wiki("Jellyfish"), difficulty=2)
nature.choice("Which animal is the symbol of the WWF, the wildlife charity?", "The giant panda", ["The tiger", "The elephant", "The polar bear"],
              "The panda logo was drawn in 1961, inspired by a panda named Chi Chi at London Zoo.",
              wiki("World Wide Fund for Nature"), era="classic", difficulty=1)
nature.choice("What is the only continent with no wild snakes?", "Antarctica", ["Australia", "Europe", "South America"],
              "It's far too cold for snakes there. Ireland and New Zealand have no native land snakes either.",
              wiki("Snake"), difficulty=2)

nature.choice("What is a male red deer called?", "A stag", ["A ram", "A boar", "A cob"],
              "Stags grow new antlers every year and shed them in late winter or spring.",
              wiki("Red deer"), difficulty=1)

assert (len(sci.questions), len(space.questions), len(nature.questions)) == (26, 29, 45), (len(sci.questions), len(space.questions), len(nature.questions))
