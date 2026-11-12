"""More famous people: inventors, explorers, scientists and leaders who changed the world."""

from . import Category, wiki

c = Category("people", prefix="people3")

# Inventors -----------------------------------------------------------------------------------------
c.yes_no("Did Thomas Edison invent the very first electric light bulb?", False,
         "Others, such as Joseph Swan in England, had made glowing bulbs before him. Edison's 1879 bulb was the first practical one that lasted long enough to sell.",
         wiki("Incandescent light bulb"), difficulty=2)
c.choice("Which machine for recording and playing back sound did Thomas Edison invent in 1877?", "The phonograph", ["The radio", "The telephone", "The microphone"],
         "The first words he recorded were 'Mary had a little lamb'.",
         wiki("Phonograph"), difficulty=2)
c.choice("Thomas Edison was nicknamed 'the Wizard of' where?", "Menlo Park", ["Oz", "Silicon Valley", "Detroit"],
         "Menlo Park, in New Jersey, was where he built his famous laboratory.",
         wiki("Thomas Edison"), era="classic", difficulty=3)
c.higher_lower("Did Thomas Edison hold more or fewer than 1,000 US patents?", True,
               "He held 1,093 US patents, one of the most of any inventor.",
               wiki("Thomas Edison"), labels=("More", "Fewer"), difficulty=3)
c.choice("In which city was Alexander Graham Bell born?", "Edinburgh", ["London", "Boston", "Toronto"],
         "He moved to Canada with his family in 1870, then to the United States.",
         wiki("Alexander Graham Bell"), difficulty=2)
c.choice("What were the first words spoken over Alexander Graham Bell's telephone, in 1876?", "'Mr Watson, come here, I want to see you.'", ["'Hello, can you hear me?'", "'What hath God wrought?'", "'Testing, one, two, three.'"],
         "Thomas Watson was his assistant, in the next room.",
         wiki("Alexander Graham Bell"), era="classic", difficulty=3)
c.yes_no("Were Alexander Graham Bell's mother and wife both deaf?", True,
         "Bell spent much of his life teaching deaf people, and that work led him towards the telephone.",
         wiki("Alexander Graham Bell"), difficulty=3)
c.choice("Which inventor, born in what is now Croatia, pioneered the alternating current (AC) electricity we use today?", "Nikola Tesla", ["Thomas Edison", "Guglielmo Marconi", "Michael Faraday"],
         "Edison backed direct current (DC). Their rivalry was called the 'War of the Currents', and AC won.",
         wiki("Nikola Tesla"), difficulty=2)
c.choice("Which Italian inventor sent the first radio signal across the Atlantic, in 1901?", "Guglielmo Marconi", ["Alessandro Volta", "Enrico Fermi", "Galileo Galilei"],
         "The signal went from Cornwall to Newfoundland in Canada. It was the letter S in Morse code.",
         wiki("Guglielmo Marconi"), difficulty=2)
c.choice("Who invented a code of dots and dashes for sending messages by telegraph?", "Samuel Morse", ["Louis Braille", "Alan Turing", "Charles Babbage"],
         "SOS in Morse code is three dots, three dashes and three dots.",
         wiki("Samuel Morse"), difficulty=1)
c.choice("Louis Braille invented his raised-dot alphabet for blind people at roughly what age?", "15", ["25", "40", "60"],
         "He'd been blind since an accident at three years old.",
         wiki("Louis Braille"), difficulty=2)
c.choice("Which scientist flew a kite in a thunderstorm to show that lightning is electricity?", "Benjamin Franklin", ["Isaac Newton", "Thomas Edison", "Michael Faraday"],
         "He also invented bifocal glasses and the lightning rod.",
         wiki("Benjamin Franklin"), difficulty=2)
c.choice("Which mathematician designed the Analytical Engine, an early idea for a computer, in the 1830s?", "Charles Babbage", ["Alan Turing", "Isaac Newton", "John von Neumann"],
         "It was never finished. Ada Lovelace wrote what is seen as the first program for it.",
         wiki("Charles Babbage"), era="classic", difficulty=2)
c.choice("Which French scientist found a way to make milk safe by heating it, a process named after him?", "Louis Pasteur", ["Marie Curie", "Antoine Lavoisier", "Louis Braille"],
         "Pasteurisation kills harmful germs. Pasteur also made early vaccines against rabies.",
         wiki("Louis Pasteur"), difficulty=1)

c.choice("Which English engineer invented the jet engine, patenting his design in 1930?", "Frank Whittle", ["Frank Hornby", "Barnes Wallis", "Christopher Cockerell"],
         "He was a young RAF officer when he had the idea. The first British jet plane flew in 1941.",
         wiki("Frank Whittle"), difficulty=3)

