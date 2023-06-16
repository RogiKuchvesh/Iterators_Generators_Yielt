class FlatIterator:
    def __init__(self, list_of_lists):
        self.list_of_lists = list_of_lists        

    def __iter__(self):
        self.sublist_cursor = 0
        self.item_cursor = 0
        self.final_list = []
        return self

    def __next__(self):        
        if self.sublist_cursor >= len(self.list_of_lists):
            raise StopIteration
        
        else:
            sublist = self.list_of_lists[self.sublist_cursor]
            if self.item_cursor < len(sublist):
                item = sublist[self.item_cursor]
                self.item_cursor += 1
                return item
            else:
                self.sublist_cursor += 1
                self.item_cursor = 0
                return self.__next__()

if __name__ == "__main__":
    list_of_lists = [["a", "b", "c"], ["d", "e", "f", "h", False], [1, 2, None]]
    flat_iterator = FlatIterator(list_of_lists)
    print(list(flat_iterator))

def test_1():
    list_of_lists_1 = [["a", "b", "c"], ["d", "e", "f", "h", False], [1, 2, None]]

    for flat_iterator_item, check_item in zip(
        FlatIterator(list_of_lists_1),
        ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None],
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None]


if __name__ == "__main__":
    test_1()
