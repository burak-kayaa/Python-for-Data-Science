class ft_tqdm:
    """Custom tqdm class to display the progress bar.

    ...

    Attributes
    ----------
    iterable : iterable
        the iterable to iterate over
    total : int
        the total number of items in the iterable (default None)
    length : int
        the length of the progress bar (default 40)

    Methods
    -------
    __iter__()
        Iterate over the iterable and display the progress bar.
    display_progress(current)
        Display the progress bar.
    """
    def __init__(self, iterable, total=None, length=130):
        """
        Parameters
        ----------
        iterable : iterable
            the iterable to iterate over
        total : int
            the total number of items in the iterable (default None)
        length : int
            the length of the progress bar (default 40)
        """

        self.iterable = iterable
        self.length = length
        self.total = total if total is not None else len(iterable)

    def __iter__(self):
        """Iterate over the iterable and display the progress bar.

        Yields
        ------
        item
            the item from the iterable
        """

        for i, item in enumerate(self.iterable):
            yield item
            self.display_progress(i + 1)

    def display_progress(self, current):
        """Display the progress bar.

        Parameters
        ----------
        current : int
            the current number of items processed

        Returns
        -------
        None
        """

        progress = current / self.total
        filled_length = int(self.length * progress)

        bar = '█' * filled_length + ' ' * \
            ((self.length - filled_length))
        percent = progress * 100
        print(f'\r{int(percent)}%|{bar}| {current}/{self.total}', end='')
        if current == self.total:
            print()
