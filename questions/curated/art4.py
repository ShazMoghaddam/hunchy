"""More Art & Culture: the world's great museums, artists, buildings, books and the stage."""

from . import Category, wiki

c = Category("art", prefix="art4")

# Museums in London and around Britain ---------------------------------------------------------------
c.choice("Which London museum is named after Queen Victoria and her husband?", "The V&A", ["The Wallace Collection", "The National Gallery", "The Science Museum"],
         "The Victoria and Albert Museum opened in 1852. It's the world's biggest museum of art and design.",
         wiki("Victoria and Albert Museum"), difficulty=1)
c.choice("Which London museum is home to the Apollo 10 space capsule and Puffing Billy, the oldest steam engine still around?", "The Science Museum", ["The Natural History Museum", "The V&A", "The British Museum"],
         "Apollo 10 flew round the Moon in 1969, two months before the first landing. It's on loan from the Smithsonian in Washington.",
         wiki("Science Museum, London"), difficulty=2)
c.yes_no("Is it free to visit the main collections of the Science Museum, the Natural History Museum and the V&A?", True,
         "Britain's national museums have been free to enter since 2001. The three stand next to each other in South Kensington.",
         wiki("Science Museum, London"), difficulty=1)
c.choice("Which London gallery on Trafalgar Square has one of Van Gogh's Sunflowers?", "The National Gallery", ["Tate Britain", "Tate Modern", "The Courtauld"],
         "It opened in 1824 and is free to visit. Van Gogh painted several Sunflowers pictures, now spread around the world.",
         wiki("National Gallery"), difficulty=2)
c.choice("Tate has galleries in London, Liverpool and which Cornish seaside town?", "St Ives", ["Falmouth", "Newquay", "Penzance"],
         "St Ives has drawn artists for over a century because of its clear, bright light.",
         wiki("Tate St Ives"), difficulty=2)
c.choice("Which famous London attraction is full of wax figures of the famous?", "Madame Tussauds", ["The London Dungeon", "The Sherlock Holmes Museum", "Ripley's Believe It or Not!"],
         "Marie Tussaud brought her wax figures from Paris to Britain in 1802, and toured them for over 30 years before settling in Baker Street.",
         wiki("Madame Tussauds"), difficulty=1)
c.choice("Which Second World War warship is now a museum moored on the Thames by Tower Bridge?", "HMS Belfast", ["HMS Victory", "The Cutty Sark", "The Golden Hinde"],
         "She fired some of the first shots on D-Day in 1944.",
         wiki("HMS Belfast"), difficulty=2)
c.choice("Which famous sailing ship, once one of the fastest tea clippers, is now a museum in Greenwich?", "The Cutty Sark", ["HMS Victory", "The Golden Hinde", "The Mary Rose"],
         "She was launched in 1869. Her name comes from a Robert Burns poem, in which a 'cutty sark' is a short nightdress worn by a witch.",
         wiki("Cutty Sark"), difficulty=2)
c.choice("Which Manchester museum includes the world's oldest surviving passenger railway station?", "The Science and Industry Museum", ["The Whitworth", "The Lowry", "The People's History Museum"],
         "Liverpool Road station opened in 1830, on the world's first inter-city railway.",
         wiki("Science and Industry Museum"), difficulty=3)
c.choice("Which city has the National Railway Museum, home of the record-breaking Mallard?", "York", ["Derby", "Crewe", "Darlington"],
         "Mallard reached 126 miles an hour in 1938, still the world record for a steam locomotive.",
         wiki("National Railway Museum"), difficulty=2, as_of="2026")
c.choice("Where can you see Dolly the sheep, the first mammal cloned from an adult cell?", "The National Museum of Scotland", ["The Natural History Museum", "The Science Museum", "The Roslin Institute"],
         "Dolly was cloned at the Roslin Institute, near Edinburgh, but her stuffed body went on show at the museum after she died in 2003.",
         wiki("Dolly (sheep)"), difficulty=3)

# Museums around the world --------------------------------------------------------------------------
c.choice("Which Paris museum has a glass pyramid at its entrance?", "The Louvre", ["The Musée d'Orsay", "The Centre Pompidou", "The Musée Rodin"],
         "The architect I. M. Pei designed the pyramid. It opened in 1989, and many Parisians hated it at first.",
         wiki("Louvre Pyramid"), difficulty=1)
c.choice("What was the Louvre before it became a museum?", "A royal fortress, then a palace", ["A railway station", "A prison", "A cathedral"],
         "It began as a fortress around 1200. The Musée d'Orsay is the one in an old railway station.",
         wiki("Louvre Palace"), difficulty=2)