# Scientists ----------------------------------------------------------------------------------------
c.choice("Which scientist's X-ray photo, called Photo 51, helped show the shape of DNA?", "Rosalind Franklin", ["Marie Curie", "Dorothy Hodgkin", "Ada Lovelace"],
         "James Watson and Francis Crick used her photo to work out the double helix in 1953.",
         wiki("Rosalind Franklin"), difficulty=2)
c.choice("Which scientist used one of the first telescopes to spot four moons going round Jupiter, in 1610?", "Galileo Galilei", ["Isaac Newton", "Nicolaus Copernicus", "Johannes Kepler"],
         "They're still called the Galilean moons: Io, Europa, Ganymede and Callisto.",
         wiki("Galileo Galilei"), difficulty=2)
c.choice("According to legend, what did Archimedes shout when he jumped out of his bath?", "Eureka!", ["Bravo!", "Hooray!", "Ta-da!"],
         "It means 'I have found it!' He'd worked out how to measure the volume of an odd shape by the water it pushes aside.",
         wiki("Eureka (word)"), difficulty=1)
c.choice("Which NASA mathematician's calculations helped John Glenn orbit the Earth in 1962?", "Katherine Johnson", ["Margaret Hamilton", "Sally Ride", "Grace Hopper"],
         "Glenn asked for her to check the computer's numbers by hand before he would fly. Her story is told in the film Hidden Figures.",
         wiki("Katherine Johnson"), difficulty=3)
c.choice("Which Canadian scientists discovered insulin, saving the lives of people with diabetes, in 1921?", "Frederick Banting and Charles Best", ["Watson and Crick", "Pierre and Marie Curie", "Fleming and Florey"],
         "Banting sold the patent for one dollar so that the medicine could be made cheaply.",
         wiki("Frederick Banting"), difficulty=3)
c.choice("Which German scientist discovered X-rays, in 1895?", "Wilhelm Röntgen", ["Albert Einstein", "Max Planck", "Robert Koch"],
         "One of the first X-ray pictures showed his wife's hand, wedding ring and all.",
         wiki("Wilhelm Röntgen"), difficulty=3)

c.choice("Which scientist, who had very little schooling, built the first electric motor and dynamo?", "Michael Faraday", ["James Clerk Maxwell", "Humphry Davy", "Thomas Edison"],
         "He started work at 13 as a bookbinder's errand boy. The farad, a unit of electricity, is named after him.",
         wiki("Michael Faraday"), difficulty=3)

# Explorers -----------------------------------------------------------------------------------------
c.choice("Which British explorer reached the South Pole in 1912, only to find Amundsen had got there first?", "Robert Falcon Scott", ["Ernest Shackleton", "Edmund Hillary", "James Cook"],
         "Scott and his four companions all died on the way back.",
         wiki("Robert Falcon Scott"), difficulty=2)
c.choice("What was the name of Ernest Shackleton's ship, crushed by Antarctic ice in 1915?", "Endurance", ["Discovery", "Titanic", "Beagle"],
         "Every one of his 28 men survived. The wreck was finally found in 2022, three kilometres down.",
         wiki("Endurance (1912 ship)"), difficulty=2)
c.choice("Which Venetian merchant wrote about his travels to China and the court of Kublai Khan?", "Marco Polo", ["Christopher Columbus", "Vasco da Gama", "Ibn Battuta"],
         "He set off in 1271, aged 17, and was away for 24 years.",
         wiki("Marco Polo"), era="classic", difficulty=2)
c.choice("Which Moroccan traveller journeyed about 120,000 km across Africa and Asia in the 1300s?", "Ibn Battuta", ["Marco Polo", "Zheng He", "Sinbad"],
         "He travelled for nearly 30 years, further than almost anyone before the age of steam.",
         wiki("Ibn Battuta"), difficulty=3)
c.choice("What were Neil Armstrong's first words when he stepped onto the Moon?", "'That's one small step for man, one giant leap for mankind.'", ["'The Eagle has landed.'", "'Houston, we have a problem.'", "'Beautiful, beautiful. Magnificent desolation.'"],
         "'The Eagle has landed' was said a few hours earlier, when the lander touched down.",
         wiki("Neil Armstrong"), difficulty=1)

# Leaders who made a mark ----------------------------------------------------------------------------------
c.choice("Which prize did Nelson Mandela share with F. W. de Klerk in 1993?", "The Nobel Peace Prize", ["The Pulitzer Prize", "The Templeton Prize", "The Order of Merit"],
         "They shared it for ending apartheid peacefully. A year later Mandela became South Africa's president.",
         wiki("Nelson Mandela"), difficulty=1)
c.choice("Nelson Mandela was often called by his clan name. What was it?", "Madiba", ["Mzee", "Baba", "Simba"],
         "People in South Africa still use it to show love and respect for him.",
         wiki("Nelson Mandela"), difficulty=2)
