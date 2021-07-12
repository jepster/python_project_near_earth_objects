"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""
from helpers import cd_to_datetime, datetime_to_str
from close_approach import CloseApproach


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """
    # [DONE] TODO: How can you, and should you, change the arguments to this constructor?
    # If you make changes, be sure to update the comments in this file.
    def __init__(self, designation: str, iau_name=None, diameter=float('nan'), hazardous=None,
                 close_approach_collection=None):
        """Create a new `NearEarthObject`.

        :param string designation: Its primary designation (required, unique).
        :param string iau_name: [optional] The IAU name
        :param float diameter: [optional] The diameter in kilometers
        :param None|bool hazardous: [optional] Marks the entity as hazardous or not
        :param list close_approach_collection: [optional] A collection of the close approaches.
        """
        # [DONE] TODO: Assign information from the arguments passed to the constructor
        # onto attributes named `designation`, `name`, `diameter`, and `hazardous`.
        # You should coerce these values to their appropriate data type and
        # handle any edge cases, such as a empty name being represented by `None`
        # and a missing diameter being represented by `float('nan')`.
        self.designation = designation
        if iau_name == '':
            iau_name = None
        self.name = iau_name
        try:
            # if the type of value is not float
            self.diameter = float(diameter)
        except ValueError:
            self.diameter = float('nan')
            print(f'The type of {diameter} is not float')

        self.hazardous = hazardous
        # Create an empty initial collection of linked approaches.
        self.close_approach_collection = close_approach_collection

    @property
    def fullname(self) -> str:
        """Return a representation of the full name of this NEO."""
        # [DONE] TODO: Use self.designation and self.name to build a fullname for this object.
        return self.designation + ' ' + self.name

    @property
    def approaches(self):
        if self.close_approach_collection is None:
            return set()
        return self.close_approach_collection

    def link_close_approach(self, close_approach: CloseApproach):
        if self.close_approach_collection is None:
            self.close_approach_collection = [close_approach]
        else:
            self.close_approach_collection.append(close_approach)

    def __str__(self) -> str:
        """Return `str(self)`."""
        # [DONE] TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.

        info = {
            "designation": self.designation,
            "iau_name": self.name,
            "diameter": self.diameter,
            "hazardous": self.hazardous,
            "close_approach_collection": self.close_approach_collection
        }

        return f"NearEarthObject({info})"

    def __repr__(self) -> str:
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")
