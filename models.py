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
    def __init__(self, designation, iau_name='', diameter=float('nan'), hazardous=None, close_approach_collection=None):
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
        self.iau_name = iau_name
        self.diameter = diameter
        self.hazardous = hazardous
        # Create an empty initial collection of linked approaches.
        self.close_approach_collection = close_approach_collection

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        # [DONE] TODO: Use self.designation and self.name to build a fullname for this object.
        return self.designation + ' ' + self.iau_name

    def __str__(self):
        """Return `str(self)`."""
        # [DONE] TODO: Use this object's attributes to return a human-readable string representation.
        # The project instructions include one possibility. Peek at the __repr__
        # method for examples of advanced string formatting.

        info = {
            "designation": self.designation,
            "iau_name": self.iau_name,
            "diameter": self.diameter,
            "hazardous": self.hazardous,
            "close_approach_collection": self.close_approach_collection
        }

        return f"NearEarthObject({info})"

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (f"NearEarthObject(designation={self.designation!r}, name={self.iau_name!r}, "
                f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})")


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
    def __init__(self, time, distance, velocity, neo):
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
        self._neo_primary_designation = neo.designation
        self.time = cd_to_datetime(time)  # [DONE] TODO: Use the cd_to_datetime function for this attribute.
        self.distance = float(distance)
        self.velocity = float(velocity)

        # Create an attribute for the referenced NEO, originally None.
        self.neo = neo

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
        return f"Approach time of {self._neo_primary_designation} was at {datetime_to_str(self.time)}"

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
