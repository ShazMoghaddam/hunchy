"""Leaders and famous people. Questions about who holds a job *now* are left out on purpose: they go out of date,
sometimes within months. Everything here is settled history."""

from . import Category, wiki

c = Category("people")

# Leaders
c.choice("Who was Britain's first woman prime minister?", "Margaret Thatcher", ["Theresa May", "Liz Truss", "Barbara Castle"],
         "Margaret Thatcher was prime minister from 1979 to 1990, longer than anyone else in the 20th century.",
         wiki("Margaret Thatcher"), era="classic", difficulty=1)
c.higher_lower("Margaret Thatcher became prime minister in 1979. Did Tony Blair become prime minister before or after 2000?", True,
               "Tony Blair became prime minister in May 1997 and served until 2007.",
               wiki("Tony Blair"), labels=("Before", "After"), era="classic", difficulty=2)
c.choice("Which British prime minister called the 2016 referendum on leaving the European Union?", "David Cameron", ["Theresa May", "Boris Johnson", "Gordon Brown"],
         "David Cameron called the referendum and resigned the morning after the vote to leave.",
         wiki("David Cameron"), era="modern", difficulty=2)
c.choice("Who is usually counted as Britain's first prime minister?", "Robert Walpole", ["William Pitt the Younger", "Winston Churchill", "Benjamin Disraeli"],
         "Sir Robert Walpole led the government from 1721 to 1742, and is generally regarded as the first prime minister.",
         wiki("Robert Walpole"), era="classic", difficulty=3)
c.choice("What is the address of the British prime minister's official home in London?", "10 Downing Street", ["1 Downing Street", "221B Baker Street", "11 Whitehall"],
         "Robert Walpole moved into Number 10 in 1735. It has been the prime minister's home and office ever since.",
         wiki("10 Downing Street"), difficulty=1)
c.choice("Who was the first president of the United States?", "George Washington", ["Abraham Lincoln", "Thomas Jefferson", "John Adams"],
         "George Washington became president in 1789. The capital city, Washington D.C., is named after him.",
         wiki("George Washington"), difficulty=1)
c.choice("Which US president issued the Emancipation Proclamation and gave the Gettysburg Address?", "Abraham Lincoln", ["George Washington", "Theodore Roosevelt", "Ulysses S. Grant"],
         "Lincoln was the 16th president. He led the country through the American Civil War and pushed through the end of slavery.",
         wiki("Abraham Lincoln"), difficulty=2)
c.choice("Who was the first Black president of the United States?", "Barack Obama", ["Joe Biden", "Colin Powell", "Jesse Jackson"],
         "Barack Obama was the 44th president, from 2009 to 2017.",
         wiki("Barack Obama"), era="modern", difficulty=1)
c.choice("Which US president was assassinated in Dallas in 1963?", "John F. Kennedy", ["Abraham Lincoln", "Richard Nixon", "Ronald Reagan"],
         "John F. Kennedy was shot in Dallas, Texas, on 22 November 1963.",
         wiki("John F. Kennedy"), era="classic", difficulty=2)
c.choice("Who was the US president when astronauts first landed on the Moon in 1969?", "Richard Nixon", ["John F. Kennedy", "Lyndon B. Johnson", "Jimmy Carter"],
         "Nixon spoke to Neil Armstrong and Buzz Aldrin by phone while they were on the Moon.",
         wiki("Richard Nixon"), era="classic", difficulty=3)
c.choice("Which US president had been a Hollywood film actor?", "Ronald Reagan", ["Jimmy Carter", "Bill Clinton", "Gerald Ford"],
         "Ronald Reagan acted in dozens of films before going into politics. He was president from 1981 to 1989.",
         wiki("Ronald Reagan"), era="classic", difficulty=2)
c.choice("Who was the first woman to be Chancellor of Germany?", "Angela Merkel", ["Ursula von der Leyen", "Theresa May", "Christine Lagarde"],
         "Angela Merkel led Germany for 16 years, from 2005 to 2021.",
         wiki("Angela Merkel"), era="modern", difficulty=2)
c.choice("Which Indian leader led a peaceful campaign for independence from Britain?", "Mahatma Gandhi", ["Jawaharlal Nehru", "Indira Gandhi", "Narendra Modi"],
         "Gandhi led protests without violence, like the 1930 Salt March. India became independent in 1947.",
         wiki("Mahatma Gandhi"), difficulty=1)
