#Messing around with API Calls

For this exercise, we started playing around with API calls, and seeing what information we can scrape from a quick API call to postcodes.io, a database of the postcodes in the UK. The first challenge was to ensure that the postcode exists.

To achieve this, we make a call to the page associated with the postcode, once the user has input it. For a website working as intended, the code being returned will be 200, which we use to action some control flow.

## Extracting more data

Whilst we can use a simple command from `requests` to check the status code, we cannot do this to extract individual pieces of data. As an exercise, I attempted to extract the parliamentary constituency from the postcode page. To do this, I first extracted a json of the scraped data using the `requests.get` command. This gets the data in the Json format, which stands for JavaScript Object Notation. Using python's json package allows the conversion of this into a dictionary, from which more data can be extracted once properly formatted.

I then used python to obtaint he value of the dictionary I was interested in, in this case the parliamentary constituency, and return it to the user.