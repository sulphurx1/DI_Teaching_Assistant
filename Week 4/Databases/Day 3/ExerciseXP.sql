-- 1. Get a list of all the languages, from the language table.
SELECT * FROM language

-- 2. Get a list of all films joined with their languages – select the following details : film title, description, and language name.
SELECT title, name FROM film JOIN language on film.language_id = language.language_id 

-- 3. Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.