c.choice("Who crowned himself Emperor of the French in 1804?", "Napoleon Bonaparte", ["Louis XIV", "Charlemagne", "Louis XVI"],
         "Napoleon took the crown from the Pope's hands and placed it on his own head at Notre-Dame in Paris.",
         wiki("Coronation of Napoleon"), difficulty=2)
c.choice("Who was the last active ruler of ancient Egypt's Ptolemaic kingdom?", "Cleopatra", ["Nefertiti", "Hatshepsut", "Tutankhamun"],
         "Cleopatra VII ruled Egypt until her death in 30 BC, after which Egypt became part of the Roman Empire.",
         wiki("Cleopatra"), difficulty=2)
c.choice("Which queen ruled England when Shakespeare's first plays were performed?", "Elizabeth I", ["Victoria", "Mary I", "Anne"],
         "Elizabeth I reigned from 1558 to 1603, a golden age for English theatre.",
         wiki("Elizabeth I"), difficulty=3)
c.choice("In which year was King Charles III crowned at Westminster Abbey?", "2023", ["2022", "2024", "2021"],
         "Charles became king in September 2022. His coronation was on 6 May 2023.",
         wiki("Coronation of Charles III and Camilla"), era="modern", difficulty=2)
c.choice("Who was Britain's longest-reigning monarch?", "Elizabeth II", ["Victoria", "George III", "Henry VIII"],
         "Queen Elizabeth II reigned for 70 years, from 1952 until her death in 2022.",
         wiki("Elizabeth II"), difficulty=1)
c.true_false("Queen Victoria became queen when she was 18 years old.", True,
             "Victoria came to the throne in 1837, a month after her 18th birthday.",
             wiki("Queen Victoria"), difficulty=2)
c.choice("Who was the first woman to become president of a country in a national election, in Iceland in 1980?", "Vigdís Finnbogadóttir", ["Golda Meir", "Indira Gandhi", "Benazir Bhutto"],
         "Vigdís Finnbogadóttir served as Iceland's president for 16 years.",
         wiki("Vigdís Finnbogadóttir"), era="classic", difficulty=3)

# Scientists, writers and explorers
c.choice("Which scientist came up with the famous equation E = mc²?", "Albert Einstein", ["Isaac Newton", "Stephen Hawking", "Marie Curie"],
         "Einstein published it in 1905. It shows that mass and energy are two forms of the same thing.",
         wiki("Albert Einstein"), difficulty=1)
c.choice("Who was the first woman to win a Nobel Prize?", "Marie Curie", ["Florence Nightingale", "Rosalind Franklin", "Ada Lovelace"],
         "Marie Curie won in 1903 for physics, and again in 1911 for chemistry.",
         wiki("Marie Curie"), difficulty=2)
c.yes_no("Did Marie Curie win Nobel Prizes in two different sciences?", True,
         "She won the physics prize in 1903 and the chemistry prize in 1911. She is still the only person to win in two different sciences.",
         wiki("Marie Curie"), difficulty=3)
c.choice("Which scientist is famous for a story about an apple and gravity?", "Isaac Newton", ["Galileo Galilei", "Charles Darwin", "Albert Einstein"],
         "Newton said that watching an apple fall helped him think about gravity. The apple tree still grows at his home, Woolsthorpe Manor.",
         wiki("Isaac Newton"), difficulty=1)
c.choice("Which naturalist sailed on HMS Beagle and wrote On the Origin of Species?", "Charles Darwin", ["David Attenborough", "Alfred Wallace", "Gregor Mendel"],
         "Darwin's voyage lasted almost five years. His book about evolution came out in 1859.",
         wiki("Charles Darwin"), difficulty=2)
c.choice("Which nurse became known as 'The Lady with the Lamp'?", "Florence Nightingale", ["Mary Seacole", "Edith Cavell", "Clara Barton"],
         "Florence Nightingale cared for soldiers in the Crimean War and went on to found modern nursing.",
         wiki("Florence Nightingale"), difficulty=2)
c.choice("Who was the first person to walk on the Moon?", "Neil Armstrong", ["Buzz Aldrin", "Yuri Gagarin", "Michael Collins"],
         "Armstrong stepped onto the Moon on 20 July 1969, followed by Buzz Aldrin about 20 minutes later.",
         wiki("Neil Armstrong"), era="classic", difficulty=1)
