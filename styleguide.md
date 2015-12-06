## Testing

Tests should:

* Clean up any generated artifacts.
* Be compatible with Nose.
* be defined as: test_%library%_%object%_%function%_%input type%
    * e.g. ```def test_librarian_Book_assign_tutle_int()```
* take no input
* be file seperated for each class, and folder seperated for each library
    * e.g. ```librarian/Book.md```
* called by test/test.py correctly
* fail if returns are different than stated in the docstring
* fail verbosely.
    * A failed test should print the expected value, and the received value to stdout.
* fail if no docstring is present.
* fail by asserting False
* pass by calling ```pass```

The minimum tests are:

* object instantiation
* object type
* object initialisation values
* string, int, list typed inputs for all functions