c.choice("In October 2025, thieves stole jewels in a daylight raid on which famous museum?", "The Louvre", ["The British Museum", "The Prado", "The Rijksmuseum"],
         "They rode up to a balcony window of the Apollo Gallery, where the French crown jewels are kept, on a mechanical lift, and were in and out in about four minutes.",
         wiki("2025 Louvre robbery"), era="modern", difficulty=2)
c.higher_lower("Is the Mona Lisa more or less than a metre tall?", False,
               "Less: it's only about 77 centimetres tall and 53 wide, which surprises many visitors.",
               wiki("Mona Lisa"), labels=("More", "Less"), difficulty=2)
c.choice("Which Paris museum has its pipes and escalators on the outside of the building?", "The Centre Pompidou", ["The Louvre", "The Musée d'Orsay", "The Fondation Louis Vuitton"],
         "Richard Rogers and Renzo Piano designed it, and it opened in 1977. The pipes are colour-coded: blue for air, green for water.",
         wiki("Centre Pompidou"), difficulty=2)
c.choice("Which Amsterdam museum has the world's biggest collection of Van Gogh's work?", "The Van Gogh Museum", ["The Rijksmuseum", "The Stedelijk Museum", "The Kröller-Müller Museum"],
         "It has around 200 of his paintings. The Kröller-Müller, also in the Netherlands, has the second-biggest.",
         wiki("Van Gogh Museum"), difficulty=1)
c.choice("Which Amsterdam museum is the building where Anne Frank and her family hid during the Second World War?", "The Anne Frank House", ["The Rembrandt House", "The Rijksmuseum", "The Resistance Museum"],
         "They hid in a secret annex behind a bookcase for two years. Her diary has been translated into more than 70 languages.",
         wiki("Anne Frank House"), difficulty=2)
c.higher_lower("Is Rembrandt's The Night Watch wider or narrower than four metres?", True,
               "Wider: it's about 4.4 metres across. In 1715 it was cut down on all four sides to fit between two doors.",
               wiki("The Night Watch"), labels=("Wider", "Narrower"), difficulty=3)
c.choice("In which city is MoMA, the Museum of Modern Art, home to Van Gogh's The Starry Night?", "New York", ["Chicago", "Los Angeles", "Washington, D.C."],
         "Many people expect The Starry Night to be in Amsterdam, but MoMA has owned it since 1941.",
         wiki("Museum of Modern Art"), difficulty=2)
c.choice("Which New York museum is in a white spiral building by Frank Lloyd Wright?", "The Guggenheim", ["MoMA", "The Met", "The Whitney"],
         "It opened in 1959. Visitors take a lift to the top and walk down a long spiral ramp.",
         wiki("Solomon R. Guggenheim Museum"), difficulty=2)
c.choice("Which New York museum hosts the Met Gala, fashion's biggest night?", "The Metropolitan Museum of Art", ["MoMA", "The Guggenheim", "The American Museum of Natural History"],
         "It's held on the first Monday in May to raise money for the museum's Costume Institute.",
         wiki("Met Gala"), era="modern", difficulty=1)
c.choice("Which group of free museums in Washington, D.C., was founded with money left by a British scientist who never visited America?", "The Smithsonian", ["The Getty", "The Frick", "The Guggenheim"],
         "James Smithson left his fortune to the United States in 1829. The Smithsonian now has over 20 museums, plus the National Zoo.",
         wiki("Smithsonian Institution"), difficulty=3)
c.choice("In which city is the Hermitage, an art museum in a former royal palace?", "Saint Petersburg", ["Moscow", "Vienna", "Prague"],
         "Its main building is the Winter Palace. Cats have lived in its basements for centuries, to keep mice away from the paintings.",
         wiki("Hermitage Museum"), difficulty=2)
c.choice("Which tiny country is home to the Sistine Chapel?", "Vatican City", ["Italy", "San Marino", "Monaco"],
         "A tricky one: it's surrounded by Rome, but Vatican City is its own country, the smallest in the world.",
         wiki("Sistine Chapel"), difficulty=2)
c.choice("Which Florence museum is home to Michelangelo's statue of David?", "The Galleria dell'Accademia", ["The Uffizi", "The Bargello", "The Pitti Palace"],
         "David was moved indoors in 1873 to protect it. A copy stands where it used to be, in the Piazza della Signoria.",
         wiki("David (Michelangelo)"), difficulty=3)
