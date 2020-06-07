# Smart XML analyzer

#### Env: python 3.7.4

## To run the application:
- Run `pip install -r requirements.txt` to install dependencies.
- Run `python3 main.py ${origin_file_path} ${diff_file_path} ${element_id}` to run an application from command line.
- Run `python3 tests.py` to run the tests.

## Command-line execution example:
- `python3 samples/sample-0-origin.html samples/sample-1-evil-gemini.html make-everything-ok-button`

## P.S.:
- First of all, I hope I got the task's gist correctly. Thank you very much for that short challenge:)
- The logic for searching the most appropriate match is simple: we just match all attributes + text values of the
origin element with an according data from matching elements found by the same tag.
- If we need the 'fuzzy' match then we can use https://pypi.org/project/python-Levenshtein/ and calculate the distance for
each value and keep lowest distance as the best match.
- `cssselect` returns a list of elements, it is not a generator. So if there is a large number of elements with such tag 
in the file, then it could produce some problems.
- Unit tests have some boilerplate. I guess pytest.mark.parametrize would solve it, but I already have 2 dependencies for 
 such easy task:)
- Please let me know if I need to remove that code from public GitHub in order to give all other candidates the same 
opportunity to solve the exercise in their own way.