import types

def flat_generator(list_of_lists):
    cursor = 0
    while cursor < len(list_of_lists):
        list_ = list_of_lists[cursor]
        for element in list_:
            yield element
        cursor += 1  

if __name__ == '__main__':
    list_of_lists = [
         ['a', 'b', 'c'],
         ['d', 'e', 'f', 'h', False],
         [1, 2, None]
         ]

    print(list(flat_generator(list_of_lists)))
       

def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
    