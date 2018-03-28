Dataprint
=========

Dataprint prints a table that scales column widths to fit the data.
Written to mesh with the sqlite3 python module, specifically
cursor.description (list comp-ed to only have the column labels), and
cursor.fetchall(). Each row in the values list is treated as a row of
table data, and element order in the list corresponds to the order of
column labels. Use the 'transpose' argument if you data is formated with
each row representing a column of data.

Example
=======

A redacted example from a side project of mine (https://github.com/mkitzan/terminus):

::

    *--------------------------------------*---------------*----------------*-----*------*--------*
    |Title                                 |Author         |Genre           |Year |Pages |Type    |
    *--------------------------------------*---------------*----------------*-----*------*--------*
    |Ellison Wonderland                    |Harlan Ellison |science fiction |1962 |191   |stories |
    |Dangerous Visions                     |Harlan Ellison |science fiction |1967 |598   |stories |
    |Love Ain't Nothing but Sex Misspelled |Harlan Ellison |science fiction |1968 |380   |stories |
    |Again, Dangerous Visions vol.1        |Harlan Ellison |science fiction |1972 |450   |stories |
    |Again, Dangerous Visions vol.2        |Harlan Ellison |science fiction |1972 |449   |stories |
    |Approaching Oblivion                  |Harlan Ellison |science fiction |1974 |164   |stories |
    |Deathbird Stories                     |Harlan Ellison |science fiction |1975 |347   |stories |
    |Stalking the Nightmare                |Harlan Ellison |science fiction |1982 |301   |stories |
    |Angry Candy                           |Harlan Ellison |science fiction |1988 |324   |stories |
    |Slippage                              |Harlan Ellison |science fiction |1997 |359   |stories |
    *--------------------------------------*---------------*----------------*-----*------*--------*

Usage
=====

First import the function 'table' from dataprint

::

    from dataprint import table

For a standard table use

::

    table(col_labels, values)

For an augmented table use the expected arguments, and any combination
of the five non-standard arguments

::

    table(col_labels, values, header="Look at this table", transpose=True, edge="#", padding=2, printer=lambda row: outfile.write(row + "\n"))

Non-Standard Arguments
======================

-  header (default None): will print whatever this string is above the
   table.

-  transpose (default False): will transpose the values argument if
   transpose=True. Helpful if a row in values corresponds to a column in
   the table rather than the expected values row corresponds to a table
   row (format of a sqlite3 fetchall call)

-  edge (default "\*"): when a horizontal line ("-") intersects a
   vertical line ("\|") in the table, an edge character is placed. By
   default a star is used, but, by including an argument for edge when
   table is called, you can augment what this character is.

-  padding (default 1): buffer determines the amount of whitespace
   between the end of the longest value in a column and that column's
   right vertical divider. Example: \|example of buffer=1 \|

-  printer (default print): allows user to write the output of dataprint
   to a file, or call some function with each line of dataprint's output
   as an argument. Each line of output is a string, so be sure your
   function takes that into account.