c.higher_lower("Is Michelangelo's David taller or shorter than four metres?", True,
               "Taller: about 5.2 metres. He carved it from one block of marble that other sculptors had given up on.",
               wiki("David (Michelangelo)"), labels=("Taller", "Shorter"), difficulty=2)
c.choice("Which Madrid museum has Picasso's huge painting Guernica?", "The Reina Sofía", ["The Prado", "The Thyssen-Bornemisza", "The Picasso Museum"],
         "Picasso painted it in 1937 after the bombing of the town of Guernica. It only came to Spain in 1981, after years in New York.",
         wiki("Guernica (Picasso)"), difficulty=3)
c.choice("Which museum opened a branch in Abu Dhabi in 2017, under a huge latticed dome?", "The Louvre", ["The Prado", "The British Museum", "The Met"],
         "Jean Nouvel designed it. Sunlight falls through the dome like light through palm leaves.",
         wiki("Louvre Abu Dhabi"), era="modern", difficulty=2)
c.choice("The Grand Egyptian Museum, which fully opened in 2025, stands near which famous sight?", "The Pyramids of Giza", ["The Valley of the Kings", "Abu Simbel", "Karnak"],
         "It's one of the biggest museums in the world, and shows all of Tutankhamun's treasures together for the first time.",
         wiki("Grand Egyptian Museum"), era="modern", difficulty=2)
c.choice("Which German city has a Museum Island, with five museums on an island in the river?", "Berlin", ["Munich", "Hamburg", "Dresden"],
         "The island is in the River Spree, and is a UNESCO World Heritage Site.",
         wiki("Museum Island"), difficulty=2)
c.choice("Which Italian city is home to La Scala, one of the world's most famous opera houses?", "Milan", ["Rome", "Venice", "Naples"],
         "La Scala opened in 1778. Tickets for its opening night each December are among the hardest to get in the opera world.",
         wiki("La Scala"), difficulty=2)

# Artists and artworks ------------------------------------------------------------------------------
c.choice("Which artist's Salvator Mundi sold for 450 million dollars in 2017, a record for a painting at auction?", "Leonardo da Vinci", ["Pablo Picasso", "Vincent van Gogh", "Andy Warhol"],
         "Nobody is completely sure Leonardo painted all of it, and where it is now has been a mystery for years.",
         wiki("Salvator Mundi (Leonardo)"), difficulty=2)
c.yes_no("Did Leonardo da Vinci write many of his notes backwards, in mirror writing?", True,
         "He wrote from right to left, so his notebooks are easiest to read in a mirror. He was left-handed.",
         wiki("Leonardo da Vinci"), difficulty=2)
c.yes_no("Was Banksy's Girl with Balloon shredded just after it sold at auction?", True,
         "In 2018, a shredder hidden in the frame cut half of it into strips. Renamed Love Is in the Bin, it sold again in 2021 for far more.",
         wiki("Love Is in the Bin"), era="modern", difficulty=1)
c.yes_no("Was Frida Kahlo married to the painter Diego Rivera?", True,
         "Twice: they married in 1929, divorced in 1939 and married again a year later.",
         wiki("Frida Kahlo"), difficulty=2)
c.choice("Who painted The Garden of Earthly Delights, full of strange creatures?", "Hieronymus Bosch", ["Pieter Bruegel the Elder", "Jan van Eyck", "Rembrandt"],
         "Bosch painted it about 500 years ago. It's in the Prado in Madrid.",
         wiki("The Garden of Earthly Delights"), difficulty=3)
c.choice("Who painted The Arnolfini Portrait, with a tiny round mirror reflecting the whole room?", "Jan van Eyck", ["Hans Holbein the Younger", "Hieronymus Bosch", "Pieter Bruegel the Elder"],
         "He painted it in 1434. It hangs in the National Gallery in London.",
         wiki("Arnolfini Portrait"), difficulty=3)
c.choice("Which German artist painted the famous portraits of Henry VIII?", "Hans Holbein the Younger", ["Albrecht Dürer", "Lucas Cranach", "Anthony van Dyck"],
         "Holbein was the king's court painter. His picture of Anne of Cleves helped persuade Henry to marry her.",
         wiki("Hans Holbein the Younger"), difficulty=3)
c.choice("Which artist made a famous print of a rhinoceros in 1515, without ever seeing one?", "Albrecht Dürer", ["Leonardo da Vinci", "Hans Holbein the Younger", "Raphael"],
         "He worked from a written description and a sketch, which is why it seems to wear armour.",
         wiki("Dürer's Rhinoceros"), difficulty=3)
