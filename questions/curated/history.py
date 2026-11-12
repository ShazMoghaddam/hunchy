from . import Category, wiki

c = Category("history")

c.choice("In which year did the Battle of Hastings take place?", "1066", ["1087", "1215", "966"],
         "William of Normandy beat King Harold II at Hastings in 1066 and became William the Conqueror.",
         wiki("Battle of Hastings"), difficulty=2)
c.choice("Which king of England was forced to agree to the Magna Carta in 1215?", "King John", ["Henry VIII", "Richard the Lionheart", "Edward I"],
         "King John sealed the Magna Carta at Runnymede in 1215. It limited the king's power for the first time.",
         wiki("Magna Carta"), difficulty=3)
c.choice("How many wives did King Henry VIII have?", "Six", ["Four", "Five", "Eight"],
         "Henry VIII married six times. A rhyme helps remember their fates: divorced, beheaded, died, divorced, beheaded, survived.",
         wiki("Wives of Henry VIII"), difficulty=1)
c.choice("In which year did Christopher Columbus first reach the Americas?", "1492", ["1066", "1588", "1620"],
         "Columbus landed in the Bahamas in October 1492, on a voyage paid for by Spain.",
         wiki("Voyages of Christopher Columbus"), difficulty=2)
c.choice("Which famous fire destroyed much of the City of London in 1666?", "The Great Fire of London", ["The Fire of Rome", "The Blitz", "The Gunpowder Plot"],
         "The Great Fire of London started in a bakery on Pudding Lane in September 1666 and burned for about four days.",
         wiki("Great Fire of London"), difficulty=1)
c.yes_no("Did the Great Fire of London start in a bakery?", True,
         "It began at Thomas Farriner's bakery on Pudding Lane in the early hours of 2 September 1666.",
         wiki("Great Fire of London"), difficulty=2)
c.choice("Who tried to blow up the Houses of Parliament in the Gunpowder Plot of 1605?", "Guy Fawkes", ["Oliver Cromwell", "Walter Raleigh", "Francis Drake"],
         "Guy Fawkes was caught guarding the gunpowder on 5 November 1605. That's why Bonfire Night is on 5 November.",
         wiki("Gunpowder Plot"), difficulty=1)
c.choice("In which year was the Spanish Armada defeated?", "1588", ["1066", "1492", "1666"],
         "Elizabeth I's navy, helped by storms, beat Spain's great fleet of ships in 1588.",
         wiki("Spanish Armada"), era="classic", difficulty=3)
c.choice("Which city was buried when Mount Vesuvius erupted in AD 79?", "Pompeii", ["Rome", "Athens", "Venice"],
         "Ash from Vesuvius buried Pompeii so quickly that streets, homes and even loaves of bread were preserved.",
         wiki("Pompeii"), difficulty=1)
c.choice("On which day in 44 BC was Julius Caesar killed?", "The Ides of March", ["New Year's Day", "Midsummer's Day", "The Ides of June"],
         "Caesar was stabbed by Roman senators on the Ides of March, 15 March, 44 BC.",
         wiki("Assassination of Julius Caesar"), difficulty=3)
c.choice("Which Roman emperor ordered a wall built across northern Britain?", "Hadrian", ["Nero", "Augustus", "Caligula"],
         "Building of Hadrian's Wall began in AD 122. Parts of it still stand today.",
         wiki("Hadrian's Wall"), difficulty=2)
c.choice("Whose tomb did Howard Carter find in Egypt's Valley of the Kings in 1922?", "Tutankhamun", ["Cleopatra", "Ramesses II", "Khufu"],
         "Tutankhamun's tomb was found almost untouched, packed with treasures including his famous gold mask.",
         wiki("Tutankhamun"), difficulty=2)
