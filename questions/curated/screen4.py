"""More Film & TV: the stars, the directors and the stories behind the films everyone knows.

The wrong answers are chosen to tempt: another famous Tom, the actor who played the same part in a different film,
or the star who was nearly cast. Every cast and year was checked against a second source (see CHECKS.md).
"""

from . import Category, wiki

c = Category("film-tv", prefix="film4")

# The stars ---------------------------------------------------------------------------------------
c.choice("Who played Maverick, the hotshot fighter pilot in Top Gun (1986)?", "Tom Cruise", ["Tom Hanks", "Val Kilmer", "Kurt Russell"],
         "Val Kilmer played his rival, Iceman. Cruise came back as Maverick in Top Gun: Maverick in 2022, 36 years later.",
         wiki("Top Gun"), era="classic", difficulty=1)
c.yes_no("Did Top Gun: Maverick (2022) take more money at cinemas than the original Top Gun?", True,
         "Much more: about 1.5 billion dollars, against about 357 million for the 1986 film. Cruise flew in real fighter jets for it.",
         wiki("Top Gun: Maverick"), era="modern", difficulty=2)
c.choice("In which Mission: Impossible film does Tom Cruise climb the outside of the Burj Khalifa in Dubai?", "Ghost Protocol", ["Fallout", "Rogue Nation", "Dead Reckoning"],
         "Ghost Protocol came out in 2011. Cruise did the climb himself, held on by cables, more than 120 floors up.",
         wiki("Mission: Impossible – Ghost Protocol"), era="modern", difficulty=3)
c.choice("Which of these films did Tom Hanks NOT star in?", "Top Gun", ["Forrest Gump", "Big", "Cast Away"],
         "Top Gun was the other Tom: Tom Cruise. Hanks won Best Actor for Forrest Gump, which took six Oscars in 1995.",
         wiki("Tom Hanks filmography"), difficulty=1)
c.choice("In Cast Away, what does Tom Hanks's stranded character call his volleyball?", "Wilson", ["Spalding", "Mikasa", "Wilfred"],
         "The ball is named after its maker, Wilson. Hanks lost about 25 kilograms to film the island scenes.",
         wiki("Cast Away"), difficulty=2)
c.choice("In Big (1988), a boy wakes up in a grown man's body. What does Tom Hanks dance on in a famous toy shop scene?", "A giant floor piano", ["A trampoline", "A dance mat", "A pinball table"],
         "The scene was filmed in FAO Schwarz, the famous toy shop on Fifth Avenue in New York.",
         wiki("Big (film)"), era="classic", difficulty=2)
c.choice("Who played Maximus in Gladiator (2000)?", "Russell Crowe", ["Mel Gibson", "Gerard Butler", "Hugh Jackman"],
         "Crowe won the Best Actor Oscar for it, and Gladiator won Best Picture.",
         wiki("Gladiator (2000 film)"), difficulty=2)
c.choice("Which actor starred as Lucius in Gladiator II (2024)?", "Paul Mescal", ["Jacob Elordi", "Barry Keoghan", "Josh O'Connor"],
         "Mescal, from Ireland, first became famous in the TV series Normal People. Denzel Washington co-starred.",
         wiki("Gladiator II"), era="modern", difficulty=3)
c.choice("Which actor plays the T-800 cyborg in The Terminator (1984)?", "Arnold Schwarzenegger", ["Sylvester Stallone", "Jean-Claude Van Damme", "Dolph Lundgren"],
         "James Cameron wrote and directed it, years before Titanic and Avatar.",
         wiki("The Terminator"), era="classic", difficulty=1)
c.choice("Who wrote Rocky (1976) and starred as the boxer Rocky Balboa?", "Sylvester Stallone", ["Robert De Niro", "Al Pacino", "Arnold Schwarzenegger"],
         "Stallone refused to sell the script unless he could play the lead. Rocky won the Oscar for Best Picture.",
         wiki("Rocky"), era="classic", difficulty=2)
c.choice("Which actor played the tough San Francisco detective in Dirty Harry (1971)?", "Clint Eastwood", ["Steve McQueen", "Charles Bronson", "John Wayne"],
         "Eastwood played Inspector Harry Callahan in five films, from 1971 to 1988.",
         wiki("Dirty Harry"), era="classic", difficulty=2)
c.choice("Clint Eastwood won his first Oscar for Best Director for which western?", "Unforgiven", ["The Good, the Bad and the Ugly", "A Fistful of Dollars", "Pale Rider"],
         "Unforgiven (1992) also won Best Picture. Eastwood won Best Director again for Million Dollar Baby (2004).",
         wiki("Unforgiven"), era="classic", difficulty=3)
c.choice("Which Italian director made A Fistful of Dollars with Clint Eastwood?", "Sergio Leone", ["Federico Fellini", "Sergio Corbucci", "Bernardo Bertolucci"],
         "It was the first of three 'spaghetti westerns' with Eastwood as the Man with No Name, ending with The Good, the Bad and the Ugly.",
         wiki("A Fistful of Dollars"), era="classic", difficulty=3)
c.higher_lower("Clint Eastwood directed the courtroom film Juror #2, released in 2024. Was he over or under 90 at the time?", True,
               "Over: he was 94. Eastwood was born in San Francisco in May 1930.",
               wiki("Juror No. 2"), labels=("Over 90", "Under 90"), era="modern", difficulty=2)
c.choice("Who plays Red, the prisoner who tells the story of The Shawshank Redemption?", "Morgan Freeman", ["Denzel Washington", "Samuel L. Jackson", "Danny Glover"],
         "The film did poorly in cinemas in 1994, then became one of the most loved films ever through video and TV.",
         wiki("The Shawshank Redemption"), difficulty=2)
c.choice("In Bruce Almighty (2003), who plays God?", "Morgan Freeman", ["Anthony Hopkins", "Michael Caine", "Sean Connery"],
         "Jim Carrey plays Bruce, a TV reporter who is handed God's powers for a while.",
         wiki("Bruce Almighty"), difficulty=2)
c.choice("In Invictus (2009), which actor plays Nelson Mandela?", "Morgan Freeman", ["Idris Elba", "Denzel Washington", "Sidney Poitier"],
         "A tricky one: Idris Elba played Mandela too, in Long Walk to Freedom (2013), and Sidney Poitier did in a 1997 TV film.",
         wiki("Invictus (film)"), difficulty=3)