c.choice("Which Italian painter, famous for dramatic light and shadow, was born Michelangelo Merisi?", "Caravaggio", ["Raphael", "Titian", "Tintoretto"],
         "Caravaggio is the name of the town in Lombardy that his family came from.",
         wiki("Caravaggio"), difficulty=3)
c.choice("Which Renaissance artist painted The School of Athens in the Vatican?", "Raphael", ["Michelangelo", "Leonardo da Vinci", "Titian"],
         "He was working on it at the same time Michelangelo was painting the Sistine Chapel ceiling nearby. Raphael died at 37.",
         wiki("The School of Athens"), difficulty=3)
c.choice("Which Flemish painter's name gives us the word for a full, curvy figure?", "Peter Paul Rubens", ["Anthony van Dyck", "Rembrandt", "Titian"],
         "'Rubenesque' comes from him. He also painted the ceiling of the Banqueting House in Whitehall.",
         wiki("Peter Paul Rubens"), difficulty=3)
c.choice("Which French sculptor made the marble lovers called The Kiss?", "Auguste Rodin", ["Antonio Canova", "Henry Moore", "Michelangelo"],
         "Gustav Klimt's golden painting has the same name. One of Rodin's marble versions is at Tate in London.",
         wiki("The Kiss (Rodin sculpture)"), difficulty=2)
c.choice("Which French Impressionist painted ballet dancers again and again?", "Edgar Degas", ["Pierre-Auguste Renoir", "Claude Monet", "Édouard Manet"],
         "He also made a sculpture, Little Dancer Aged Fourteen, dressed in a real tutu.",
         wiki("Edgar Degas"), difficulty=2)
c.choice("Which artist painted Le Déjeuner sur l'herbe, a picnic scene that shocked Paris in 1863?", "Édouard Manet", ["Claude Monet", "Gustave Courbet", "Pierre-Auguste Renoir"],
         "Manet and Monet were friends, and people mixed up their names even then.",
         wiki("Le Déjeuner sur l'herbe"), difficulty=3)
c.choice("Which French artist moved to Tahiti and painted the people and colours of the South Seas?", "Paul Gauguin", ["Paul Cézanne", "Henri Matisse", "Henri de Toulouse-Lautrec"],
         "Before that, he shared a house with Van Gogh in Arles for nine weeks in 1888. It ended in a famous argument.",
         wiki("Paul Gauguin"), difficulty=2)
c.choice("Which artist made famous posters for the Moulin Rouge in Paris?", "Henri de Toulouse-Lautrec", ["Edgar Degas", "Alphonse Mucha", "Paul Gauguin"],
         "He was a regular at the Moulin Rouge, sketching its dancers and singers.",
         wiki("Henri de Toulouse-Lautrec"), difficulty=2)
c.choice("Which Czech artist's Art Nouveau posters show women with long, swirling hair?", "Alphonse Mucha", ["Gustav Klimt", "Egon Schiele", "Henri de Toulouse-Lautrec"],
         "Mucha became famous overnight in 1895 with a poster for the actress Sarah Bernhardt.",
         wiki("Alphonse Mucha"), difficulty=3)
c.choice("Which French painter painted the mountain Mont Sainte-Victoire again and again?", "Paul Cézanne", ["Claude Monet", "Paul Gauguin", "Georges Seurat"],
         "The mountain is near his home town, Aix-en-Provence. He painted it dozens of times.",
         wiki("Mont Sainte-Victoire (Cézanne)"), difficulty=3)
c.choice("Which American artist is famous for giant close-ups of flowers and New Mexico deserts?", "Georgia O'Keeffe", ["Mary Cassatt", "Frida Kahlo", "Tamara de Lempicka"],
         "Her painting Jimson Weed sold for 44.4 million dollars in 2014, then a record for a woman artist.",
         wiki("Georgia O'Keeffe"), difficulty=2)
c.choice("Which Spanish artist from Barcelona painted bright shapes, stars and squiggles?", "Joan Miró", ["Salvador Dalí", "Pablo Picasso", "Antoni Tàpies"],
         "Miró designed the logo for Spain's tourist board, the sun that's still used today.",
         wiki("Joan Miró"), difficulty=3)
c.choice("Which French artist registered his own shade of deep blue?", "Yves Klein", ["Henri Matisse", "Pablo Picasso", "Marc Chagall"],
         "It's called International Klein Blue. Picasso had his own 'Blue Period', but he didn't invent a colour.",
         wiki("International Klein Blue"), difficulty=3)
