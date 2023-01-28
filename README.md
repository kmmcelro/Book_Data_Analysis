# Book_Data_Analysis
Project to obtain information about the books on your bookshelves and create graphic interpretations of the data.

The file, Book Backlog - Template.xlsx, is the blank example of the spreadsheet that the program will populate information about your books as long as you include the title.
This file should be renamed to Book Backlog.xlsx once you start adding your books to the spreadsheet.
Categories such as Read Status,	Read Date, 	DNF Status,	Owning Status,	Format,	and Location are ones that are specific to you and you must fill out for yourself.
However, for the purpose of the analysis later, the variety inputs that I used for Read Status,	Owning Status,	Format,	and Location are listed in the template. 
I recommend sticking to these if you also want to use the analysis program.

Storygraph_Extraction_v3.py contains the functions to search storygraph for the link and book data.
Please note that these functions are compatible with the Storygraph UI updates made as of January 2023. 
Future UI updates will likely require further updates to the functions, as Storygraph does not currently have an API.
SE_tests.py tests the functions in the above file and confirm their functionality for several different search results.
Some titles like The Hobbit, or There and Back Again do require you to search with the whole name or include the author name due to search limitations.

Excel_format.py is the script that you run to update your spreadsheet with the available Storygraph details about your collection of books.