c.yes_no("Did Morgan Freeman win his Oscar in a film directed by Clint Eastwood?", True,
         "He won Best Supporting Actor for Million Dollar Baby (2004), which Eastwood directed and starred in.",
         wiki("Million Dollar Baby"), difficulty=3)
c.choice("Whose voice narrates the American version of the penguin documentary March of the Penguins?", "Morgan Freeman", ["David Attenborough", "James Earl Jones", "Samuel L. Jackson"],
         "The film won the Oscar for Best Documentary in 2006.",
         wiki("March of the Penguins"), difficulty=3)
c.choice("Which actor played Elvis Presley in Sofia Coppola's film Priscilla (2023)?", "Jacob Elordi", ["Austin Butler", "Timothée Chalamet", "Harry Styles"],
         "A sneaky one: Austin Butler had played Elvis just a year earlier, in Baz Luhrmann's Elvis (2022).",
         wiki("Priscilla (film)"), era="modern", difficulty=2)
c.choice("Which Australian actor plays the creature in Guillermo del Toro's Frankenstein (2025)?", "Jacob Elordi", ["Oscar Isaac", "Chris Hemsworth", "Hugh Jackman"],
         "Oscar Isaac plays his maker, Victor Frankenstein. Elordi first became famous in The Kissing Booth and Euphoria.",
         wiki("Frankenstein (2025 film)"), era="modern", difficulty=3)
c.choice("Which actor, once a rapper called Marky Mark, starred in The Perfect Storm and The Departed?", "Mark Wahlberg", ["Will Smith", "Matt Damon", "Jason Statham"],
         "As Marky Mark and the Funky Bunch, he had an American number one in 1991 with 'Good Vibrations'.",
         wiki("Mark Wahlberg"), difficulty=2)
c.choice("Who played Agent J in Men in Black (1997)?", "Will Smith", ["Eddie Murphy", "Chris Rock", "Wesley Snipes"],
         "Tommy Lee Jones played his partner, Agent K. Smith also sang the film's theme song.",
         wiki("Men in Black (1997 film)"), difficulty=1)
c.choice("Will Smith won the Best Actor Oscar for playing the father of which sports stars?", "Venus and Serena Williams", ["Andy and Jamie Murray", "The Bryan twins", "Lewis and Nicolas Hamilton"],
         "The film is King Richard (2021). Richard Williams coached his daughters from the age of four.",
         wiki("King Richard (film)"), era="modern", difficulty=2)
c.choice("Which film has Leonardo DiCaprio stealing secrets from people's dreams?", "Inception", ["Shutter Island", "Interstellar", "The Matrix"],
         "Christopher Nolan wrote and directed Inception (2010). The spinning top at the end still starts arguments.",
         wiki("Inception"), era="modern", difficulty=1)
c.choice("Who played Rose in Titanic (1997)?", "Kate Winslet", ["Gwyneth Paltrow", "Cate Blanchett", "Helena Bonham Carter"],
         "Titanic won 11 Oscars, equalling the record set by Ben-Hur in 1960.",
         wiki("Titanic (1997 film)"), difficulty=1)
c.higher_lower("Is the film Titanic (1997) more or less than three hours long?", True,
               "More: it runs for about three and a quarter hours. It was the most expensive film ever made at the time.",
               wiki("Titanic (1997 film)"), labels=("More", "Less"), difficulty=2)
c.yes_no("Did The Lord of the Rings: The Return of the King win every Oscar it was nominated for?", True,
         "All 11 of them, in 2004, including Best Picture. That equalled the record of Ben-Hur and Titanic.",
         wiki("The Lord of the Rings: The Return of the King"), era="modern", difficulty=3)
c.higher_lower("The Return of the King runs for 3 hours 21 minutes in cinemas. Is Avengers: Endgame longer or shorter?", False,
               "Shorter: Endgame runs for just over three hours.",
               wiki("Avengers: Endgame"), labels=("Longer", "Shorter"), era="modern", difficulty=3)
c.choice("Who played Gandalf in The Lord of the Rings films?", "Ian McKellen", ["Christopher Lee", "Michael Gambon", "Patrick Stewart"],
         "Christopher Lee played the wizard Saruman. McKellen also played Magneto in the X-Men films.",
         wiki("Ian McKellen"), difficulty=2)
c.choice("Which actor played Professor X in the X-Men films and Captain Picard in Star Trek?", "Patrick Stewart", ["Ian McKellen", "James McAvoy", "William Shatner"],
         "James McAvoy played the younger Professor X. Stewart is from Mirfield in Yorkshire.",
         wiki("Patrick Stewart"), difficulty=2)
c.choice("Who played Captain Kirk in the original Star Trek TV series?", "William Shatner", ["Leonard Nimoy", "Chris Pine", "Patrick Stewart"],
         "In 2021, aged 90, Shatner flew into space for real, on a Blue Origin rocket.",
         wiki("William Shatner"), era="classic", difficulty=2)
c.choice("Who played Dr Alan Grant in Jurassic Park (1993)?", "Sam Neill", ["Jeff Goldblum", "Harrison Ford", "Richard Attenborough"],
         "Jeff Goldblum played Ian Malcolm. Jurassic Park became the highest-earning film ever at the time.",
         wiki("Jurassic Park (film)"), difficulty=3)
c.yes_no("Was John Hammond, who builds Jurassic Park, played by Sir David Attenborough's brother?", True,
         "Richard Attenborough played him. Richard was also a director, and won Best Director for Gandhi (1982).",
         wiki("Richard Attenborough"), difficulty=2)
c.choice("Which actor played both Han Solo and Indiana Jones?", "Harrison Ford", ["Tom Selleck", "Mark Hamill", "Kurt Russell"],
         "Tom Selleck was first offered Indiana Jones, but couldn't get out of his TV series Magnum, P.I.",
         wiki("Harrison Ford"), difficulty=1)
c.choice("Whose deep voice is Darth Vader's in the original Star Wars films?", "James Earl Jones", ["David Prowse", "Christopher Lee", "Alec Guinness"],
         "David Prowse, a bodybuilder from Bristol, wore the suit. Jones's voice was added afterwards.",
         wiki("James Earl Jones"), difficulty=3)
c.choice("Which British actor played Obi-Wan Kenobi in the first Star Wars film, in 1977?", "Alec Guinness", ["Ewan McGregor", "Peter Cushing", "Christopher Lee"],
         "Ewan McGregor played the younger Obi-Wan in the prequels. Peter Cushing was in the 1977 film too, as Grand Moff Tarkin.",
         wiki("Alec Guinness"), era="classic", difficulty=2)
