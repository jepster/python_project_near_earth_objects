from close_approach import CloseApproach


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object,
    such as its primary designation (required, unique), IAU name
    (optional), diameter in kilometers (optional - sometimes unknown),
    and whether it's marked as potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close
    approaches - initialized to an empty collection, but eventually
    populated in the `NEODatabase` constructor.
    """

    # If you make changes, be sure to update the comments in this file.
    def __init__(self, **info):
        """Create a new `NearEarthObject`.

        :param info: A dictionary of excess keyword arguments supplied to
        the constructor.
        """
        # onto attributes named `designation`, `name`, `diameter`, and `
        # hazardous`.
        # You should coerce these values to their appropriate data type
        # and handle any edge cases, such as a empty name being
        # represented by `None` and a missing diameter being represented
        # by `float('nan')`.

        # parse the keyword parameters
        for key, value in info.items():
            # assign the designation parameter
            if key.lower() == 'pdes':
                # check the value of the parameter to avoid
                # an inappropriate value
                try:
                    # if the type of value is not string
                    self.designation = str(value)
                except ValueError:
                    # print the text message
                    print(f'The type of {key} is not string')

            # assign the name parameter
            elif key.lower() == 'name':
                # check the value of the parameter to avoid
                # an inappropriate or none value
                if len(value) != 0:
                    try:
                        # if the type of value is not string
                        self.name = str(value)
                    except ValueError:
                        # print the text message
                        print(f'The type of {key} is not string')
                else:
                    # if the value is none, set the value to 'None' (string)
                    self.name = None

            # assign the diameter parameter
            elif key.lower() == 'diameter':
                # check the value of the parameter to avoid
                # an inappropriate or none value
                if len(value) != 0:
                    try:
                        # if the type of value is not float
                        self.diameter = float(value)
                    except ValueError:
                        # print the text message
                        print(f'The type of {key} is not float')
                else:
                    self.diameter = float('nan')

            # assign the hazardous parameter
            elif key.lower() == 'pha':
                # check the value of the parameter to avoid
                # an inappropriate value
                try:
                    # if the type of value is not bool
                    self.hazardous = str(value)
                    if self.hazardous.lower() == 'y':
                        self.hazardous = True
                    else:
                        self.hazardous = False
                except ValueError:
                    # print the text message
                    print(f'The type of {key} is not string')

        # Create an empty initial collection of linked approaches.
        self.approaches = []

    def append(self, аpproach):
        """To add the information about a close approach.

        :param аpproach: a close approach to addition
        :return: just add information
        """
        if isinstance(аpproach, CloseApproach):
            self.approaches.append(аpproach)

    def serialize(self):
        """To serialize an object.

        :return: serialized object of NearEarth
        """
        return {'designation': self.designation,
                'name': self.name,
                'diameter_km': self.diameter,
                'potentially_hazardous': self.hazardous}

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        if self.name is not None:
            return f"'{self.designation} ({self.name})'"
        else:
            return f'{self.designation}'

    def __str__(self):
        """Return `str(self)`."""
        # The project instructions include one possibility. Peek at the
        # __repr__  # method for examples of advanced string formatting.

        if self.hazardous:
            return f'NEO {self.name} has a diameter of {self.diameter} km ' \
                   f'and is potentially hazardous.'
        else:
            return f'NEO {self.name} has a diameter of {self.diameter} km ' \
                   f'and is not potentially hazardous.'

    def __repr__(self):
        """Return a computer-readable string representation.

        Return `repr(self)`, a computer-readable string representation
        of this object.
        """
        return (f"NearEarthObject(designation={self.designation}, "
                f"name={self.name}, "
                f"diameter={self.diameter}, hazardous={self.hazardous})")