c.choice("During his 'Blue Period', which artist painted mostly in shades of blue?", "Pablo Picasso", ["Yves Klein", "Joan Miró", "Marc Chagall"],
         "It lasted from about 1901 to 1904, after the death of a close friend. A Rose Period followed.",
         wiki("Picasso's Blue Period"), difficulty=2)

# Architecture and design ---------------------------------------------------------------------------
c.choice("Which Barcelona park did Antoni Gaudí design, with a mosaic dragon at its entrance?", "Park Güell", ["Parc de la Ciutadella", "Montjuïc", "Tibidabo"],
         "It was first planned as a housing estate for wealthy families, but only two houses were ever built.",
         wiki("Park Güell"), difficulty=2)
c.choice("Which architect designed the Shard in London?", "Renzo Piano", ["Norman Foster", "Zaha Hadid", "Richard Rogers"],
         "It's 310 metres tall. Piano also designed the Centre Pompidou in Paris, with Richard Rogers.",
         wiki("The Shard"), difficulty=3)
c.choice("Which London skyscraper is nicknamed the Walkie-Talkie?", "20 Fenchurch Street", ["30 St Mary Axe", "122 Leadenhall Street", "The Shard"],
         "In 2013, its curved glass focused the sun so strongly that it melted parts of a parked car. 30 St Mary Axe is the Gherkin.",
         wiki("20 Fenchurch Street"), era="modern", difficulty=3)
c.choice("Which architect designed the London Aquatics Centre and was the first woman to win the Pritzker Prize?", "Zaha Hadid", ["Norman Foster", "Thomas Heatherwick", "Richard Rogers"],
         "The Pritzker is often called architecture's Nobel Prize. She won it in 2004.",
         wiki("Zaha Hadid"), difficulty=2)
c.choice("Which designer made the London 2012 Olympic cauldron, with a copper petal for every country?", "Thomas Heatherwick", ["Zaha Hadid", "Anish Kapoor", "Norman Foster"],
         "Heatherwick also designed the New Routemaster bus. Anish Kapoor made the red ArcelorMittal Orbit tower in the Olympic Park.",
         wiki("Thomas Heatherwick"), difficulty=3)
c.choice("Which architect designed the Sydney Opera House?", "Jørn Utzon", ["Frank Gehry", "Le Corbusier", "Oscar Niemeyer"],
         "Utzon, from Denmark, left the project in 1966 after rows over money, and never saw it finished.",
         wiki("Jørn Utzon"), difficulty=3)

# Ways of making art -------------------------------------------------------------------------------
c.choice("What do you call a painting done on wet plaster?", "A fresco", ["A mosaic", "A collage", "An etching"],
         "Michelangelo's Sistine Chapel ceiling is a fresco. The paint becomes part of the wall as the plaster dries.",
         wiki("Fresco"), difficulty=2)
c.choice("What is a triptych?", "A picture in three panels", ["A picture in two panels", "A carving in stone", "A stained-glass window"],
         "Two panels make a diptych. Many old altarpieces are triptychs, with side panels that fold over the middle.",
         wiki("Triptych"), difficulty=3)
c.choice("Which old kind of paint is made with egg yolk?", "Tempera", ["Oil paint", "Gouache", "Pastel"],
         "Botticelli's Birth of Venus is painted in tempera. Oil paint took over in the 1400s and 1500s.",
         wiki("Tempera"), difficulty=3)
c.choice("What is the Japanese art of arranging flowers called?", "Ikebana", ["Bonsai", "Kintsugi", "Origami"],
         "Bonsai is growing miniature trees, and origami is paper folding.",
         wiki("Ikebana"), difficulty=2)
c.choice("What is the Japanese art of mending broken pottery with gold called?", "Kintsugi", ["Ikebana", "Raku", "Shibori"],
         "Instead of hiding the cracks, it makes them shine, as part of the object's story.",
         wiki("Kintsugi"), difficulty=2)

# Books and writers ---------------------------------------------------------------------------------
c.choice("Who wrote and drew The Tiger Who Came to Tea?", "Judith Kerr", ["Julia Donaldson", "Shirley Hughes", "Quentin Blake"],
         "It came out in 1968. Kerr also created Mog, the forgetful cat, in 17 books.",
         wiki("Judith Kerr"), difficulty=2)
c.choice("Which Brontë sister wrote Wuthering Heights?", "Emily", ["Charlotte", "Anne", "Branwell"],
         "Charlotte wrote Jane Eyre and Anne wrote The Tenant of Wildfell Hall. Branwell was their brother.",
         wiki("Wuthering Heights"), difficulty=2)