c.choice("Who played Marty McFly in Back to the Future (1985)?", "Michael J. Fox", ["Eric Stoltz", "Matthew Broderick", "Tom Cruise"],
         "Eric Stoltz was cast first and filmed for about five weeks before he was replaced by Fox.",
         wiki("Back to the Future"), era="classic", difficulty=1)
c.choice("Who played Peter Venkman in Ghostbusters (1984)?", "Bill Murray", ["Dan Aykroyd", "Chevy Chase", "Eddie Murphy"],
         "Dan Aykroyd and Harold Ramis wrote the film and played the other two scientists, Ray and Egon.",
         wiki("Ghostbusters (1984 film)"), era="classic", difficulty=2)
c.choice("Who played John McClane in Die Hard (1988)?", "Bruce Willis", ["Mel Gibson", "Kurt Russell", "Harrison Ford"],
         "Alan Rickman played the villain, Hans Gruber, in his first film role.",
         wiki("Die Hard"), era="classic", difficulty=1)
c.yes_no("Is Die Hard set at Christmas?", True,
         "It all happens at an office Christmas party on Christmas Eve, which is why people argue every year about whether it's a Christmas film.",
         wiki("Die Hard"), difficulty=2)
c.choice("In The Matrix (1999), which colour pill does Neo take?", "Red", ["Blue", "Green", "White"],
         "Morpheus, played by Laurence Fishburne, offers him the choice. The red pill shows him the truth.",
         wiki("The Matrix"), difficulty=1)
c.choice("Who played Don Vito Corleone in The Godfather (1972)?", "Marlon Brando", ["Al Pacino", "Robert De Niro", "James Caan"],
         "Robert De Niro played the young Vito in The Godfather Part II. Both won Oscars for playing the same man.",
         wiki("The Godfather"), era="classic", difficulty=2)
c.yes_no("Have two different actors won Oscars for playing the Joker?", True,
         "Heath Ledger won for The Dark Knight (2008), awarded after his death, and Joaquin Phoenix won for Joker (2019).",
         wiki("Joker (2019 film)"), era="modern", difficulty=2)
c.choice("Who played the Joker in Tim Burton's Batman (1989)?", "Jack Nicholson", ["Heath Ledger", "Joaquin Phoenix", "Mark Hamill"],
         "Nicholson took a share of the film's takings and toy sales instead of a normal fee, and earned a fortune. Mark Hamill voiced the Joker in cartoons.",
         wiki("Batman (1989 film)"), era="classic", difficulty=2)
c.choice("Which actor has played both Batman and Beetlejuice?", "Michael Keaton", ["Jack Nicholson", "Danny DeVito", "Jim Carrey"],
         "Keaton was Batman in 1989 and 1992, and Beetlejuice in 1988 and again in Beetlejuice Beetlejuice in 2024.",
         wiki("Michael Keaton"), difficulty=2)
c.choice("Who played Batman in The Batman (2022)?", "Robert Pattinson", ["Christian Bale", "Ben Affleck", "Michael Keaton"],
         "Pattinson, from London, first became famous as the vampire Edward Cullen in the Twilight films.",
         wiki("The Batman (film)"), era="modern", difficulty=2)
c.yes_no("Was Christian Bale, Batman in The Dark Knight, born in Wales?", True,
         "He was born in Haverfordwest, Pembrokeshire, in 1974. His first big role was as a boy in Spielberg's Empire of the Sun.",
         wiki("Christian Bale"), difficulty=3)
c.choice("Who played Alfred, Batman's butler, in Christopher Nolan's Batman films?", "Michael Caine", ["Gary Oldman", "Morgan Freeman", "Anthony Hopkins"],
         "A tricky one, because the others are in the same films: Gary Oldman is Commissioner Gordon and Morgan Freeman is Lucius Fox.",
         wiki("The Dark Knight trilogy"), era="modern", difficulty=2)
c.choice("Who played Superman in the 1978 film?", "Christopher Reeve", ["Henry Cavill", "Brandon Routh", "Dean Cain"],
         "Henry Cavill played him from 2013, and David Corenswet took over in Superman (2025).",
         wiki("Superman (1978 film)"), era="classic", difficulty=2)
c.choice("Which of these actors has NOT played Spider-Man in a film?", "Tom Hiddleston", ["Tom Holland", "Andrew Garfield", "Tobey Maguire"],
         "Hiddleston plays Loki. The three Spider-Men all appeared together in Spider-Man: No Way Home (2021).",
         wiki("Spider-Man: No Way Home"), era="modern", difficulty=1)
c.choice("Who played Tony Stark, Iron Man, in the Marvel films?", "Robert Downey Jr.", ["Chris Evans", "Chris Hemsworth", "Mark Ruffalo"],
         "Downey won his first Oscar in 2024, as Best Supporting Actor for Oppenheimer.",
         wiki("Robert Downey Jr."), era="modern", difficulty=1)
c.choice("Who plays Nick Fury in the Marvel films?", "Samuel L. Jackson", ["Laurence Fishburne", "Idris Elba", "Don Cheadle"],
         "He first appeared as Fury in a short scene after the credits of Iron Man (2008).",
         wiki("Nick Fury (Marvel Cinematic Universe)"), era="modern", difficulty=2)
c.choice("Which actress plays MJ in Tom Holland's Spider-Man films and Chani in Dune?", "Zendaya", ["Florence Pugh", "Anya Taylor-Joy", "Jenna Ortega"],
         "She began on the Disney Channel and has won two Emmys for the series Euphoria.",
         wiki("Zendaya"), era="modern", difficulty=2)
c.choice("Who played Ken in Barbie (2023)?", "Ryan Gosling", ["Ryan Reynolds", "Chris Pine", "Zac Efron"],
         "Margot Robbie played Barbie, and Gosling's song 'I'm Just Ken' was nominated for an Oscar.",
         wiki("Barbie (film)"), era="modern", difficulty=1)
c.higher_lower("Barbie and Oppenheimer opened on the same day in 2023. Did Barbie take more or less money at cinemas?", True,
               "More: about 1.4 billion dollars to Oppenheimer's 975 million. Fans who saw both called it 'Barbenheimer'.",
               wiki("Barbenheimer"), labels=("More", "Less"), era="modern", difficulty=2)
c.choice("Which Deadpool actor bought Wrexham football club with Rob McElhenney?", "Ryan Reynolds", ["Ryan Gosling", "Hugh Jackman", "Will Ferrell"],
         "They took over the Welsh club in 2021. The series Welcome to Wrexham follows their story.",
         wiki("Ryan Reynolds"), era="modern", difficulty=1)
