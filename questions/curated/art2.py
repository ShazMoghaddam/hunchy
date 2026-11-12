"""More Art & Culture: artists, paintings, movements and museums."""

from . import Category, wiki

c = Category("art", prefix="art2")

c.choice("Which Russian-born artist is seen as one of the first to paint completely abstract pictures?", "Wassily Kandinsky", ["Marc Chagall", "Kazimir Malevich", "Pablo Picasso"],
         "Kandinsky said he could 'hear' colours, and named many paintings like pieces of music: Compositions and Improvisations.",
         wiki("Wassily Kandinsky"), difficulty=2)
c.yes_no("Did Wassily Kandinsky give some of his paintings names like pieces of music, such as 'Composition VII'?", True,
         "He believed colours and shapes could work like musical notes.",
         wiki("Wassily Kandinsky"), difficulty=3)
c.choice("Which American artist started out spray-painting graffiti in New York under the tag SAMO?", "Jean-Michel Basquiat", ["Keith Haring", "Andy Warhol", "Jackson Pollock"],
         "Basquiat's painting Untitled (1982), a skull, sold for $110.5 million in 2017.",
         wiki("Jean-Michel Basquiat"), era="modern", difficulty=2)
c.choice("Which artist often painted a three-pointed crown in his pictures?", "Jean-Michel Basquiat", ["Roy Lichtenstein", "Banksy", "Damien Hirst"],
         "The crown became Basquiat's signature, a way of honouring the people he admired.",
         wiki("Jean-Michel Basquiat"), era="modern", difficulty=3)
c.choice("Which country was Vincent van Gogh from?", "The Netherlands", ["France", "Belgium", "Germany"],
         "Van Gogh did much of his best-known work in France, where he moved in 1886.",
         wiki("Vincent van Gogh"), difficulty=2)
c.choice("Which flowers did Van Gogh paint in a famous series?", "Sunflowers", ["Tulips", "Roses", "Daisies"],
         "He painted the sunflowers to decorate a room for his friend, the painter Paul Gauguin.",
         wiki("Sunflowers (Van Gogh series)"), difficulty=1)
c.higher_lower("Van Gogh painted for about 10 years. Did he make more or fewer than 500 paintings in that time?", True,
               "He made about 860 oil paintings, most of them in the last two years of his life.",
               wiki("Vincent van Gogh"), labels=("More", "Fewer"), difficulty=3)
c.choice("Which Japanese artist made the famous print The Great Wave off Kanagawa?", "Hokusai", ["Hiroshige", "Yayoi Kusama", "Utamaro"],
         "The print, from around 1831, shows Mount Fuji small in the distance behind the wave.",
         wiki("The Great Wave off Kanagawa"), difficulty=2)
c.choice("Which mountain can you see in the background of The Great Wave off Kanagawa?", "Mount Fuji", ["Mount Everest", "Kilimanjaro", "Mont Blanc"],
         "It was part of a series called Thirty-six Views of Mount Fuji.",
         wiki("The Great Wave off Kanagawa"), difficulty=2)
c.choice("Which Japanese artist is famous for covering rooms and pumpkins in polka dots?", "Yayoi Kusama", ["Hokusai", "Takashi Murakami", "Yoko Ono"],
         "Yayoi Kusama's mirrored Infinity Rooms make the dots seem to go on for ever.",
         wiki("Yayoi Kusama"), era="modern", difficulty=2)
c.choice("Which Austrian painter covered The Kiss in gold leaf?", "Gustav Klimt", ["Egon Schiele", "Oskar Kokoschka", "Edvard Munch"],
         "The Kiss hangs in the Belvedere palace in Vienna.",
         wiki("The Kiss (Klimt)"), difficulty=2)
c.choice("Which Dutch artist painted The Night Watch?", "Rembrandt", ["Johannes Vermeer", "Vincent van Gogh", "Piet Mondrian"],
         "The Night Watch is about 4.5 metres wide. It hangs in the Rijksmuseum in Amsterdam.",
         wiki("The Night Watch"), difficulty=2)
c.choice("Which Dutch artist painted grids of black lines with blocks of red, yellow and blue?", "Piet Mondrian", ["Rembrandt", "Vincent van Gogh", "M. C. Escher"],
         "Mondrian's style has inspired dresses, buildings and even trainers.",
         wiki("Piet Mondrian"), difficulty=2)
c.choice("Which American painter made 'drip paintings' by flicking paint onto canvas on the floor?", "Jackson Pollock", ["Mark Rothko", "Andy Warhol", "Edward Hopper"],
         "People nicknamed him 'Jack the Dripper'.",
         wiki("Jackson Pollock"), era="classic", difficulty=2)