c.choice("Who wrote Treasure Island and Strange Case of Dr Jekyll and Mr Hyde?", "Robert Louis Stevenson", ["Walter Scott", "Arthur Conan Doyle", "Charles Dickens"],
         "Stevenson was from Edinburgh. Treasure Island began as a map he drew with his stepson.",
         wiki("Robert Louis Stevenson"), difficulty=2)
c.choice("Which author created the Famous Five and Noddy?", "Enid Blyton", ["Roald Dahl", "Beatrix Potter", "Anne Fine"],
         "She wrote more than 700 books, sometimes 10,000 words in a day.",
         wiki("Enid Blyton"), era="classic", difficulty=1)
c.choice("Who wrote and drew The Tale of Peter Rabbit?", "Beatrix Potter", ["A. A. Milne", "Enid Blyton", "Kenneth Grahame"],
         "Potter left her farms and over 4,000 acres of the Lake District to the National Trust.",
         wiki("Beatrix Potter"), difficulty=1)
c.choice("Who wrote the Discworld novels?", "Terry Pratchett", ["Douglas Adams", "Neil Gaiman", "Philip Pullman"],
         "There are 41 Discworld novels. The world is a flat disc carried on the backs of four elephants, standing on a giant turtle.",
         wiki("Discworld"), difficulty=2)
c.choice("Who wrote War Horse, which became a stage hit with life-size puppet horses?", "Michael Morpurgo", ["Roald Dahl", "Philip Pullman", "Anthony Horowitz"],
         "The National Theatre's horse puppets are worked by three people each, one for the head and two inside the body.",
         wiki("War Horse (novel)"), difficulty=2)
c.choice("In The Hitchhiker's Guide to the Galaxy, what is the answer to life, the universe and everything?", "42", ["7", "0", "100"],
         "Douglas Adams said he simply picked an ordinary, smallish number. The trouble is, nobody knows what the question was.",
         wiki("Phrases from The Hitchhiker's Guide to the Galaxy"), difficulty=2)
c.choice("Lewis Carroll wrote Alice's Adventures in Wonderland. What was his day job?", "Maths lecturer at Oxford", ["Doctor in London", "Vicar in Yorkshire", "Teacher in Scotland"],
         "His real name was Charles Dodgson, and he also wrote books on logic and maths.",
         wiki("Lewis Carroll"), difficulty=3)
c.choice("Who wrote Frankenstein?", "Mary Shelley", ["Bram Stoker", "Percy Shelley", "Emily Brontë"],
         "She started it at 18, during a ghost story contest with friends by Lake Geneva in 1816. Percy Shelley was her husband.",
         wiki("Frankenstein"), difficulty=1)
c.choice("Which Yorkshire seaside town helped inspire Bram Stoker's Dracula?", "Whitby", ["Scarborough", "Bridlington", "Filey"],
         "In the book, Dracula comes ashore at Whitby in the shape of a large dog.",
         wiki("Whitby"), difficulty=2)
c.choice("How many Harry Potter books are there?", "7", ["8", "6", "9"],
         "There are eight films, because the last book was split into two.",
         wiki("Harry Potter"), difficulty=1)
c.choice("Which author wrote the His Dark Materials books, starting with Northern Lights?", "Philip Pullman", ["C. S. Lewis", "J. K. Rowling", "Terry Pratchett"],
         "In the books, every person has a daemon, an animal companion that is part of their soul.",
         wiki("His Dark Materials"), difficulty=3)
c.choice("Which of Agatha Christie's detectives is Belgian?", "Hercule Poirot", ["Miss Marple", "Inspector Maigret", "Inspector Clouseau"],
         "Maigret is French, created by a Belgian writer, Georges Simenon. Clouseau is the bungling detective of The Pink Panther.",
         wiki("Hercule Poirot"), difficulty=2)
c.choice("Which Agatha Christie play has been on in London since 1952?", "The Mousetrap", ["Murder on the Orient Express", "And Then There Were None", "Death on the Nile"],
         "It's the longest-running play in the world. At the end, the audience is asked to keep the ending a secret.",
         wiki("The Mousetrap"), difficulty=1, as_of="2026")
c.choice("Which children's book stars Mr Toad, Ratty, Mole and Badger?", "The Wind in the Willows", ["Watership Down", "The Borrowers", "Brambly Hedge"],
         "Kenneth Grahame wrote it in 1908, from bedtime stories he told his son.",
         wiki("The Wind in the Willows"), difficulty=1)