c.choice("Which actor played Wolverine and the showman P. T. Barnum in The Greatest Showman?", "Hugh Jackman", ["Russell Crowe", "Chris Hemsworth", "Ryan Reynolds"],
         "Jackman, from Sydney, first played Wolverine in X-Men (2000).",
         wiki("Hugh Jackman"), difficulty=2)
c.choice("Which Irish actor played Tommy Shelby in Peaky Blinders and won an Oscar for Oppenheimer?", "Cillian Murphy", ["Tom Hardy", "Colin Farrell", "Paul Mescal"],
         "Tom Hardy was in Peaky Blinders too, as the gangster Alfie Solomons. The series is set in Birmingham.",
         wiki("Cillian Murphy"), era="modern", difficulty=2)
c.choice("Which actor played Bob Dylan in A Complete Unknown (2024)?", "Timothée Chalamet", ["Jacob Elordi", "Austin Butler", "Andrew Garfield"],
         "Chalamet did his own singing and guitar playing, and was nominated for Best Actor.",
         wiki("A Complete Unknown"), era="modern", difficulty=2)
c.choice("Who played Holly Golightly in Breakfast at Tiffany's (1961)?", "Audrey Hepburn", ["Katharine Hepburn", "Grace Kelly", "Marilyn Monroe"],
         "Same surname, no relation: Katharine Hepburn was a different star. Audrey's little black dress was designed by Givenchy.",
         wiki("Breakfast at Tiffany's (film)"), era="classic", difficulty=2)
c.choice("Whose white dress blows up over a subway grate in The Seven Year Itch (1955)?", "Marilyn Monroe", ["Audrey Hepburn", "Grace Kelly", "Elizabeth Taylor"],
         "It's one of the most famous images in film history. The dress sold at auction in 2011 for over 4 million dollars.",
         wiki("The Seven Year Itch"), era="classic", difficulty=2)
c.choice("Which Hollywood star became Princess of Monaco in 1956?", "Grace Kelly", ["Audrey Hepburn", "Rita Hayworth", "Ava Gardner"],
         "She married Prince Rainier III and gave up acting. She starred in three Hitchcock films, including Rear Window.",
         wiki("Grace Kelly"), era="classic", difficulty=2)
c.choice("Who starred opposite Ingrid Bergman in Casablanca (1942)?", "Humphrey Bogart", ["Cary Grant", "Clark Gable", "James Stewart"],
         "Nobody in the film actually says 'Play it again, Sam'. It's one of the most famous misquotes in cinema.",
         wiki("Casablanca (film)"), era="classic", difficulty=2)
c.choice("Which British actress played Scarlett O'Hara in Gone with the Wind (1939)?", "Vivien Leigh", ["Olivia de Havilland", "Bette Davis", "Katharine Hepburn"],
         "Olivia de Havilland was in it too, as Melanie. Hattie McDaniel became the first Black actor to win an Oscar for her role in it.",
         wiki("Gone with the Wind (film)"), era="classic", difficulty=3)
c.choice("Who played Dorothy in The Wizard of Oz (1939)?", "Judy Garland", ["Shirley Temple", "Liza Minnelli", "Julie Andrews"],
         "Garland was 16 when filming began. Liza Minnelli is her daughter.",
         wiki("Judy Garland"), era="classic", difficulty=1)
c.choice("What is the name of Dorothy's little dog in The Wizard of Oz?", "Toto", ["Lassie", "Benji", "Rin Tin Tin"],
         "Toto was played by a female Cairn Terrier called Terry.",
         wiki("Toto (Oz)"), difficulty=1)
c.choice("Who played Captain von Trapp in The Sound of Music (1965)?", "Christopher Plummer", ["Rex Harrison", "Gregory Peck", "Richard Burton"],
         "Plummer was Canadian. Many years later, at 82, he won an Oscar for Beginners.",
         wiki("The Sound of Music (film)"), era="classic", difficulty=3)
c.choice("Who dances and splashes through puddles in Singin' in the Rain (1952)?", "Gene Kelly", ["Fred Astaire", "Frank Sinatra", "Dick Van Dyke"],
         "Debbie Reynolds co-starred. She was later the mother of Carrie Fisher, Princess Leia in Star Wars.",
         wiki("Singin' in the Rain"), era="classic", difficulty=2)
c.choice("Who played Sandy in Grease (1978)?", "Olivia Newton-John", ["Stockard Channing", "Olivia Hussey", "Farrah Fawcett"],
         "Stockard Channing played Rizzo. Newton-John was born in Cambridge, England, and grew up in Australia.",
         wiki("Grease (film)"), era="classic", difficulty=1)
c.yes_no("Did John Travolta star in both Grease and Pulp Fiction?", True,
         "He played Danny in Grease (1978) and Vincent Vega in Pulp Fiction (1994), and danced in both.",
         wiki("John Travolta"), difficulty=1)
c.choice("Who played the dance teacher Johnny Castle in Dirty Dancing (1987)?", "Patrick Swayze", ["Kevin Bacon", "Tom Cruise", "Rob Lowe"],
         "Swayze also sang 'She's Like the Wind' on the film's soundtrack. Kevin Bacon had danced his way through Footloose three years earlier.",
         wiki("Dirty Dancing"), era="classic", difficulty=2)
c.choice("Which actor gives his name to a game where you link any actor to him in six steps?", "Kevin Bacon", ["Tom Hanks", "Christopher Walken", "Samuel L. Jackson"],
         "It's called Six Degrees of Kevin Bacon. He later set up a charity called SixDegrees.org.",
         wiki("Six Degrees of Kevin Bacon"), difficulty=2)
c.choice("Which actor dressed up as a Scottish nanny in Mrs. Doubtfire (1993)?", "Robin Williams", ["Dustin Hoffman", "Steve Martin", "Billy Crystal"],
         "Dustin Hoffman had dressed as a woman for a role too, in Tootsie (1982).",
         wiki("Mrs. Doubtfire"), difficulty=1)
c.choice("Who played Bert, the chimney sweep in Mary Poppins (1964), with a famously wobbly cockney accent?", "Dick Van Dyke", ["Gene Kelly", "Danny Kaye", "Bing Crosby"],
         "He came back for Mary Poppins Returns (2018), in his 90s, and danced on a desk.",
         wiki("Dick Van Dyke"), era="classic", difficulty=2)
