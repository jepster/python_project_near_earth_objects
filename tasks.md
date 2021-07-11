* [DONE] Task 0: Inspect data. (data/neos.csv and data/cad.json)
* [DONE] Task 1: Build models. (models.py)
Write __init__ and __str__ methods for NearEarthObject and CloseApproach
* [DONE] Task 2a: Extract data. (extract.py)
Implement load_neos and load_approaches to read data from CSV and JSON files.
* Task 2b: Process data. (database.py)
Implement the constructor for NEODatabase, preprocessing the data to help with future queries.
Write methods to get NEOs by primary designation or by name.
* Task 3a: Create filters. (filters.py)
Define a hierarchy of Filters.
Implement create_filters to create a collection of filters from user-specified criteria.
* Task 3b: Query matching close approaches (database.py)
Implement the query method to generate a stream of CloseApproaches that match the given filters.
* Task 3c: Limit results. (filter.py)
Write limit to produce only the first values from a generator.
* Task 4: Save data. (write.py)
Implement write_to_csv and write_to_json to save structured data to a formatted file.