c.choice("Which American painter made Nighthawks, showing people in a late-night diner?", "Edward Hopper", ["Norman Rockwell", "Grant Wood", "Jackson Pollock"],
         "Hopper painted it in 1942. It hangs in the Art Institute of Chicago.",
         wiki("Nighthawks"), era="classic", difficulty=3)
c.choice("Which painting by Grant Wood shows a farmer with a pitchfork beside a woman?", "American Gothic", ["The Gleaners", "Christina's World", "The Haywain"],
         "Wood's sister and his dentist were the models.",
         wiki("American Gothic"), era="classic", difficulty=3)
c.choice("Which British artist is famous for bright paintings of Los Angeles swimming pools?", "David Hockney", ["Francis Bacon", "Lucian Freud", "Damien Hirst"],
         "Hockney's A Bigger Splash was painted in 1967. He was born in Bradford.",
         wiki("David Hockney"), era="classic", difficulty=2)
c.choice("Which artist painted busy northern town scenes with 'matchstick men'?", "L. S. Lowry", ["J. M. W. Turner", "John Constable", "David Hockney"],
         "Lowry painted Salford and Manchester while working as a rent collector.",
         wiki("L. S. Lowry"), era="classic", difficulty=2)
c.choice("Which artist gives his name to Britain's best-known prize for modern art?", "J. M. W. Turner", ["John Constable", "Thomas Gainsborough", "William Blake"],
         "Turner was famous for stormy seas and blazing sunsets. The Turner Prize began in 1984.",
         wiki("Turner Prize"), difficulty=3)
c.choice("Which English painter made The Hay Wain, showing a cart in a river?", "John Constable", ["J. M. W. Turner", "Thomas Gainsborough", "L. S. Lowry"],
         "Constable painted it in 1821. It's in the National Gallery in London.",
         wiki("The Hay Wain"), era="classic", difficulty=3)
c.choice("Who painted The Birth of Venus, showing a goddess on a giant shell?", "Sandro Botticelli", ["Leonardo da Vinci", "Raphael", "Titian"],
         "It hangs in the Uffizi Gallery in Florence.",
         wiki("The Birth of Venus"), difficulty=3)
c.choice("Who painted The Last Supper on the wall of a dining hall in Milan?", "Leonardo da Vinci", ["Michelangelo", "Raphael", "Caravaggio"],
         "Leonardo tried a new technique that didn't last well, so the paint began flaking off within his lifetime.",
         wiki("The Last Supper (Leonardo)"), difficulty=2)
c.choice("Which Spanish painter made Las Meninas, which shows the artist himself at work?", "Diego Velázquez", ["Francisco Goya", "El Greco", "Pablo Picasso"],
         "Picasso loved Las Meninas so much that he painted 58 versions of it.",
         wiki("Las Meninas"), difficulty=3)
c.choice("Which French artist made bright 'cut-outs' from painted paper late in life?", "Henri Matisse", ["Claude Monet", "Paul Cézanne", "Edgar Degas"],
         "When illness stopped him painting, Matisse 'drew with scissors'.",
         wiki("Henri Matisse"), difficulty=3)
c.choice("Which painter used thousands of tiny dots of colour, a style called pointillism?", "Georges Seurat", ["Vincent van Gogh", "Claude Monet", "Paul Gauguin"],
         "Seurat's A Sunday Afternoon on the Island of La Grande Jatte took him about two years.",
         wiki("Georges Seurat"), difficulty=3)
c.choice("Which art movement got its name from Claude Monet's painting Impression, Sunrise?", "Impressionism", ["Cubism", "Surrealism", "Expressionism"],
         "A critic meant the name as an insult in 1874. The painters took it on proudly.",
         wiki("Impression, Sunrise"), difficulty=2)
c.choice("Which Belgian artist painted a man in a bowler hat with an apple in front of his face?", "René Magritte", ["Salvador Dalí", "Joan Miró", "Max Ernst"],
         "The painting is called The Son of Man, from 1964.",
         wiki("The Son of Man"), era="classic", difficulty=3)
c.choice("Which American artist turned comic-strip pictures, complete with printed dots, into big paintings?", "Roy Lichtenstein", ["Andy Warhol", "Jasper Johns", "Keith Haring"],
         "Lichtenstein's dots copy the Ben-Day dots used to print comics cheaply.",
         wiki("Roy Lichtenstein"), era="classic", difficulty=3)
c.choice("Whose famous prints of Marilyn Monroe repeat her face in bright colours?", "Andy Warhol", ["Roy Lichtenstein", "David Hockney", "Banksy"],
         "Warhol made the Marilyn Diptych in 1962. He also said everyone would be famous for 15 minutes.",
         wiki("Marilyn Diptych"), era="classic", difficulty=2)