c.choice("Who played Ellen Ripley in Alien (1979)?", "Sigourney Weaver", ["Linda Hamilton", "Jamie Lee Curtis", "Carrie Fisher"],
         "Linda Hamilton played another famous action heroine, Sarah Connor, in The Terminator.",
         wiki("Alien (film)"), era="classic", difficulty=2)
c.choice("Who played the blacksmith Will Turner in Pirates of the Caribbean?", "Orlando Bloom", ["Jude Law", "Hugh Jackman", "Ewan McGregor"],
         "Bloom had played Legolas in The Lord of the Rings just before. Johnny Depp was nominated for an Oscar as Captain Jack Sparrow.",
         wiki("Pirates of the Caribbean: The Curse of the Black Pearl"), era="modern", difficulty=2)
c.choice("Which actress played Jules in Bend It Like Beckham (2002), a year before Pirates of the Caribbean?", "Keira Knightley", ["Emma Watson", "Kate Winslet", "Carey Mulligan"],
         "Parminder Nagra played Jess, a girl from Hounslow who dreams of playing football like David Beckham.",
         wiki("Bend It Like Beckham"), era="modern", difficulty=3)
c.choice("Who played Hugh Grant's love interest, a famous film star, in Notting Hill (1999)?", "Julia Roberts", ["Sandra Bullock", "Meg Ryan", "Gwyneth Paltrow"],
         "Grant plays the owner of a little travel bookshop in Notting Hill, west London.",
         wiki("Notting Hill (film)"), difficulty=2)
c.choice("Julia Roberts won the Oscar for Best Actress for which film?", "Erin Brockovich", ["Pretty Woman", "Notting Hill", "Steel Magnolias"],
         "She won in 2001, playing a real woman who took on a giant power company. Pretty Woman only got her a nomination.",
         wiki("Erin Brockovich (film)"), difficulty=3)
c.choice("In Love Actually, who plays the Prime Minister who dances around Downing Street?", "Hugh Grant", ["Colin Firth", "Alan Rickman", "Bill Nighy"],
         "Bill Nighy steals the film as Billy Mack, an ageing rock star with a cheesy Christmas single.",
         wiki("Love Actually"), difficulty=2)
c.choice("Who has more Oscar nominations than any other actor?", "Meryl Streep", ["Katharine Hepburn", "Jack Nicholson", "Denzel Washington"],
         "Streep has 21 nominations and three wins. Katharine Hepburn holds the record for wins, with four.",
         wiki("Meryl Streep"), difficulty=2, as_of="2026")
c.choice("In which film does Meryl Streep play a terrifying fashion magazine editor?", "The Devil Wears Prada", ["Mamma Mia!", "The Iron Lady", "Julie & Julia"],
         "Anne Hathaway plays her new assistant. The editor, Miranda Priestly, is said to be based on Vogue's Anna Wintour.",
         wiki("The Devil Wears Prada (film)"), era="modern", difficulty=1)
c.choice("Which actress played M, James Bond's boss, from GoldenEye to Skyfall?", "Judi Dench", ["Helen Mirren", "Maggie Smith", "Julie Walters"],
         "She was the first woman to play M. She also won an Oscar for about eight minutes on screen as Elizabeth I in Shakespeare in Love.",
         wiki("Judi Dench"), difficulty=2)
c.choice("Which actress played Professor McGonagall in Harry Potter and the Dowager Countess in Downton Abbey?", "Maggie Smith", ["Judi Dench", "Helen Mirren", "Julie Walters"],
         "Julie Walters was in Harry Potter too, as Mrs Weasley.",
         wiki("Maggie Smith"), difficulty=2)
c.choice("Who played Severus Snape in the Harry Potter films?", "Alan Rickman", ["Gary Oldman", "Ralph Fiennes", "Jason Isaacs"],
         "All four were in the films: Oldman was Sirius Black, Fiennes was Voldemort and Isaacs was Lucius Malfoy.",
         wiki("Alan Rickman"), difficulty=2)
c.choice("In the series Wednesday, what is the name of the helpful hand with no body?", "Thing", ["Lurch", "Fingers", "Hand"],
         "Thing is played by a magician, Victor Dorobantu, whose arm is filmed and the rest of him edited out. Lurch is the family's butler.",
         wiki("Wednesday (TV series)"), era="modern", difficulty=1)
c.yes_no("Was Millie Bobby Brown, Eleven in Stranger Things, born in Spain?", True,
         "She was born in Marbella in 2004, to British parents, and grew up partly in Bournemouth.",
         wiki("Millie Bobby Brown"), era="modern", difficulty=3)
c.choice("Who became the oldest Best Actor winner, aged 83, for The Father (2020)?", "Anthony Hopkins", ["Michael Caine", "Ian McKellen", "Christopher Plummer"],
         "Hopkins, from Port Talbot in Wales, had won Best Actor 29 years earlier for The Silence of the Lambs.",
         wiki("Anthony Hopkins"), difficulty=3)
c.choice("Who was the first Black actor to win the Oscar for Best Actor, in 1964?", "Sidney Poitier", ["Denzel Washington", "Harry Belafonte", "James Earl Jones"],
         "He won for Lilies of the Field. Denzel Washington became the second, nearly 40 years later.",
         wiki("Sidney Poitier"), era="classic", difficulty=2)
c.choice("Denzel Washington won the Oscar for Best Actor for which film?", "Training Day", ["Malcolm X", "Philadelphia", "The Equalizer"],
         "He won in 2002. He'd already won Best Supporting Actor for Glory (1989).",
         wiki("Denzel Washington"), difficulty=3)
c.choice("Which Bond star became the first Black woman to win the Oscar for Best Actress?", "Halle Berry", ["Whitney Houston", "Viola Davis", "Angela Bassett"],
         "She won in 2002 for Monster's Ball, then played Jinx in Die Another Day that same year.",
         wiki("Halle Berry"), difficulty=3)
c.choice("Who played the martial arts hero of Enter the Dragon (1973)?", "Bruce Lee", ["Jackie Chan", "Chuck Norris", "Jet Li"],
         "A teenage Jackie Chan is in it too, as a stuntman fighting Bruce Lee.",
         wiki("Enter the Dragon"), era="classic", difficulty=2)
c.choice("Which silent film star was famous as 'The Tramp', with a bowler hat and a cane?", "Charlie Chaplin", ["Buster Keaton", "Stan Laurel", "Harold Lloyd"],
         "Chaplin was born in London in 1889. Stan Laurel was English too, and travelled to America with him.",
         wiki("Charlie Chaplin"), era="classic", difficulty=1)
