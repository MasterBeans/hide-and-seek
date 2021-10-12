import random


class Hider:
    """A code template for a hider whom the seeker looks for. The
    responsibility of this class of objects is to stay in one location so that
    the seeker will be able to pursue and find the location.

    Stereotype:
        Information Holder

    Attributes:
        location (integer): The location of the Hider (1-1000).
        distance (list): The distance from the Seeker.
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Hider): An instance of Hider.
        """
        self.location = random.randint(1, 1000)
        self.distance = [0, 0]  # start with two so get_message always works

    def get_hint(self):
        """Gets a message for the seeker.

        Args:
          self (Hider): An instance of Hider.

        Returns:
          string: A message from the hider.
        """
        message = "(^.^) Getting colder!"
        if self.distance[-1] == 0:
            message = "(;.;) You found me!"
        elif self.distance[-1] < self.distance[-2]:
            message = "(>.<) Getting warmer!"
        elif self.distance[-1] > self.distance[-2]:
            message = "(^.^) Getting colder!"
        return message

    def watch(self, location):
        """Watch for the seeker's location and keeps track of the distance.

        Args:
          self (Hider): An instance of Hider.
        """
        distance = abs(self.location - location)
        self.distance.append(distance)
