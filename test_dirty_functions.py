from dirty_function import  random_famous

def test_random_famous():
    Famous = ('Max', 'Leo', 'Kate')
    assert len(random_famous(('bob', "Leo", "Tom"))) == 2
    for person  in random_famous(Famous,2):
        assert person in Famous