c.choice("Who played Queen Elizabeth II in the first two series of The Crown?", "Claire Foy", ["Olivia Colman", "Imelda Staunton", "Helen Mirren"],
         "Olivia Colman took over for series three and four, and Imelda Staunton for the last two. Helen Mirren played her in the film The Queen (2006).",
         wiki("The Crown (TV series)"), era="modern", difficulty=2)

# Directors and the people behind the camera -------------------------------------------------------
c.choice("Which director made Psycho, The Birds and Vertigo?", "Alfred Hitchcock", ["Stanley Kubrick", "Orson Welles", "Billy Wilder"],
         "Hitchcock was born in Leytonstone, London. He never won a competitive Oscar for directing.",
         wiki("Alfred Hitchcock"), era="classic", difficulty=1)
c.choice("Which director made Alien, Blade Runner and Gladiator?", "Ridley Scott", ["James Cameron", "Tony Scott", "Denis Villeneuve"],
         "His younger brother Tony directed Top Gun. James Cameron made the sequel Aliens, and Villeneuve made Blade Runner 2049.",
         wiki("Ridley Scott"), difficulty=2)
c.choice("Who directed Edward Scissorhands and Beetlejuice?", "Tim Burton", ["Sam Raimi", "Guillermo del Toro", "Henry Selick"],
         "He also directed Batman (1989). The Nightmare Before Christmas was his idea, but Henry Selick directed it.",
         wiki("Tim Burton"), difficulty=2)
c.choice("Who directed The Lord of the Rings trilogy?", "Peter Jackson", ["Guillermo del Toro", "Taika Waititi", "Sam Raimi"],
         "He filmed all three at the same time in New Zealand, over more than a year.",
         wiki("Peter Jackson"), difficulty=2)
c.choice("Greta Gerwig directed Barbie. Which film about four sisters did she make before it?", "Little Women", ["Pride and Prejudice", "Sense and Sensibility", "Mamma Mia!"],
         "Her Little Women came out in 2019, with Saoirse Ronan and Florence Pugh. Barbie made her the first woman to direct a billion-dollar film on her own.",
         wiki("Little Women (2019 film)"), era="modern", difficulty=2)
c.choice("Who was the first woman to win the Oscar for Best Director, in 2010?", "Kathryn Bigelow", ["Jane Campion", "Sofia Coppola", "Greta Gerwig"],
         "She won for The Hurt Locker, beating Avatar, made by her former husband, James Cameron.",
         wiki("Kathryn Bigelow"), difficulty=3)
c.choice("Which director made Pulp Fiction and Kill Bill?", "Quentin Tarantino", ["Martin Scorsese", "Guy Ritchie", "Robert Rodriguez"],
         "Pulp Fiction won the top prize at the Cannes Film Festival, the Palme d'Or, in 1994.",
         wiki("Quentin Tarantino"), difficulty=2)
c.choice("Which British director made Lock, Stock and Two Smoking Barrels and Snatch?", "Guy Ritchie", ["Matthew Vaughn", "Danny Boyle", "Richard Curtis"],
         "Matthew Vaughn produced both films, and later directed Kingsman and Kick-Ass himself.",
         wiki("Guy Ritchie"), difficulty=2)
c.choice("Which director of Slumdog Millionaire also staged the London 2012 Olympics opening ceremony?", "Danny Boyle", ["Sam Mendes", "Ridley Scott", "Christopher Nolan"],
         "The ceremony included a short film of the Queen meeting Daniel Craig's James Bond at Buckingham Palace.",
         wiki("Danny Boyle"), difficulty=2)
c.choice("Who wrote Four Weddings and a Funeral, Notting Hill and Love Actually?", "Richard Curtis", ["Ricky Gervais", "Nick Hornby", "Armando Iannucci"],
         "He also co-wrote Blackadder and Mr. Bean, and co-founded Comic Relief.",
         wiki("Richard Curtis"), difficulty=3)
c.choice("Which director made the space film 2001: A Space Odyssey (1968)?", "Stanley Kubrick", ["Steven Spielberg", "George Lucas", "Ridley Scott"],
         "Kubrick, an American, lived and worked in England for most of his life.",
         wiki("2001: A Space Odyssey"), era="classic", difficulty=2)
c.choice("What is the name of the talking computer in 2001: A Space Odyssey?", "HAL 9000", ["Skynet", "Mother", "KITT"],
         "Skynet is the computer in The Terminator, Mother runs the ship in Alien, and KITT is the talking car in Knight Rider.",
         wiki("HAL 9000"), difficulty=2)
c.choice("Which of these Steven Spielberg films came out first?", "Jaws", ["Raiders of the Lost Ark", "E.T. the Extra-Terrestrial", "Jurassic Park"],
         "Jaws (1975) is often called the first summer blockbuster. Then came Raiders (1981), E.T. (1982) and Jurassic Park (1993).",
         wiki("Steven Spielberg filmography"), difficulty=3)
c.choice("Which composer wrote the music for Jaws, Star Wars and the first Harry Potter films?", "John Williams", ["Hans Zimmer", "John Barry", "Ennio Morricone"],
         "Williams has more than 50 Oscar nominations, more than any other living person.",
         wiki("John Williams"), difficulty=2, as_of="2026")
c.choice("Hans Zimmer won his first Oscar for the music of which film?", "The Lion King", ["Gladiator", "Inception", "Pirates of the Caribbean"],
         "He won for The Lion King (1994) and again, 27 years later, for Dune.",
         wiki("Hans Zimmer"), difficulty=3)
c.choice("Which Italian composer wrote the music for The Good, the Bad and the Ugly?", "Ennio Morricone", ["Nino Rota", "Vangelis", "Giacomo Puccini"],
         "Nino Rota wrote the music for The Godfather. Morricone finally won an Oscar at 87, for The Hateful Eight.",
         wiki("Ennio Morricone"), era="classic", difficulty=3)
c.choice("Which singer won an Oscar for the theme song to the Bond film Skyfall?", "Adele", ["Billie Eilish", "Sam Smith", "Shirley Bassey"],
         "Sam Smith and Billie Eilish won for the next two Bond songs as well: three Oscars in a row.",
         wiki("Skyfall (Adele song)"), era="modern", difficulty=2)

# James Bond ----------------------------------------------------------------------------------------
c.choice("Which actor played James Bond in the most official Bond films?", "Roger Moore", ["Sean Connery", "Daniel Craig", "Pierce Brosnan"],
         "Moore made seven. Connery made six official ones, plus Never Say Never Again (1983), which wasn't made by the usual producers.",
         wiki("James Bond in film"), difficulty=3, as_of="2026")
