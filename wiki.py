import wikipedia

print(wikipedia.summary('Mahatma gandhi'))


#If you want to create a complete wikipedia search use this function named wikisearch.Call the function if you wanted

def wikisearch():
    while True:

        a=input('search:')
        print(wikipedia.summary(a))