c.choice("What does the word 'Renaissance' mean?", "Rebirth", ["Golden age", "New painting", "Royal court"],
         "It describes the revival of art and learning in Europe from the 1300s to the 1600s, starting in Italy.",
         wiki("Renaissance"), difficulty=2)
c.choice("Which sculpture in Chicago's Millennium Park is nicknamed 'The Bean'?", "Cloud Gate", ["The Kelpies", "Spoonbridge and Cherry", "The Thinker"],
         "It's made of 168 stainless steel plates welded together and polished like a mirror. Anish Kapoor designed it.",
         wiki("Cloud Gate"), era="modern", difficulty=3)
c.choice("Which British artist put a real shark in a tank of preserving liquid as a work of art?", "Damien Hirst", ["Tracey Emin", "Banksy", "Antony Gormley"],
         "It's called The Physical Impossibility of Death in the Mind of Someone Living, from 1991.",
         wiki("The Physical Impossibility of Death in the Mind of Someone Living"), era="modern", difficulty=3)
c.choice("Which artist's famous work is her own unmade bed?", "Tracey Emin", ["Yoko Ono", "Damien Hirst", "Barbara Hepworth"],
         "My Bed was shortlisted for the Turner Prize in 1999.",
         wiki("My Bed"), era="modern", difficulty=3)
c.choice("Which giant horse heads made of steel stand beside a canal in Scotland?", "The Kelpies", ["The Angel of the North", "The Spirit of Ecstasy", "The Iron Horses"],
         "The Kelpies, near Falkirk, are 30 metres tall. Kelpies are shape-changing water horses in Scottish folklore.",
         wiki("The Kelpies"), era="modern", difficulty=2)
c.choice("Which Paris museum is inside an old railway station?", "The Musée d'Orsay", ["The Louvre", "The Pompidou Centre", "The Rodin Museum"],
         "The station opened for the 1900 World's Fair. The museum, full of Impressionist paintings, opened in 1986.",
         wiki("Musée d'Orsay"), difficulty=3)
c.choice("Which Spanish city has a Guggenheim Museum covered in curving titanium?", "Bilbao", ["Madrid", "Barcelona", "Seville"],
         "Frank Gehry designed it. It opened in 1997 and turned Bilbao into a tourist hotspot.",
         wiki("Guggenheim Museum Bilbao"), difficulty=3)
c.choice("In which city is the Prado, one of Spain's great art museums?", "Madrid", ["Barcelona", "Seville", "Valencia"],
         "The Prado opened in 1819 and has the world's best collection of Velázquez and Goya.",
         wiki("Museo del Prado"), difficulty=2)
c.choice("In which city is the Uffizi Gallery, home to Botticelli's Birth of Venus?", "Florence", ["Rome", "Venice", "Milan"],
         "The building was first designed as offices: uffizi means 'offices' in Italian.",
         wiki("Uffizi"), difficulty=3)
c.choice("In which city is the Rijksmuseum, home to The Night Watch?", "Amsterdam", ["Rotterdam", "Brussels", "The Hague"],
         "The Rijksmuseum is the national museum of the Netherlands. A cycle path runs right through the middle of the building.",
         wiki("Rijksmuseum"), difficulty=2)
c.yes_no("Is the Mona Lisa painted on canvas?", False,
         "It's painted on a panel of poplar wood.",
         wiki("Mona Lisa"), difficulty=3)
c.true_false("Picasso's full name has more than ten words in it.", True,
             "He was given a very long name, starting Pablo Diego José Francisco de Paula Juan Nepomuceno.",
             wiki("Pablo Picasso"), difficulty=3)
c.choice("Which British sculptor made smooth, rounded figures with holes through them, like Reclining Figure?", "Henry Moore", ["Antony Gormley", "Anish Kapoor", "Damien Hirst"],
         "Henry Moore was the son of a Yorkshire coal miner.",
         wiki("Henry Moore"), era="classic", difficulty=3)
c.choice("What do you call a picture an artist makes of themselves?", "A self-portrait", ["A still life", "A landscape", "A sketchbook"],
         "Rembrandt made around 80 self-portraits over his life.",
         wiki("Self-portrait"), difficulty=1)
c.choice("Which painter cut off part of his own ear in 1888?", "Vincent van Gogh", ["Paul Gauguin", "Claude Monet", "Edvard Munch"],
         "He later painted Self-Portrait with Bandaged Ear.",
         wiki("Vincent van Gogh"), difficulty=2)
