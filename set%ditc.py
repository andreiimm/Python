movie_suggestion = {"Finding Nemo", "The 100", "Maleficent","Call Me By Your Name", "The Babadook", "Finding Nemo"}
print(" Lsit of films: " ,movie_suggestion)
movie_details = {
    "Maleficent" : 10,
    "Finding Nemo" : 4 ,
    "Call Me By Your Name" : 8.5
}

movie_suggestion.add("The Nun")
movie_suggestion.remove("The Babadook")

print("Updated List of films : ",
movie_suggestion)

movie_details["The 100"] = 8.9
movie_details["Finding Nemo"] = 2
print("Furtherly more updated details : ",movie_details)
print()