c.choice("Which Shakespeare play do actors often call 'the Scottish play', to avoid bad luck?", "Macbeth", ["Hamlet", "King Lear", "Othello"],
         "Theatre folk believe saying 'Macbeth' inside a theatre brings disaster.",
         wiki("The Scottish Play"), difficulty=2)
c.choice("Roughly how many plays did Shakespeare write?", "About 38", ["About 12", "About 60", "About 100"],
         "He also wrote 154 sonnets. A few plays were written with other writers.",
         wiki("Shakespeare's plays"), difficulty=2)
c.choice("Which London theatre is a rebuilt copy of Shakespeare's open-air playhouse?", "Shakespeare's Globe", ["The Old Vic", "The Rose", "The National Theatre"],
         "It opened in 1997. It was the first building with a thatched roof allowed in London since the Great Fire of 1666.",
         wiki("Shakespeare's Globe"), difficulty=2)
c.choice("Which Russian writer wrote War and Peace?", "Leo Tolstoy", ["Fyodor Dostoevsky", "Anton Chekhov", "Alexander Pushkin"],
         "It's around 1,200 pages long in most English editions.",
         wiki("War and Peace"), difficulty=2)
c.choice("Which Spanish novel has a knight who charges at windmills, thinking they're giants?", "Don Quixote", ["El Cid", "Lazarillo de Tormes", "The Three Musketeers"],
         "Miguel de Cervantes wrote it. He died in April 1616, within days of Shakespeare.",
         wiki("Don Quixote"), difficulty=2)
c.choice("Which Colombian writer wrote One Hundred Years of Solitude?", "Gabriel García Márquez", ["Isabel Allende", "Pablo Neruda", "Jorge Luis Borges"],
         "He won the Nobel Prize in Literature in 1982. Netflix made the book into a series in 2024.",
         wiki("One Hundred Years of Solitude"), difficulty=3)

# Festivals and dance ------------------------------------------------------------------------------
c.choice("What is Edinburgh's huge August arts festival, where anyone can put on a show, called?", "The Fringe", ["The Hogmanay", "The Tattoo", "The Book Festival"],
         "It's the biggest arts festival in the world. It started in 1947, when eight groups turned up uninvited to the new Edinburgh Festival.",
         wiki("Edinburgh Festival Fringe"), difficulty=2)
c.choice("Which Brazilian city's carnival has samba schools parading through the Sambadrome?", "Rio de Janeiro", ["São Paulo", "Salvador", "Recife"],
         "The Sambadrome was designed by the architect Oscar Niemeyer and opened in 1984.",
         wiki("Rio Carnival"), difficulty=1)
c.choice("Which Italian city's carnival is famous for its masks?", "Venice", ["Rome", "Florence", "Naples"],
         "Masks once let people of every class mix without being recognised.",
         wiki("Carnival of Venice"), difficulty=1)
c.choice("Which dance comes from Argentina?", "The tango", ["Salsa", "Samba", "Flamenco"],
         "It began in Buenos Aires in the late 1800s. Salsa grew from Cuban music, samba is Brazilian and flamenco is Spanish.",
         wiki("Tango"), difficulty=1)
c.choice("Flamenco comes from which part of Spain?", "Andalusia", ["Catalonia", "The Basque Country", "Galicia"],
         "Andalusia is in the south, home to Seville and Granada. Flamenco is on UNESCO's list of world cultural heritage.",
         wiki("Flamenco"), difficulty=3)

# More museums and galleries -------------------------------------------------------------------------
c.choice("Which Paris museum shows Monet's huge Water Lilies in two oval rooms?", "The Musée de l'Orangerie", ["The Musée Marmottan Monet", "The Musée d'Orsay", "The Louvre"],
         "Monet planned the rooms himself. The Marmottan has his Impression, Sunrise, which gave Impressionism its name.",
         wiki("Musée de l'Orangerie"), difficulty=3)
c.choice("Which London gallery, in Somerset House on the Strand, has Manet's A Bar at the Folies-Bergère?", "The Courtauld Gallery", ["The National Gallery", "The Wallace Collection", "Tate Britain"],
         "The Courtauld is small but full of Impressionist masterpieces, including a Van Gogh self-portrait with a bandaged ear.",
         wiki("Courtauld Gallery"), difficulty=3)
c.choice("In which city is the MUNCH museum, home to versions of The Scream?", "Oslo", ["Bergen", "Stockholm", "Copenhagen"],
         "Munch left thousands of his works to the city of Oslo when he died in 1944.",
         wiki("Munch Museum"), difficulty=2)
