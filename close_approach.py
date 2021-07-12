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
    # [DONE] TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.
    def __init__(self, **info):
        """Create a new `CloseApproach`.

        :param string time: The date and time (in UTC) of closest approach. NASA's format, at least in the `cd`
        field of close approach data, uses the English locale's month names. For example, December 31st, 2020 at noon
        is: 2020-Dec-31 12:00
        :param float distance: The nominal approach distance in astronomical units.
        :param float velocity: The relative approach velocity in kilometers per second.
        :param NearEarthObject neo: Reference to its `NearEarthObject` - initially, this information
        (the NEO's primary designation) is saved in a private attribute, but the referenced NEO is
        eventually replaced in the `NEODatabase` constructor.
        """
        # [DONE] TODO: Assign information from the arguments passed to the constructor
        # onto attributes named `_designation`, `time`, `distance`, and `velocity`.
        # You should coerce these values to their appropriate data type and handle any edge cases.
        # The `cd_to_datetime` function will be useful.
        # parse the keyword parameters
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
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        # [DONE] TODO: Use this object's `.time` attribute and the `datetime_to_str` function to
        # build a formatted representation of the approach time.
        # [DONE] TODO: Use self.designation and self.name to build a fullname for this object.
        return f"Approach time of {self._designation} was at {datetime_to_str(self.time)}"

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
        # [DONE] TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.
        return f"A CloseApproach time={self.time_str} distance={self.distance} velocity={self.velocity} neo={self.neo}"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
                f"velocity={self.velocity:.2f}, neo={self.neo!r})")
