"""More science: chemistry, physics, the human body and health."""

from . import Category, wiki

c = Category("science", prefix="science3")
NHS_FIVE_A_DAY = ("NHS: 5 A Day", "https://www.nhs.uk/live-well/eat-well/5-a-day/why-5-a-day/")
NHS_HANDS = ("NHS: how to wash your hands", "https://www.nhs.uk/live-well/best-way-to-wash-your-hands/")
NHS_SLEEP = ("NHS Every Mind Matters: sleep", "https://www.nhs.uk/oneyou/every-mind-matters/sleep/")

# Chemistry -----------------------------------------------------------------------------------------
c.choice("What is the chemical name for ordinary table salt?", "Sodium chloride", ["Calcium carbonate", "Potassium nitrate", "Sodium bicarbonate"],
         "Its formula is NaCl. On their own, sodium is a metal that fizzes in water and chlorine is a poisonous gas.",
         wiki("Sodium chloride"), difficulty=2)
c.choice("Which is the only metal that is liquid at room temperature?", "Mercury", ["Lead", "Tin", "Aluminium"],
         "Mercury was once used in most thermometers. Bromine is also liquid at room temperature, but it isn't a metal.",
         wiki("Mercury (element)"), difficulty=2)
c.choice("Which is the lightest element?", "Hydrogen", ["Helium", "Oxygen", "Carbon"],
         "Hydrogen is element number 1. Its atoms have just one proton and one electron.",
         wiki("Hydrogen"), difficulty=1)
c.choice("What is rust?", "Iron that has reacted with oxygen and water", ["A kind of mould", "Dried mud", "Copper that has gone green"],
         "Its chemical name is iron oxide. Painting or oiling iron keeps the air and water off.",
         wiki("Rust"), difficulty=1)
c.choice("Diamonds and the graphite in pencils are both made of which element?", "Carbon", ["Silicon", "Lead", "Calcium"],
         "The atoms are just arranged differently. In diamond they're locked in a rigid frame, in graphite they lie in slippery layers.",
         wiki("Allotropes of carbon"), difficulty=2)
c.choice("What is 'dry ice'?", "Frozen carbon dioxide", ["Frozen water with salt in", "Frozen nitrogen", "Ice kept in a vacuum"],
         "It's about −78 °C and turns straight from a solid into a gas, which is why it's used for stage smoke.",
         wiki("Dry ice"), difficulty=2)
c.choice("How many elements are there in the periodic table?", "118", ["92", "103", "150"],
         "The last four were named in 2016. About 90 of them are found in nature; the rest have only been made in laboratories.",
         wiki("Periodic table"), difficulty=2, as_of="2026-11")
c.choice("Which element is named after Marie and Pierre Curie?", "Curium", ["Polonium", "Radium", "Einsteinium"],
         "Marie Curie herself named polonium, after Poland, the country she came from.",
         wiki("Curium"), difficulty=2)
c.choice("Why does breathing in helium make your voice sound squeaky?", "Sound travels faster through helium", ["Helium tightens your vocal cords", "Helium is colder than air", "Helium makes your throat smaller"],
         "Your vocal cords vibrate at the same speed, but the faster sound changes which parts of your voice are loudest.",
         wiki("Helium"), difficulty=3)
c.yes_no("Does water get bigger when it freezes?", True,
         "It expands by about 9%, which is why ice floats and why pipes can burst in winter.",
         wiki("Properties of water"), difficulty=1)
c.choice("What is the chemical formula for ozone, the gas that shields us from the sun's ultraviolet rays?", "O₃", ["O₂", "CO₂", "H₂O₂"],
         "Normal oxygen is O₂, two atoms joined together. Ozone has three.",
         wiki("Ozone"), difficulty=3)
c.choice("Lemon juice has a pH of about 2. What does that make it?", "An acid", ["An alkali", "Neutral", "A salt"],
         "Anything below 7 is acidic. Soap and bleach are alkaline, above 7.",
         wiki("PH"), difficulty=2)
c.choice("What is the everyday name for sodium bicarbonate?", "Baking soda", ["Washing soda", "Table salt", "Chalk"],
         "When it meets an acid it fizzes out carbon dioxide, which makes cakes rise.",
         wiki("Sodium bicarbonate"), difficulty=2)
c.choice("Which gas is known as 'laughing gas'?", "Nitrous oxide", ["Helium", "Carbon monoxide", "Neon"],
         "Dentists and midwives use it as a painkiller. It was discovered in 1772.",
         wiki("Nitrous oxide"), difficulty=2)
c.yes_no("Does gold rust or go dull over time?", False,
         "Gold hardly reacts with anything, which is why ancient gold treasure still shines when it's dug up.",
         wiki("Gold"), difficulty=2)
c.choice("Which element is there most of in the Earth's crust?", "Oxygen", ["Iron", "Silicon", "Carbon"],
         "Almost half of the crust, by weight, is oxygen, locked up in rocks and minerals.",
         wiki("Abundance of elements in Earth's crust"), difficulty=3)