c.choice("Which actor played Bond in just one film, On Her Majesty's Secret Service (1969)?", "George Lazenby", ["Timothy Dalton", "David Niven", "Roger Moore"],
         "Lazenby was an Australian model with almost no acting experience. Timothy Dalton made two Bond films.",
         wiki("George Lazenby"), era="classic", difficulty=3)
c.higher_lower("Daniel Craig played Bond in five films. Did Pierce Brosnan play him in more or fewer?", False,
               "Fewer: Brosnan made four, from GoldenEye (1995) to Die Another Day (2002).",
               wiki("Pierce Brosnan"), labels=("More", "Fewer"), difficulty=2)
c.choice("Which Bond villain has steel teeth?", "Jaws", ["Oddjob", "Blofeld", "Goldfinger"],
         "Jaws, played by the 2.18-metre Richard Kiel, appeared in The Spy Who Loved Me and Moonraker.",
         wiki("Jaws (James Bond)"), era="classic", difficulty=2)
c.choice("In Goldfinger (1964), what deadly object does Oddjob throw?", "His bowler hat", ["An umbrella", "A boomerang", "A golf club"],
         "The hat has a steel rim. Oddjob was played by Harold Sakata, an Olympic weightlifting silver medallist.",
         wiki("Oddjob"), era="classic", difficulty=2)
c.choice("What is the name of the inventor who gives James Bond his gadgets?", "Q", ["M", "Moneypenny", "Felix"],
         "Q stands for Quartermaster. Desmond Llewelyn played him in 17 films.",
         wiki("Q (James Bond)"), difficulty=1)
c.choice("At which studios near London are the Bond films made, on a stage named after 007?", "Pinewood", ["Leavesden", "Ealing", "Elstree"],
         "The Harry Potter films were made at Leavesden, which is now the Warner Bros. Studio Tour.",
         wiki("Pinewood Studios"), difficulty=3)

# Films from around the world ----------------------------------------------------------------------
c.choice("Which South Korean film became the first not in English to win Best Picture?", "Parasite", ["Oldboy", "Train to Busan", "The Handmaiden"],
         "Bong Joon Ho's film won four Oscars in 2020, including Best Director.",
         wiki("Parasite (2019 film)"), era="modern", difficulty=2)
c.choice("What's the nickname of the Hindi film industry based in Mumbai?", "Bollywood", ["Nollywood", "Tollywood", "Kollywood"],
         "The B comes from Bombay, Mumbai's old name. Nollywood is Nigeria's huge film industry.",
         wiki("Hindi cinema"), difficulty=1)
c.choice("Which Bollywood star is often called the 'King of Bollywood'?", "Shah Rukh Khan", ["Amitabh Bachchan", "Salman Khan", "Aamir Khan"],
         "Amitabh Bachchan has his own nickname: Big B.",
         wiki("Shah Rukh Khan"), difficulty=3)
c.choice("Which Indian film's song 'Naatu Naatu' won an Oscar in 2023?", "RRR", ["Slumdog Millionaire", "Lagaan", "Baahubali"],
         "Slumdog Millionaire's 'Jai Ho' had won the same award in 2009.",
         wiki("RRR"), era="modern", difficulty=3)
c.choice("What's the top prize at the Cannes Film Festival called?", "The Palme d'Or", ["The Golden Lion", "The Golden Bear", "The Golden Globe"],
         "It means Golden Palm. The Golden Lion is Venice's top prize, and the Golden Bear is Berlin's.",
         wiki("Palme d'Or"), difficulty=2)
c.choice("Which award is a gold statuette officially called the Academy Award of Merit?", "The Oscar", ["The Golden Globe", "The BAFTA", "The Emmy"],
         "Nobody is quite sure where the nickname 'Oscar' came from. It has been used since the 1930s.",
         wiki("Academy Awards"), difficulty=2)
c.choice("What does a BAFTA award look like?", "A theatre mask", ["A golden man", "A winged woman holding an atom", "A globe"],
         "The mask was designed in 1955 by the American sculptor Mitzi Cunliffe. The Emmy is the winged woman.",
         wiki("British Academy Film Awards"), difficulty=3)
c.yes_no("Was Rocky (1976), which won Best Picture, filmed in less than a month?", True,
         "It was shot in about 28 days on a small budget, and Stallone used his own dog, Butkus, in the film.",
         wiki("Rocky"), era="classic", difficulty=3)
c.choice("Which 1927 film was the first full-length film with synchronised talking?", "The Jazz Singer", ["Steamboat Willie", "Metropolis", "The Wizard of Oz"],
         "Steamboat Willie, Mickey Mouse's first hit, came the next year, with synchronised sound too.",
         wiki("The Jazz Singer"), era="classic", difficulty=3)
c.choice("In The Italian Job (1969), which cars do the gang use for their getaway?", "Minis", ["Fiat 500s", "Volkswagen Beetles", "Ford Escorts"],
         "Three Minis, in red, white and blue, race through Turin. Michael Caine leads the gang.",
         wiki("The Italian Job"), era="classic", difficulty=2)

# British film and TV -------------------------------------------------------------------------------
c.choice("In which city is The Full Monty (1997) set?", "Sheffield", ["Leeds", "Manchester", "Newcastle"],
         "Out-of-work steelworkers become strippers to earn some money. It later became a stage show and a TV series.",
         wiki("The Full Monty"), difficulty=2)
c.choice("In Billy Elliot, what does the miner's son secretly learn instead of boxing?", "Ballet", ["Tap dancing", "The piano", "Football"],
         "The film came out in 2000. Its stage musical, with music by Elton John, ran in the West End for over ten years.",
         wiki("Billy Elliot"), difficulty=1)
c.choice("Which comedy is set in the Slough office of a paper company?", "The Office", ["The IT Crowd", "Peep Show", "Gavin & Stacey"],
         "Ricky Gervais and Stephen Merchant made it in 2001. The American version starred Steve Carell.",
         wiki("The Office (British TV series)"), difficulty=2)
c.choice("Gavin comes from Essex. Which Welsh town is Stacey from?", "Barry", ["Swansea", "Cardiff", "Newport"],
         "James Corden and Ruth Jones wrote Gavin & Stacey and played Smithy and Nessa.",
         wiki("Gavin & Stacey"), era="modern", difficulty=2)
c.choice("In which seaside town is Fawlty Towers set?", "Torquay", ["Brighton", "Blackpool", "Eastbourne"],
         "John Cleese and Connie Booth wrote it. Only 12 episodes were ever made.",
         wiki("Fawlty Towers"), era="classic", difficulty=2)
