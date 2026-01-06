MongoDB - Non-relational databases
=========

Definition
----------

Non-relational databases have been established as the favorite option for the Internet of Things paradigm based on their flexibility over their data structure and a faster data retrieve when compared with relational databases. 
Therefore, non-relational database presents qualities more compatibles with the expected needs of the smart bio-manufacturing, and it is then the data storage strategy selected for our database.

MongoDB is currently the most popular example of non-relational database program. Some examples of software using MongoDB are SEGA, BARCLAYS, or the tax platform for the UK government, etc.
MongoDB organizes its data in documents that subsequently are organized in collections, usually with common fields between documents. Those documents characterize by be available to store their data in a JSON data format. 


How to...
------------------------------------------
It is a simple script using Flask in order to create a REST API with a mongo database to get and post data.


.. literalinclude:: scripts/example_pymongo.py