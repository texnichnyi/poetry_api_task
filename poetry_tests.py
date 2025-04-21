import requests

base_route = 'https://poetrydb.org'

# Test case 1 - Verify total number of authors
assert len(requests.get(f'{base_route}/author').json()['authors']) == 129

# Test case 2 - Verify line of a poem
assert requests.get(f'{base_route}/title/To My Wife - With A Copy Of My Poems').json()[0]['lines'][2] == 'From a poet to a poem'

# Test case 3 - Verify author of poem's line
assert requests.get(f'{base_route}/lines/From a poet to a poem/author').json()[0]['author'] == 'Oscar Wilde'
