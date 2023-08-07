-- 1. In the dvdrental database write a query to select all the columns from the “customer” table.
SELECT * FROM customer

-- 2. Write a query to display the names (first_name, last_name) using an alias named “full_name”.
SELECT first_name, last_name AS full_name FROM customer

-- 3. Lets get all the dates that accounts were created. Write a query to select all the create_date from the “customer” table (there should be no duplicates).
SELECT create_date FROM customer GROUP BY create_date ORDER BY min(create_date)

-- 4. Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.
SELECT first_name FROM customer ORDER BY first_name DESC

-- 5. Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.
SELECT film_id, title, description, release_year, rental_rate FROM film ORDER BY rental_rate 

-- 6. Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.
SELECT phone FROM address WHERE district = 'Texas'

-- 7. Write a query to retrieve all movie details where the movie id is either 15 or 150.
SELECT * FROM film WHERE film_id = 15 OR film_id = 150

-- 8. Write a query which should check if your favorite movie exists in the database. Have your query get the film ID, title, description, length and the rental rate, these details can be found in the “film” table.
SELECT film_id, title, description, length, rental_rate FROM film WHERE title LIKE '%favorite_movies%'

-- 9. No luck finding your movie? Maybe you made a mistake spelling the name. Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.
SELECT film_id, title, description, length, rental_rate FROM film WHERE title ILIKE 'al%'

-- 10. Write a query which will find the 10 cheapest movies.
SELECT film_id, title, description, length, rental_rate FROM film ORDER BY rental_rate FETCH FIRST 10 ROWS ONLY

-- 11. Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
--     Bonus: Try to not use LIMIT.
SELECT film_id, title, description, length, rental_rate FROM film ORDER BY rental_rate OFFSET 10 ROWS FETCH FIRST 10 ROWS ONLY

-- 12. Write a query which will join the data in the customer table and the payment table. You want to get the first name and last name from the curstomer table, as well as the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).
SELECT first_name, last_name, amount, payment_date FROM customer FULL JOIN payment ON customer.customer_id = payment.customer_id;

-- 13. You need to check your inventory. Write a query to get all the movies which are not in inventory.
SELECT * FROM film FULL OUTER JOIN inventory ON film.film_id = inventory.inventory_id WHERE film.film_id NOT IN (inventory.film_id)

-- 14. ELECT country_id, country FROM country
SELECT customer.first_name, customer.last_name, payment.amount, payment.payment_date, staff.staff_id AS the_order FROM customer JOIN payment ON customer.customer_id = payment.customer_id JOIN staff ON staff.staff_id = payment.staff_id ORDER BY the_order

-- 15. Bonus You want to be able to see how your sellers have been doing? Write a query to get the customer’s id, names (first and last), the amount and the date of payment ordered by the id of the staff member who sold them the dvd.
SELECT city.city, country.country FROM city JOIN country ON city.country_id = country.country_id