import api_routes.api as route


def test_total_authors():
    # Test case 1 - Verify total number of authors
    assert len(route.get_author()['authors']) == 129


def test_poem_line():
    # Test case 2 - Verify line of a poem
    assert route.get_poem(poem='To My Wife - With A Copy Of My Poems')[0]['lines'][2] == 'From a poet to a poem'


def test_line_author():
    # Test case 3 - Verify author of poem's line
    assert route.get_line_author(line='From a poet to a poem')[0]['author'] == 'Oscar Wilde'
