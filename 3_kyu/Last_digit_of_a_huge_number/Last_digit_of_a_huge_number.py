def last_digit(lst):
    pass




if __name__ == "__main__":
        assert last_digit([]) == 1
        assert last_digit([0, 0]) == 1
        assert last_digit([0, 0, 0]) == 0
        assert last_digit([1, 2]) == 1
        assert last_digit([3, 4, 5]) == 1
        assert last_digit([4, 3, 6]) == 4
        assert last_digit([7, 6, 21]) == 1
        assert last_digit([12, 30, 21]) == 6
        assert last_digit([2, 2, 2, 0]) == 4
        assert last_digit([937640, 767456, 981242]) == 0
        assert last_digit([123232, 694022, 140249]) == 6
        assert last_digit([499942, 898102, 846073]) == 6
        