c.choice("Neon, argon and helium are 'noble gases'. Why are they called that?", "They hardly react with anything", ["They were discovered by nobles", "They glow gold", "They're very expensive"],
         "Like nobles who kept to themselves, they don't mix with other elements.",
         wiki("Noble gas"), difficulty=3)
c.choice("Who first named oxygen and hydrogen, and is often called the father of modern chemistry?", "Antoine Lavoisier", ["Robert Boyle", "John Dalton", "Dmitri Mendeleev"],
         "He also showed that matter isn't lost when things burn, it just changes form.",
         wiki("Antoine Lavoisier"), era="classic", difficulty=3)

# Physics -------------------------------------------------------------------------------------------
c.yes_no("Can sound travel through space?", False,
         "Sound needs air, water or something solid to travel through. Space is almost empty, so it's silent.",
         wiki("Sound"), difficulty=1)
c.choice("What is the coldest temperature possible, called absolute zero?", "About −273 °C", ["−100 °C", "−180 °C", "−500 °C"],
         "At −273.15 °C atoms almost stop moving. Nothing can ever be cooled below it.",
         wiki("Absolute zero"), difficulty=2)
c.choice("Which colour is on the outside of a rainbow's arc?", "Red", ["Violet", "Blue", "Yellow"],
         "The order is red, orange, yellow, green, blue, indigo, violet. In a double rainbow, the second bow is the other way round.",
         wiki("Rainbow"), difficulty=2)
c.choice("Which scientist first split white light into a rainbow of colours with a prism?", "Isaac Newton", ["Galileo Galilei", "Albert Einstein", "Michael Faraday"],
         "Newton did it in the 1660s and showed that white light is a mix of all the colours.",
         wiki("Opticks"), difficulty=2)
c.choice("What is measured in volts?", "The push of an electric current", ["How bright a light is", "How heavy something is", "How loud a sound is"],
         "The volt is named after Alessandro Volta, who made the first battery in 1800.",
         wiki("Volt"), difficulty=2)
c.choice("In a vacuum, which falls faster, a feather or a hammer?", "They fall at the same speed", ["The hammer", "The feather", "Neither falls at all"],
         "An Apollo 15 astronaut tried it on the Moon in 1971, and they hit the ground together.",
         wiki("Apollo 15"), difficulty=2)

# The body ------------------------------------------------------------------------------------------
c.higher_lower("Does a person's heart beat more or less than 100,000 times a day?", True,
               "At about 70 beats a minute, it's roughly 100,000 times a day and more than 2.5 billion in a lifetime.",
               wiki("Heart rate"), labels=("More", "Less"), difficulty=3)
c.choice("Roughly how much blood is in an adult's body?", "About 5 litres", ["About 1 litre", "About 12 litres", "About 25 litres"],
         "Blood makes up about 7% of your body weight.",
         wiki("Blood volume"), difficulty=2)
c.higher_lower("Adults have 206 bones. Are babies born with more or fewer?", True,
               "Babies have about 300. Some of them join together as we grow up.",
               wiki("Human skeleton"), labels=("More", "Fewer"), difficulty=2)
c.choice("Which is the longest bone in the human body?", "The thigh bone (femur)", ["The shin bone (tibia)", "The spine", "The upper arm bone (humerus)"],
         "It's about a quarter of a person's height.",
         wiki("Femur"), difficulty=1)
c.choice("Roughly how much of the human body is water?", "About 60%", ["About 10%", "About 30%", "About 90%"],
         "Babies are even wetter, at about 75%.",
         wiki("Body water"), difficulty=2)
c.choice("What gives blood its red colour?", "Haemoglobin, which contains iron", ["Vitamin C", "Copper", "Red skin cells"],
         "Haemoglobin carries oxygen from the lungs round the body.",
         wiki("Hemoglobin"), difficulty=2)
c.choice("Sailors once got scurvy on long voyages. Which vitamin were they missing?", "Vitamin C", ["Vitamin A", "Vitamin D", "Vitamin B12"],
         "The Royal Navy gave sailors lemon and lime juice, which is how British sailors got the nickname 'limeys'.",
         wiki("Scurvy"), era="classic", difficulty=2)
c.choice("Roughly what share of the body's energy does the brain use?", "About 20%", ["About 2%", "About 50%", "About 75%"],
         "It's only about 2% of our body weight, but it's very hungry.",
         wiki("Human brain"), difficulty=3)
c.yes_no("Can the human liver grow back if part of it is removed?", True,
         "It can regrow to its full size from as little as a quarter of the original. That's why people can donate part of their liver.",
         wiki("Liver regeneration"), difficulty=2)
c.choice("Which of your lungs is a little smaller?", "The left one", ["The right one", "Neither, they're exactly the same", "It depends whether you're left-handed"],
         "The left lung leaves room for the heart. It has two lobes, while the right has three.",
         wiki("Lung"), difficulty=3)