c.choice("Salvador Dalí's museum, with giant eggs on its roof, is in which Spanish town where he was born?", "Figueres", ["Cadaqués", "Barcelona", "Girona"],
         "It's in an old theatre, and Dalí is buried in a crypt underneath it.",
         wiki("Figueres"), difficulty=3)
c.choice("Which American city's Art Institute has both Nighthawks and American Gothic?", "Chicago", ["New York", "Boston", "Philadelphia"],
         "The two bronze lions outside its front steps are famous in Chicago too.",
         wiki("Art Institute of Chicago"), difficulty=3)
c.choice("Which Scottish city's Riverside Museum of transport was designed by Zaha Hadid?", "Glasgow", ["Edinburgh", "Dundee", "Aberdeen"],
         "It opened in 2011 beside the River Clyde, with a zigzag roof. It was named European Museum of the Year in 2013.",
         wiki("Riverside Museum"), difficulty=3)
c.choice("Scotland's first design museum, opened in 2018, is a branch of which London museum?", "The V&A", ["The Design Museum", "The Science Museum", "The British Museum"],
         "V&A Dundee was designed by the Japanese architect Kengo Kuma, to look like a cliff face.",
         wiki("V&A Dundee"), era="modern", difficulty=2)
c.choice("Which Japanese island is full of art museums, with a giant yellow polka-dot pumpkin by its pier?", "Naoshima", ["Hokkaido", "Okinawa", "Miyajima"],
         "The pumpkin is by Yayoi Kusama. It was swept into the sea by a typhoon in 2021, then rebuilt.",
         wiki("Naoshima"), era="modern", difficulty=3)

# More artists --------------------------------------------------------------------------------------
c.choice("Which Spanish artist painted The Third of May 1808, showing soldiers firing on civilians?", "Francisco Goya", ["Diego Velázquez", "El Greco", "Bartolomé Murillo"],
         "It's in the Prado in Madrid. Goya was court painter to the Spanish kings.",
         wiki("The Third of May 1808"), difficulty=3)
c.choice("The painter El Greco worked in Spain. On which island was he born?", "Crete", ["Cyprus", "Sicily", "Rhodes"],
         "His nickname simply means 'the Greek'. His real name was Doménikos Theotokópoulos.",
         wiki("El Greco"), difficulty=3)
c.choice("Which artist put 100 iron statues of himself on Crosby Beach, near Liverpool?", "Antony Gormley", ["Anish Kapoor", "Henry Moore", "Damien Hirst"],
         "The work is called Another Place. Gormley also made the Angel of the North.",
         wiki("Another Place (sculpture)"), difficulty=2)
c.choice("Which English artist painted Whistlejacket, a life-size rearing horse?", "George Stubbs", ["J. M. W. Turner", "John Constable", "Thomas Gainsborough"],
         "Stubbs studied horses so closely that he dissected them to learn their anatomy. The painting is in the National Gallery.",
         wiki("Whistlejacket"), difficulty=3)
c.choice("Which of Turner's paintings shows an old warship being towed away to be broken up?", "The Fighting Temeraire", ["The Hay Wain", "Rain, Steam and Speed", "The Slave Ship"],
         "It was voted Britain's favourite painting in 2005, and appears on the £20 note with Turner.",
         wiki("The Fighting Temeraire"), difficulty=3)
c.choice("Which Pre-Raphaelite artist painted Ophelia, floating among flowers in a stream?", "John Everett Millais", ["Dante Gabriel Rossetti", "John William Waterhouse", "William Holman Hunt"],
         "The model, Elizabeth Siddal, lay in a bath of water for hours and caught a bad cold. It hangs in Tate Britain.",
         wiki("Ophelia (painting)"), difficulty=3)
c.choice("Which Glasgow designer is famous for tall-backed chairs and the Glasgow School of Art building?", "Charles Rennie Mackintosh", ["William Morris", "Robert Adam", "Alexander 'Greek' Thomson"],
         "His Art Nouveau style, with roses and straight lines, is still copied on jewellery and prints.",
         wiki("Charles Rennie Mackintosh"), difficulty=2)
c.choice("Which designer's flowery wallpapers, like Strawberry Thief, are still sold today?", "William Morris", ["Charles Rennie Mackintosh", "Laura Ashley", "Orla Kiely"],
         "Morris led the Arts and Crafts movement in Victorian England, which valued things made well by hand.",
         wiki("William Morris"), difficulty=2)