c.higher_lower("The Great Pyramid of Giza was built around 2560 BC. Was Stonehenge's first stage built earlier or later?", True,
               "The first stage of Stonehenge, a circular ditch and bank, was built around 3000 BC, a few centuries before the Great Pyramid.",
               wiki("Stonehenge"), labels=("Earlier", "Later"), difficulty=3)
c.choice("Which country did Germany invade on 1 September 1939, starting the Second World War in Europe?", "Poland", ["France", "Belgium", "Russia"],
         "Britain and France declared war on Germany two days later, on 3 September 1939.",
         wiki("Invasion of Poland"), era="classic", difficulty=2)
c.choice("In which year did the Second World War end?", "1945", ["1918", "1939", "1950"],
         "The war in Europe ended in May 1945, and in Asia in August, with Japan's formal surrender on 2 September 1945.",
         wiki("World War II"), era="classic", difficulty=1)
c.choice("In which year did the First World War begin?", "1914", ["1939", "1905", "1918"],
         "The war began in the summer of 1914 and ended with an armistice on 11 November 1918.",
         wiki("World War I"), era="classic", difficulty=1)
c.yes_no("Did the First World War end with an armistice at 11 o'clock on the 11th day of the 11th month?", True,
         "The guns fell silent at 11am on 11 November 1918. That's why Remembrance Day is held on 11 November.",
         wiki("Armistice of 11 November 1918"), era="classic", difficulty=2)
c.choice("Whose assassination in Sarajevo in 1914 helped spark the First World War?", "Archduke Franz Ferdinand", ["Tsar Nicholas II", "Kaiser Wilhelm II", "King George V"],
         "Franz Ferdinand, heir to the throne of Austria-Hungary, was shot in Sarajevo on 28 June 1914.",
         wiki("Assassination of Archduke Franz Ferdinand"), era="classic", difficulty=3)
c.choice("What was the code name for the Allied landings in Normandy on D-Day, 6 June 1944?", "Operation Overlord", ["Operation Barbarossa", "Operation Desert Storm", "Operation Sea Lion"],
         "Overlord was the whole invasion. The landings on the beaches themselves were called Operation Neptune.",
         wiki("Operation Overlord"), era="classic", difficulty=3)
c.choice("During the Second World War, which battle was fought in the skies over southern England in 1940?", "The Battle of Britain", ["The Battle of the Bulge", "The Battle of Midway", "The Battle of Waterloo"],
         "The RAF fought the German air force from July to October 1940, stopping a planned invasion.",
         wiki("Battle of Britain"), era="classic", difficulty=2)
c.choice("In 1940, more than 330,000 soldiers were rescued from the beaches of which French town?", "Dunkirk", ["Calais", "Normandy", "Brest"],
         "Hundreds of small boats, many owned by ordinary people, helped the navy carry soldiers home from Dunkirk.",
         wiki("Dunkirk evacuation"), era="classic", difficulty=2)
c.choice("Which American naval base was attacked by Japan on 7 December 1941?", "Pearl Harbor", ["San Diego", "Guantanamo Bay", "Norfolk"],
         "The attack on Pearl Harbor in Hawaii brought the United States into the Second World War.",
         wiki("Attack on Pearl Harbor"), era="classic", difficulty=2)
c.choice("In which city did Anne Frank hide with her family during the Second World War?", "Amsterdam", ["Berlin", "Paris", "Vienna"],
         "Anne Frank wrote her famous diary while hiding in a secret annexe in Amsterdam from 1942 to 1944.",
         wiki("Anne Frank"), era="classic", difficulty=2)
c.choice("Who was Britain's prime minister for most of the Second World War?", "Winston Churchill", ["Neville Chamberlain", "Clement Attlee", "Harold Wilson"],
         "Churchill became prime minister in May 1940 and led Britain until July 1945.",
         wiki("Winston Churchill"), era="classic", difficulty=1)
c.choice("In which year did the Berlin Wall fall?", "1989", ["1961", "1975", "1991"],
         "The border opened on the night of 9 November 1989, and Germany was reunited the next year.",
         wiki("Fall of the Berlin Wall"), era="classic", difficulty=2)