c.choice("Roughly how much of our DNA do we share with chimpanzees?", "About 99%", ["About 50%", "About 75%", "About 90%"],
         "They are our closest living relatives, along with bonobos.",
         wiki("Chimpanzee"), difficulty=2)
c.choice("What is your 'funny bone' really?", "A nerve", ["A small bone", "A muscle", "A tendon"],
         "It's the ulnar nerve, which runs close to the skin at the elbow. Knocking it gives that tingling feeling.",
         wiki("Ulnar nerve"), difficulty=2)
c.choice("Which muscle makes you hiccup when it suddenly tightens?", "The diaphragm", ["The heart", "The tongue", "The stomach"],
         "The diaphragm sits under your lungs. When it jerks, your vocal cords snap shut, making the 'hic' sound.",
         wiki("Hiccup"), difficulty=2)
c.yes_no("Do fingernails grow faster than toenails?", True,
         "Fingernails grow about 3 mm a month, two to three times as fast as toenails.",
         wiki("Nail (anatomy)"), difficulty=2)
c.choice("Which part of the eye has no blood vessels and takes its oxygen straight from the air?", "The cornea, the clear window at the front", ["The iris, the coloured ring", "The retina, at the back", "The optic nerve"],
         "It has no blood vessels so that light can pass through it clearly.",
         wiki("Cornea"), difficulty=3)
c.choice("Which blood group can be given to almost anyone in an emergency?", "O negative", ["AB positive", "A positive", "B negative"],
         "It's called the universal donor. AB positive people are universal receivers.",
         wiki("Blood type"), difficulty=2)
c.choice("Which are the smallest blood vessels in the body?", "Capillaries", ["Arteries", "Veins", "Valves"],
         "Some are so narrow that red blood cells have to pass through them in single file.",
         wiki("Capillary"), difficulty=2)

# Health --------------------------------------------------------------------------------------------
c.choice("How many portions of fruit and vegetables a day does the NHS recommend?", "At least 5", ["At least 2", "At least 8", "At least 10"],
         "A portion is 80 g, about a handful. Fresh, frozen, tinned and dried all count.",
         NHS_FIVE_A_DAY, difficulty=1)
c.choice("For about how long does the NHS say you should wash your hands with soap?", "20 seconds", ["5 seconds", "1 minute", "2 minutes"],
         "That's about as long as singing 'Happy Birthday' twice.",
         NHS_HANDS, difficulty=1)
c.choice("How much sleep do most adults need each night?", "About 7 to 9 hours", ["About 4 to 5 hours", "About 10 to 12 hours", "About 13 to 14 hours"],
         "Children and teenagers need more.",
         NHS_SLEEP, difficulty=1)
c.choice("Which was the first human disease to be wiped out completely, in 1980?", "Smallpox", ["Polio", "Measles", "Malaria"],
         "It was beaten by a worldwide vaccination campaign, almost 200 years after Edward Jenner's first vaccine.",
         wiki("Smallpox"), difficulty=2)
c.choice("In which year was Britain's National Health Service, the NHS, set up?", "1948", ["1918", "1936", "1966"],
         "It opened on 5 July 1948, free to everyone when they needed it.",
         wiki("National Health Service (England)"), difficulty=2)
c.choice("In 1978, Louise Brown was born in Oldham. What was special about her?", "She was the world's first 'test-tube baby'", ["She was the first baby born on TV", "She was the first child given a heart transplant", "She was born on a plane"],
         "She was conceived by IVF, a method developed by Robert Edwards and Patrick Steptoe.",
         wiki("Louise Brown"), era="classic", difficulty=3)
c.choice("What was Dolly, born in Scotland in 1996, the first of?", "Mammals cloned from an adult cell", ["Animals born in space", "Sheep with two heads", "Pets to live to 30"],
         "Dolly the sheep was created near Edinburgh, and was named after the singer Dolly Parton.",
         wiki("Dolly (sheep)"), era="classic", difficulty=2)
c.yes_no("Do antibiotics work against viruses, such as colds and flu?", False,
         "Antibiotics only kill bacteria. Taking them when they aren't needed helps germs become resistant to them.",
         ("NHS: antibiotics", "https://www.nhs.uk/medicines/antibiotics/"), difficulty=2)
c.choice("What does the 'SPF' on sun cream measure?", "How well it blocks the rays that cause sunburn", ["How long it stays wet", "How much water it can take", "How many vitamins it has"],
         "SPF stands for 'sun protection factor'. It's about UVB rays. A star rating on UK bottles shows protection from UVA rays.",
         ("NHS: sunscreen and sun safety", "https://www.nhs.uk/live-well/seasonal-health/sunscreen-and-sun-safety/"), difficulty=3)
c.yes_no("Does cracking your knuckles cause arthritis?", False,
         "Studies have found no link. One doctor cracked the knuckles of only one hand for over 60 years and found no difference between his hands.",
         wiki("Cracking joints"), difficulty=2)
