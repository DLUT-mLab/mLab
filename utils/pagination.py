PAGE_LIMIT = 5


class Pagination:

    def __init__(self, start, end, all_count):
        self.start = start
        self.end = end
        self.all_count = all_count