c.higher_lower("The Berlin Wall fell in 1989. Was it first built before or after 1960?", False,
               "Building began on 13 August 1961, so the wall stood for 28 years.",
               wiki("Berlin Wall"), labels=("Before", "After"), era="classic", difficulty=3)
c.choice("In which year did the Titanic sink?", "1912", ["1905", "1921", "1898"],
         "The Titanic hit an iceberg on its first voyage and sank in the early hours of 15 April 1912.",
         wiki("Titanic"), difficulty=1)
c.yes_no("Was the Titanic on its very first voyage when it sank?", True,
         "It had set off from Southampton on its maiden voyage to New York.",
         wiki("Titanic"), difficulty=1)
c.choice("In which year did people first walk on the Moon?", "1969", ["1959", "1972", "1965"],
         "Neil Armstrong and Buzz Aldrin landed on the Moon on 20 July 1969.",
         wiki("Apollo 11"), era="classic", difficulty=1)
c.choice("In which year did the French Revolution begin with the storming of the Bastille?", "1789", ["1815", "1776", "1848"],
         "Crowds stormed the Bastille prison in Paris on 14 July 1789. France still celebrates 14 July as its national day.",
         wiki("Storming of the Bastille"), difficulty=3)
c.choice("Which famous battle in 1815 ended Napoleon's rule for good?", "Waterloo", ["Trafalgar", "Austerlitz", "Hastings"],
         "Wellington's British-led army and the Prussians beat Napoleon at Waterloo, in what is now Belgium.",
         wiki("Battle of Waterloo"), difficulty=2)
c.choice("At which sea battle in 1805 was Admiral Nelson killed?", "Trafalgar", ["Waterloo", "Jutland", "The Nile"],
         "Nelson won the Battle of Trafalgar but was shot during it. Nelson's Column in Trafalgar Square remembers him.",
         wiki("Battle of Trafalgar"), difficulty=3)
c.choice("In which year did the United States declare its independence from Britain?", "1776", ["1789", "1812", "1700"],
         "The Declaration of Independence was adopted on 4 July 1776, which is why Americans celebrate the Fourth of July.",
         wiki("United States Declaration of Independence"), difficulty=2)
c.choice("In which country did the Industrial Revolution begin?", "Great Britain", ["Germany", "The United States", "France"],
         "Factories, steam engines and new machines spread across Britain from the second half of the 1700s.",
         wiki("Industrial Revolution"), difficulty=2)
c.choice("Who were the first people to fly a powered aeroplane, in 1903?", "The Wright brothers", ["The Montgolfier brothers", "Charles Lindbergh", "Amelia Earhart"],
         "Orville and Wilbur Wright flew at Kitty Hawk, North Carolina, on 17 December 1903. The first flight lasted 12 seconds.",
         wiki("Wright brothers"), difficulty=2)
c.higher_lower("Queen Victoria reigned for 63 years. Did Queen Elizabeth II reign for longer or shorter?", True,
               "Elizabeth II reigned for 70 years, from 1952 to 2022: longer than any other British monarch.",
               wiki("Elizabeth II"), labels=("Longer", "Shorter"), difficulty=1)
c.choice("Which group of Scandinavian raiders attacked the monastery of Lindisfarne in 793?", "The Vikings", ["The Romans", "The Normans", "The Saxons"],
         "The raid on Lindisfarne, off the coast of Northumberland, is often taken as the start of the Viking Age in Britain.",
         wiki("Lindisfarne"), difficulty=1)
c.choice("Which terrible disease killed a huge share of Europe's people in the late 1340s?", "The Black Death", ["Smallpox", "Cholera", "Spanish flu"],
         "The Black Death, a plague, killed somewhere between a third and a half of Europe's population.",
         wiki("Black Death"), difficulty=2)