c.yes_no("Did Nelson Mandela wear a Springbok rugby shirt to hand over the 1995 Rugby World Cup?", True,
         "The Springbok shirt had been a symbol of white South Africa. His wearing it helped bring the country together.",
         wiki("1995 Rugby World Cup final"), difficulty=2)
c.choice("Nelson Mandela International Day is held each year on which date, his birthday?", "18 July", ["11 February", "27 April", "10 December"],
         "People are asked to spend 67 minutes helping others, one minute for each year he spent in public service.",
         wiki("Mandela Day"), difficulty=3)
c.yes_no("Did Winston Churchill win the Nobel Prize in Literature?", True,
         "He won it in 1953 for his history books and his speeches.",
         wiki("Winston Churchill"), difficulty=2)
c.choice("Which US president was elected four times, more than any other?", "Franklin D. Roosevelt", ["Abraham Lincoln", "George Washington", "Theodore Roosevelt"],
         "He led the country through the Great Depression and most of the Second World War. A president can now only serve two terms.",
         wiki("Franklin D. Roosevelt"), era="classic", difficulty=2)
c.choice("Which US president gave his name to the teddy bear?", "Theodore Roosevelt", ["Franklin D. Roosevelt", "Abraham Lincoln", "Ronald Reagan"],
         "In 1902 he refused to shoot a bear tied to a tree on a hunting trip. A toymaker named a bear after 'Teddy'.",
         wiki("Teddy bear"), difficulty=2)
c.choice("Which president said 'We choose to go to the Moon' in a famous 1962 speech?", "John F. Kennedy", ["Richard Nixon", "Dwight D. Eisenhower", "Lyndon B. Johnson"],
         "He set the goal of landing on the Moon before 1970. Apollo 11 did it in July 1969.",
         wiki("We choose to go to the Moon"), era="classic", difficulty=2)
c.choice("Whose face is on the US one-dollar bill?", "George Washington", ["Abraham Lincoln", "Benjamin Franklin", "Thomas Jefferson"],
         "Abraham Lincoln is on the five-dollar bill, and Benjamin Franklin on the hundred.",
         wiki("United States one-dollar bill"), difficulty=1)
c.choice("In 1930, Mahatma Gandhi led a 385 km march to the sea in protest against a tax on what?", "Salt", ["Tea", "Cotton", "Rice"],
         "At the end he picked up a lump of natural salt from the shore, breaking the British law.",
         wiki("Salt March"), difficulty=2)
c.choice("Which country is named after Simón Bolívar, who led much of South America to independence from Spain?", "Bolivia", ["Venezuela", "Colombia", "Ecuador"],
         "Bolívar was born in Caracas, Venezuela. He's known across South America as 'El Libertador', the Liberator.",
         wiki("Simón Bolívar"), difficulty=1)
c.choice("Which leader founded modern Turkey in 1923 and gave it a new alphabet?", "Mustafa Kemal Atatürk", ["Suleiman the Magnificent", "Ismet İnönü", "Osman I"],
         "'Atatürk' means 'father of the Turks'. In 1928 Turkish switched from Arabic letters to Latin ones.",
         wiki("Mustafa Kemal Atatürk"), difficulty=3)
c.choice("Who was the Soviet leader whose reforms helped end the Cold War, winning him the Nobel Peace Prize in 1990?", "Mikhail Gorbachev", ["Boris Yeltsin", "Leonid Brezhnev", "Nikita Khrushchev"],
         "He was the last leader of the Soviet Union, which broke up in 1991.",
         wiki("Mikhail Gorbachev"), era="classic", difficulty=2)
c.choice("Which nurse from Jamaica set up the 'British Hotel' to care for soldiers in the Crimean War?", "Mary Seacole", ["Florence Nightingale", "Edith Cavell", "Elizabeth Fry"],
         "In 2004 she was voted the greatest Black Briton in a public poll.",
         wiki("Mary Seacole"), difficulty=2)
c.choice("Which woman led the suffragettes, who campaigned for women's right to vote in Britain?", "Emmeline Pankhurst", ["Florence Nightingale", "Mary Wollstonecraft", "Queen Victoria"],
         "Their motto was 'Deeds, not words'. Her daughters Christabel and Sylvia joined the fight too.",
         wiki("Emmeline Pankhurst"), difficulty=1)
c.choice("Who escaped slavery and then led about 70 others to freedom on the 'Underground Railroad'?", "Harriet Tubman", ["Rosa Parks", "Sojourner Truth", "Maya Angelou"],
         "The Underground Railroad wasn't a real railway but a secret network of safe houses.",
         wiki("Harriet Tubman"), difficulty=2)
c.choice("Which leader is called the founding father of modern Singapore?", "Lee Kuan Yew", ["Sun Yat-sen", "Mahathir Mohamad", "Sukarno"],
         "He was its prime minister for 31 years, from 1959, as it grew from a small port to one of the world's richest places.",
         wiki("Lee Kuan Yew"), difficulty=3)
