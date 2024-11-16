from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend_books():
    genre = request.form.get('genre')
    age_group = request.form.get('age_group')
    language = request.form.get('language')

    # Example book recommendations based on genre, age group, and language
    books = {
        'fiction': [ 'To Kill a Mockingbird by Harper Lee',
        '1984 by George Orwell',
        'Pride and Prejudice by Jane Austen',
        'The Great Gatsby by F. Scott Fitzgerald',
        'The Catcher in the Rye by J.D. Salinger',
        'The Hobbit by J.R.R. Tolkien',
        'Harry Potter and the Sorcerer\'s Stone by J.K. Rowling',
        'The Lord of the Rings by J.R.R. Tolkien',
        'The Chronicles of Narnia by C.S. Lewis',
        'The Book Thief by Markus Zusak',
        'The Kite Runner by Khaled Hosseini',
        'The Alchemist by Paulo Coelho',
        'Little Women by Louisa May Alcott',
        'The Secret Garden by Frances Hodgson Burnett',
        'The Handmaid\'s Tale by Margaret Atwood'],
        'sci-fi': [ 'Dune by Frank Herbert',
        'Neuromancer by William Gibson',
        'The Left Hand of Darkness by Ursula K. Le Guin',
        'The War of the Worlds by H.G. Wells',
        'Foundation by Isaac Asimov',
        'Snow Crash by Neal Stephenson',
        'The Martian by Andy Weir',
        'Altered Carbon by Richard K. Morgan',
        'Hyperion by Dan Simmons',
        'Ready Player One by Ernest Cline',
        'The Hunger Games by Suzanne Collins',
        'The Windup Girl by Paolo Bacigalupi',
        'The Three-Body Problem by Liu Cixin',
        'The Stars My Destination by Alfred Bester',
        'The Dispossessed by Ursula K. Le Guin'],
        'horror': [ 'Dracula by Bram Stoker',
        'Frankenstein by Mary Shelley',
        'The Shining by Stephen King',
        'It by Stephen King',
        'The Haunting of Hill House by Shirley Jackson',
        'The Exorcist by William Peter Blatty',
        'The Call of Cthulhu by H.P. Lovecraft',
        'The Silence of the Lambs by Thomas Harris',
        'Psycho by Robert Bloch',
        'Bird Box by Josh Malerman',
        'Mexican Gothic by Silvia Moreno-Garcia',
        'House of Leaves by Mark Z. Danielewski',
        'World War Z by Max Brooks',
        'The Girl Next Door by Jack Ketchum',
        'Hell House by Richard Matheson'],
        'comedy': [ 'Good Omens by Neil Gaiman and Terry Pratchett',
        'The Hitchhiker\'s Guide to the Galaxy by Douglas Adams',
        'Catch-22 by Joseph Heller',
        'The Importance of Being Earnest by Oscar Wilde',
        'The Princess Bride by William Goldman',
        'A Confederacy of Dunces by John Kennedy Toole',
        'The Rosie Project by Graeme Simsion',
        'Where d You Go, Bernadette by Maria Semple',
        'Bossypants by Tina Fey',
        'The Flatshare by Beth O\'Leary',
        'Eleanor Oliphant Is Completely Fine by Gail Honeyman',
        'The 100-Year-Old Man Who Climbed Out the Window and Disappeared by Jonas Jonasson',
        'The World According to Garp by John Irving',
        'The Eyre Affair by Jasper Fforde',
        'Fool by Christopher Moore'],
        'action': [ 'The Bourne Identity by Robert Ludlum',
        'The Girl with the Dragon Tattoo by Stieg Larsson',
        'The Hunt for Red October by Tom Clancy',
        'Jack Reacher by Lee Child',
        'The Spy Who Came in from the Cold by John le Carré',
        'The Day of the Jackal by Frederick Forsyth',
        'The Killing Floor by Lee Child',
        'The Silent Patient by Alex Michaelides',
        'The Lincoln Lawyer by Michael Connelly',
        'A Time to Kill by John Grisham',
        'The Dark Tower by Stephen King',
        'The Black Prism by Brent Weeks',
        'I Am Pilgrim by Terry Hayes',
        'The Secret Agent by Joseph Conrad',
        'The Bourne Supremacy by Robert Ludlum'],
        'thriller': [ 'The Girl on the Train by Paula Hawkins',
        'Gone Girl by Gillian Flynn',
        'The Silent Patient by Alex Michaelides',
        'Big Little Lies by Liane Moriarty',
        'The Woman in the Window by A.J. Finn',
        'Shutter Island by Dennis Lehane',
        'Before I Go to Sleep by S.J. Watson',
        'The Couple Next Door by Shari Lapena',
        'The Last Thing He Told Me by Laura Dave',
        'Anatomy of a Scandal by Sarah Vaughan',
        'Behind Closed Doors by B.A. Paris',
        'I Am Watching You by Teresa Driscoll',
        'The Woman in Cabin 10 by Ruth Ware',
        'The Reversal by Michael Connelly',
        'The Secret History by Donna Tartt'],
        'biography': ['The Diary of a Young Girl by Anne Frank',
        'Long Walk to Freedom by Nelson Mandela',
        'The Glass Castle by Jeannette Walls',
        'Steve Jobs by Walter Isaacson',
        'Becoming by Michelle Obama',
        'Educated by Tara Westover',
        'When Breath Becomes Air by Paul Kalanithi',
        'The Autobiography of Malcolm X by Malcolm X and Alex Haley',
        'Into the Wild by Jon Krakauer',
        'I Am Malala by Malala Yousafzai',
        'The Wright Brothers by David McCullough',
        'The Immortal Life of Henrietta Lacks by Rebecca Skloot',
        'The Long Hard Road to Freedom by Maya Angelou',
        'The Hiding Place by Corrie ten Boom',
        'The Zookeeper\'s Wife by Diane Ackerman'],
        'autobiography': [ 'The Autobiography of Benjamin Franklin by Benjamin Franklin',
        'The Story of My Life by Helen Keller',
        'I Know Why the Caged Bird Sings by Maya Angelou',
        'A Moveable Feast by Ernest Hemingway',
        'The Long Hard Road to Freedom by Maya Angelou',
        'The Autobiography of Mark Twain by Mark Twain',
        'Night by Elie Wiesel',
        'My Life So Far by Jane Fonda',
        'The Seven Storey Mountain by Thomas Merton',
        'On Writing by Stephen King',
        'When Breath Becomes Air by Paul Kalanithi',
        'Becoming by Michelle Obama',
        'The Glass Castle by Jeannette Walls',
        'The Wright Brothers by David McCullough',
        'Steve Jobs by Walter Isaacson'],
    }

    # Example of filtering recommendations based on genre
    recommended_books = books.get(genre, [])

    return render_template('index.html', books=recommended_books, genre=genre, age_group=age_group, language=language)

if __name__ == '__main__':
    app.run(debug=True)