c.choice("Who was the first woman to fly solo across the Atlantic Ocean?", "Amelia Earhart", ["Amy Johnson", "Bessie Coleman", "Valentina Tereshkova"],
         "Amelia Earhart flew from Newfoundland to Northern Ireland in 1932.",
         wiki("Amelia Earhart"), era="classic", difficulty=2)
c.choice("Which mathematician is often called the first computer programmer?", "Ada Lovelace", ["Alan Turing", "Charles Babbage", "Grace Hopper"],
         "In the 1840s Ada Lovelace wrote what is seen as the first program, for Charles Babbage's planned Analytical Engine.",
         wiki("Ada Lovelace"), difficulty=3)
c.choice("Which mathematician helped break the Enigma code in the Second World War?", "Alan Turing", ["Ada Lovelace", "Tim Berners-Lee", "John von Neumann"],
         "Alan Turing worked at Bletchley Park. He is on the Bank of England's £50 note.",
         wiki("Alan Turing"), era="classic", difficulty=2)
c.choice("In which town was William Shakespeare born?", "Stratford-upon-Avon", ["London", "Oxford", "Canterbury"],
         "Shakespeare was born in Stratford-upon-Avon in 1564. You can still visit the house he was born in.",
         wiki("William Shakespeare"), difficulty=2)
c.choice("Who wrote A Christmas Carol, the story of Ebenezer Scrooge?", "Charles Dickens", ["Jane Austen", "Lewis Carroll", "Thomas Hardy"],
         "Dickens wrote it in just six weeks. It was published on 19 December 1843 and sold out by Christmas Eve.",
         wiki("A Christmas Carol"), difficulty=1)
c.choice("In which year was the first Harry Potter book published?", "1997", ["2001", "1993", "1999"],
         "Harry Potter and the Philosopher's Stone was first published in the UK in June 1997.",
         wiki("Harry Potter and the Philosopher's Stone"), era="modern", difficulty=2)
c.choice("Who wrote Charlie and the Chocolate Factory?", "Roald Dahl", ["J. K. Rowling", "David Walliams", "Enid Blyton"],
         "Roald Dahl's book first came out in 1964. He also wrote Matilda, The BFG and The Witches.",
         wiki("Charlie and the Chocolate Factory"), difficulty=1)
c.choice("Who wrote The Lion, the Witch and the Wardrobe?", "C. S. Lewis", ["J. R. R. Tolkien", "Lewis Carroll", "Philip Pullman"],
         "It came out in 1950, the first of the seven Chronicles of Narnia books to be published.",
         wiki("The Lion, the Witch and the Wardrobe"), difficulty=2)
c.choice("Who wrote The Hobbit and The Lord of the Rings?", "J. R. R. Tolkien", ["C. S. Lewis", "George R. R. Martin", "Terry Pratchett"],
         "The Hobbit came out in 1937. Tolkien was a professor of English at Oxford.",
         wiki("J. R. R. Tolkien"), difficulty=2)
c.choice("Which explorer led the first expedition to reach the South Pole, in 1911?", "Roald Amundsen", ["Robert Falcon Scott", "Ernest Shackleton", "Edmund Hillary"],
         "Amundsen's Norwegian team got there on 14 December 1911, about five weeks before Scott's British team.",
         wiki("Roald Amundsen"), difficulty=3)
c.choice("Who first reached the top of Mount Everest with Tenzing Norgay in 1953?", "Edmund Hillary", ["George Mallory", "Reinhold Messner", "Chris Bonington"],
         "The New Zealander Edmund Hillary and the Sherpa Tenzing Norgay reached the summit on 29 May 1953.",
         wiki("Edmund Hillary"), era="classic", difficulty=2)
c.choice("Which British scientist invented the World Wide Web?", "Tim Berners-Lee", ["Alan Turing", "Bill Gates", "Steve Jobs"],
         "Tim Berners-Lee came up with the idea in 1989 while working at CERN in Switzerland.",
         wiki("Tim Berners-Lee"), era="modern", difficulty=2)
c.choice("Which famous naturalist presented the TV series Blue Planet and Planet Earth?", "David Attenborough", ["Chris Packham", "Steve Irwin", "Bear Grylls"],
         "David Attenborough has made nature films for the BBC for more than 70 years.",
         wiki("David Attenborough"), difficulty=1)

assert len(c.questions) == 40, len(c.questions)