c.choice("Who was released from prison in 1990 and became South Africa's president in 1994?", "Nelson Mandela", ["Desmond Tutu", "F. W. de Klerk", "Thabo Mbeki"],
         "Mandela spent 27 years in prison. He became South Africa's first Black president.",
         wiki("Nelson Mandela"), era="classic", difficulty=1)
c.choice("Which American civil rights campaigner made the 'I Have a Dream' speech in 1963?", "Martin Luther King Jr.", ["Malcolm X", "Rosa Parks", "Barack Obama"],
         "He gave the speech to about 250,000 people at the March on Washington on 28 August 1963.",
         wiki("I Have a Dream"), era="classic", difficulty=1)
c.yes_no("Did Rosa Parks refuse to give up her seat on a bus in Montgomery, Alabama, in 1955?", True,
         "Her arrest led to the Montgomery bus boycott, a turning point in the American civil rights movement.",
         wiki("Rosa Parks"), era="classic", difficulty=2)
c.choice("In which year did a nuclear reactor explode at Chernobyl?", "1986", ["1979", "1991", "1966"],
         "Reactor 4 at Chernobyl, in what is now Ukraine, exploded on 26 April 1986.",
         wiki("Chernobyl disaster"), era="classic", difficulty=3)
c.choice("Which crisis in 1962 brought the USA and the Soviet Union close to nuclear war?", "The Cuban Missile Crisis", ["The Suez Crisis", "The Berlin Airlift", "The Korean War"],
         "For 13 days in October 1962 the world held its breath over Soviet missiles in Cuba.",
         wiki("Cuban Missile Crisis"), era="classic", difficulty=2)
c.choice("In which year did the Channel Tunnel between England and France open?", "1994", ["1984", "2000", "1975"],
         "The tunnel opened in May 1994. Its rail tunnels are about 50 km long, with about 38 km under the sea.",
         wiki("Channel Tunnel"), era="classic", difficulty=2)
c.choice("In which year did euro notes and coins first go into people's pockets?", "2002", ["1999", "1992", "2008"],
         "The euro started for banks in 1999. Notes and coins arrived on 1 January 2002.",
         wiki("Euro"), era="modern", difficulty=3)
c.choice("In 1893, which became the first self-governing country to let all women vote in national elections?", "New Zealand", ["The United Kingdom", "The United States", "France"],
         "New Zealand women won the right to vote in national elections in 1893, decades before most of the world.",
         wiki("Women's suffrage in New Zealand"), difficulty=3)
c.choice("Who led the Allied armies in Europe on D-Day and later became US president?", "Dwight D. Eisenhower", ["George Patton", "Harry Truman", "John F. Kennedy"],
         "Eisenhower was Supreme Commander of the Allied forces in Europe, and US president from 1953 to 1961.",
         wiki("Dwight D. Eisenhower"), era="classic", difficulty=3)
c.true_false("The ancient Olympic Games were held in Greece.", True,
             "They were held at Olympia, in honour of the god Zeus. The first recorded Games are traditionally dated to 776 BC.",
             wiki("Ancient Olympic Games"), difficulty=1)
c.choice("Which ancient wonder was a giant statue standing at a harbour on a Greek island?", "The Colossus of Rhodes", ["The Statue of Liberty", "The Sphinx", "The Lighthouse of Alexandria"],
         "The bronze Colossus stood on Rhodes for only about 54 years before an earthquake toppled it in 226 BC.",
         wiki("Colossus of Rhodes"), difficulty=3)
c.choice("In 1773, colonists angry about British taxes threw tea into the harbour of which American city?", "Boston", ["New York", "Philadelphia", "Baltimore"],
         "The Boston Tea Party saw 342 chests of tea thrown into the harbour. It was a step towards the American Revolution.",
         wiki("Boston Tea Party"), difficulty=1)

assert len(c.questions) == 50, len(c.questions)