c.choice("Which wartime sitcom follows a Home Guard platoon in Walmington-on-Sea?", "Dad's Army", ["'Allo 'Allo!", "Porridge", "It Ain't Half Hot Mum"],
         "It ran from 1968 to 1977 and is still repeated on BBC Two.",
         wiki("Dad's Army"), era="classic", difficulty=2)
c.choice("In which comedy does Rowan Atkinson play Edmund in four different centuries?", "Blackadder", ["Red Dwarf", "Mr. Bean", "The Thick of It"],
         "It moves from the Middle Ages to the First World War, with Tony Robinson as his servant Baldrick.",
         wiki("Blackadder"), era="classic", difficulty=2)
c.choice("Which pub is at the heart of EastEnders?", "The Queen Vic", ["The Rovers Return", "The Woolpack", "The Nag's Head"],
         "The Rovers Return is in Coronation Street, the Woolpack in Emmerdale, and the Nag's Head is Del Boy's local in Only Fools and Horses.",
         wiki("The Queen Victoria"), difficulty=1)
c.choice("Who hosts the UK version of The Traitors?", "Claudia Winkleman", ["Tess Daly", "Holly Willoughby", "Davina McCall"],
         "It's filmed at Ardross Castle in the Scottish Highlands. Tess Daly co-hosted Strictly with Winkleman.",
         wiki("The Traitors (British TV series)"), era="modern", difficulty=1)
c.choice("Who was the first host of Who Wants to Be a Millionaire? in Britain, in 1998?", "Chris Tarrant", ["Jeremy Clarkson", "Des O'Connor", "Bradley Walsh"],
         "Jeremy Clarkson took over when the show came back in 2018.",
         wiki("Who Wants to Be a Millionaire? (British game show)"), difficulty=2)
c.choice("Which quiz show has Bradley Walsh and a team of 'chasers'?", "The Chase", ["Pointless", "Eggheads", "Tipping Point"],
         "The chasers have nicknames such as the Beast, the Governess and the Dark Destroyer.",
         wiki("The Chase (British game show)"), era="modern", difficulty=1)
c.choice("On the TV quiz Pointless, what kind of answer scores best?", "One nobody in the survey thought of", ["The most popular answer", "The longest answer", "The fastest answer"],
         "Each answer scores a point for every person in a survey of 100 who gave it, so zero, a 'pointless' answer, is perfect.",
         wiki("Pointless"), era="modern", difficulty=2)
c.choice("How many seconds do Countdown contestants get to make a word?", "30", ["60", "45", "20"],
         "Countdown was the very first programme shown on Channel 4, in 1982.",
         wiki("Countdown (game show)"), difficulty=2)
c.choice("What are Ant and Dec's first names?", "Anthony and Declan", ["Andrew and Declan", "Anthony and Dexter", "Antonio and Desmond"],
         "Ant McPartlin and Declan Donnelly met as child actors on the BBC series Byker Grove in Newcastle.",
         wiki("Ant & Dec"), difficulty=2)
c.choice("What is the name of Jeremy Clarkson's farm, seen on Clarkson's Farm?", "Diddly Squat", ["Muddy Acres", "Hawkstone", "Top Gear Farm"],
         "It's in Oxfordshire, in the Cotswolds. Hawkstone is the name of his beer.",
         wiki("Clarkson's Farm"), era="modern", difficulty=2)
c.choice("Which real castle plays the house in Downton Abbey?", "Highclere Castle", ["Alnwick Castle", "Blenheim Palace", "Castle Howard"],
         "Highclere is in Hampshire. Alnwick Castle in Northumberland played Hogwarts in the first two Harry Potter films.",
         wiki("Highclere Castle"), difficulty=2)
c.choice("From which London station does the Hogwarts Express leave, on Platform 9 and three-quarters?", "King's Cross", ["Paddington", "Euston", "St Pancras"],
         "There's a luggage trolley disappearing into a wall at the real station, for photos.",
         wiki("King's Cross railway station"), difficulty=1)

# Streaming ------------------------------------------------------------------------------------------
c.choice("In Stranger Things, what do the kids call the dark, dangerous world hidden beneath their town?", "The Upside Down", ["The Shadow Realm", "The Nether", "The Phantom Zone"],
         "The Nether is from Minecraft and the Phantom Zone from Superman. The series ended with its fifth season, at the end of 2025.",
         wiki("Stranger Things"), era="modern", difficulty=2)
c.choice("Which Netflix drama is set in high society in Regency London?", "Bridgerton", ["The Crown", "Downton Abbey", "Peaky Blinders"],
         "It's based on Julia Quinn's novels about the eight Bridgerton brothers and sisters.",
         wiki("Bridgerton"), era="modern", difficulty=1)
c.choice("Which game is the Netflix series The Queen's Gambit about?", "Chess", ["Poker", "Snooker", "Bridge"],
         "Anya Taylor-Joy plays Beth Harmon, an orphan who becomes a chess champion. A 'gambit' is a kind of chess opening.",
         wiki("The Queen's Gambit (miniseries)"), era="modern", difficulty=1)
c.choice("Who plays the scruffy spy boss Jackson Lamb in Slow Horses?", "Gary Oldman", ["Colin Firth", "Jim Broadbent", "Timothy Spall"],
         "Slow Horses, on Apple TV+, is about MI5 agents sent to a dead-end office for messing up.",
         wiki("Slow Horses"), era="modern", difficulty=3)
c.choice("What is the real name of the little green character fans called 'Baby Yoda' in The Mandalorian?", "Grogu", ["Din Djarin", "Yaddle", "Ahsoka"],
         "Din Djarin is the Mandalorian himself, played by Pedro Pascal.",
         wiki("Grogu"), era="modern", difficulty=2)

# Sci-fi and fantasy worlds ------------------------------------------------------------------------
c.choice("On which desert planet is Dune set?", "Arrakis", ["Tatooine", "Jakku", "Pandora"],
         "Tatooine and Jakku are desert planets from Star Wars. Dune is based on Frank Herbert's 1965 novel.",
         wiki("Arrakis"), era="modern", difficulty=2)
c.choice("On which moon is Avatar set?", "Pandora", ["Endor", "Arrakis", "Titan"],
         "Pandora orbits a made-up giant planet. Endor is the forest moon where the Ewoks live in Star Wars.",
         wiki("Avatar (2009 film)"), era="modern", difficulty=2)
