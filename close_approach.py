from helpers import cd_to_datetime, datetime_to_str


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(self, **info):
        """Create a new `CloseApproach`.

        :param string time: The date and time (in UTC) of closest approach.
        NASA's format, at least in the `cd`
        field of close approach data, uses the English locale's month names.
        For example, December 31st, 2020 at noon
        is: 2020-Dec-31 12:00
        :param float distance: The nominal approach distance in astronomical
        units.
        :param float velocity: The relative approach velocity in kilometers per
        second.
        :param NearEarthObject neo: Reference to its `NearEarthObject` -
        initially, this information
        (the NEO's primary designation) is saved in a private attribute, but
        the referenced NEO is
        eventually replaced in the `NEODatabase` constructor.
        """
        for key, value in info.items():
            # assign the designation parameter
            if key.lower() == 'des':
                # check the value of the parameter to avoid
                # an inappropriate value
                try:
                    # if the type of value is not string
                    self._designation = str(value)
                except ValueError:
                    # print the text message
                    print(f'The type of {key} is not string')

            # assign the time parameter
            elif key.lower() == 'cd':
                # check the value of the parameter to avoid
                # an inappropriate value
                try:
                    # if the type of value is not string
                    self.time = str(value)
                    self.time = cd_to_datetime(self.time)
                except ValueError:
                    # print the text message
                    print(f'The type of {key} is not string')

            # assign the distance parameter
            elif key.lower() == 'dist':
                # check the value of the parameter to avoid
                # an inappropriate value
                try:
                    # if the type of value is not float
                    self.distance = float(value)
                except ValueError:
                    # print the text message
                    print(f'The type of {key} is not float')

            # assign the velocity parameter
            elif key.lower() == 'v_rel':
                # check the value of the parameter to avoid
                # an inappropriate value
                try:
                    # if the type of value is not float
                    self.velocity = float(value)
                except ValueError:
                    # print the text message
                    print(f'The type of {key} is not float')

        self.neo = self._designation

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s
        approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default
        representation includes seconds - significant figures that don't
        exist in our input data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        return f"Approach time of {self._designation} was at " \
               f"{datetime_to_str(self.time)}"

    def get_neo_primary_designation(self) -> str:
        return self._designation

    @property
    def designation(self):
        """To access to the self._designation.

        :return: self._designation
        """
        return self._designation

    def __str__(self):
        """Return `str(self)`."""
        return f"A CloseApproach time={self.time_str} " \
               f"distance={self.distance} velocity={self.velocity} " \
               f"neo={self.neo}"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of
        this object."""
        return (
            f"CloseApproach(time={self.time_str!r}, "
            f"distance={self.distance:.2f}, "f"velocity={self.velocity:.2f}, "
            f"neo={self.neo!r})")
