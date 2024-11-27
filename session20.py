from datetime import datetime
from typing import Union
import math

class Person:
    """
    A class representing a person with attributes such as name, age, year of birth, and salary details.

    Attributes:
        _first_name (str): The first name of the person.
        _last_name (str): The last name of the person.
        _yob (int): The year of birth of the person.
        _base_salary (int): The base salary of the person.
        _bonus (float): The bonus percentage of the salary.
    """
    def __init__(self, first_name: str = '', last_name: str = '', birth_year: int = None):
        """
        Initializes the Person instance.

        Args:
            first_name (str): The first name of the person (default: '').
            last_name (str): The last name of the person (default: '').
            year (int): The year of birth of the person (default: None).
        """
        self._first_name = first_name
        self._last_name = last_name
        self._birth_year = birth_year
        self._base_salary = None
        self._bonus = None

    @property
    def current_year(self):
        """Read-only property that returns the current year"""
        return datetime.now().year

    @property
    def age(self):
        """
        Returns:
            int: The age of the person based on their year of birth.
        """
        if self._birth_year is not None:
            return self.current_year - self._birth_year
        return None

    def set_birth_year(self, year):
        """
        Sets the year of birth.

        Args:
            year (int): The year of birth.

        Raises:
            ValueError: If the year is not an integer.
        """
        if not isinstance(year, int):
            raise ValueError('Year must be of type int')
        self._birth_year = year

    @property
    def full_name(self)  -> str:
        """
        Returns:
            str: The full name of the person.
        """
        return f"{self._first_name} {self._last_name}".strip()

    @full_name.setter
    def full_name(self, name: str = None) -> None:
        """
        Sets the first and last name.

        Args:
            f_name (str): Full name string with first and last names.

        Raises:
            ValueError: If the input is not a string or does not include both first and last names.
        """
        if not isinstance(name, str):
            raise ValueError('Full name must be of type str')

        parts = name.split()
        if len(parts) >= 2:
            self._first_name = parts[0]
            self._last_name = " ".join(parts[1:])
        else:
            raise ValueError("Full name must include both first and last name")

    @property
    def first_name(self) -> str:
        """Returns the first name of the person."""
        return self._first_name

    @property
    def last_name(self) -> str:
        """Returns the last name of the person."""
        return self._last_name

    def _validate_bonus(self, bonus):
        """
        Validate the bonus value to ensure it is within the acceptable range.

        Parameters:
        ----------
        bonus : int or float
            The bonus value to validate, expected to be in the range [0, 100].

        Returns:
        -------
        int or float
            The validated bonus value if it is within the range.

        Raises:
        ------
        ValueError
            If the bonus value is not between 0 and 100 (inclusive).

        """
        if not 0 <= bonus <= 100:
            raise ValueError("Bonus must be between 0 and 100")
        return bonus

    @property
    def bonus(self):
        """
        Get the bonus percentage.

        Returns:
        -------
        float or int
            The current bonus percentage value.
        """
        return self._bonus

    @bonus.setter
    def bonus(self, value):
        """
        Set the bonus percentage after validation.

        Parameters:
        ----------
        value : float or int
            The bonus percentage to be set. Must be between 0 and 100.

        Raises:
        ------
        ValueError
            If the bonus value is not within the acceptable range.
        """
        self._bonus = self._validate_bonus(value)

    @property
    def base_salary(self) -> Union[int, None]:
        """
        Get the base salary of the person.

        Returns:
        -------
        int or None
            The base salary value, or None if not set.
        """
        return self._base_salary

    def set_salary(self, base_salary: int, bonus: Union[float, int]) -> None:
        """
        Sets the base salary and bonus percentage.

        Args:
            base_salary (int): The base salary.
            bonus (Union[float, int]): The bonus percentage.

        Raises:
            ValueError: If the inputs are invalid.
        """
        if not isinstance(base_salary, int):
            raise ValueError('Base Salary must be of type int')
        if not isinstance(bonus, (int, float)):
            raise ValueError('Bonus must be of type int or float')
        if base_salary < 0:
            raise ValueError('Base Salary must be non-negative')
        self._validate_bonus(bonus)
        self._base_salary = base_salary
        self._bonus = bonus

    @property
    def salary(self) -> Union[float, int]:
        """
        Compute the total salary including the bonus.

        Returns:
        -------
        float or int
            The total salary, including the calculated bonus amount, or 0 if 
            base salary or bonus is not set.

        Notes:
        ------
        - Total salary is calculated as:
        `base_salary + (base_salary * (bonus / 100))`.
        - If either `base_salary` or `bonus` is None, returns 0.
        """
        if self._base_salary is not None and self._bonus is not None:
            bonus_amount = self._base_salary * (self._bonus / 100)
            return self._base_salary + bonus_amount
        return 0


class Circle:
    """
    A class representing a circle with properties for radius, diameter, and area.

    Attributes:
    ----------
    _radius : float
        The radius of the circle.
    _area : float or None
        Cached value of the circle's area, recalculated when radius changes.
    """
    def __init__(self, radius: float):
        """
        Initialize the Circle with a given radius.

        Parameters:
        ----------
        radius : float
            The radius of the circle.
        """
        self._radius = radius  # Initialize to None
        self._area = None    # Cache for area
        # self.set_radius(radius)  # Use setter for initial validation

    def _validate_radius(self, radius: float) -> None:
        """
        Validate that the radius is positive and numeric.

        Parameters:
        ----------
        radius : float
            The radius to validate.

        Returns:
        -------
        float
            The validated radius.

        Raises:
        ------
        ValueError
            If the radius is not numeric or is not positive.
        """
        if not isinstance(radius, (int, float)):
            raise ValueError("Radius must be either int or float")
        if radius <= 0:
            raise ValueError("Radius must be positive")
        return radius

    @property
    def radius(self) -> float:
        """
        Get the radius of the circle.

        Returns:
        -------
        float
            The radius of the circle.
        """
        return self._radius

    @radius.setter
    def radius(self, radius: Union[int, float]) -> None:
        """
        Set the radius of the circle after validation.

        Parameters:
        ----------
        radius : Union[int, float]
            The new radius value.

        Raises:
        ------
        ValueError
            If the radius is invalid.
        """
        if not isinstance(radius, (int, float)):
            raise ValueError('Radius must be either int or float')
        self._radius = self._validate_radius(radius)
        self._area = None

    @property
    def diameter(self) -> float:
        """
        Compute and get the diameter of the circle.

        Returns:
        -------
        float
            The diameter of the circle.
        """
        return 2 * self._radius

    @diameter.setter
    def diameter(self, diameter: Union[int, float]) -> None:
        """
        Set the diameter of the circle and update the radius.

        Parameters:
        ----------
        diameter : Union[int, float]
            The new diameter value.

        Raises:
        ------
        ValueError
            If the diameter is invalid.
        """
        if not isinstance(diameter, (int, float)):
            raise ValueError('Diameter must be either int or float')
        self._radius = diameter / 2
        self._area = None

    @property
    def area(self) -> float:
        """
        Compute and get the cached area of the circle.

        Returns:
        -------
        float
            The area of the circle, calculated as π * radius^2.
        """
        if self._area is None:
            self._area = math.pi * self._radius ** 2
        return self._area

class Vehicle:
    """
    A class representing a generic vehicle.

    Attributes:
    ----------
    vehicle_count : int
        Class variable tracking the total number of vehicle instances.
    _manufacturer : str
        The manufacturer of the vehicle.
    _model : str
        The model of the vehicle.
    _year : int
        The manufacturing year of the vehicle.
    """
    vehicle_count = 0
    
    def __init__(self, manufacturer: str, model: str, year: int):
        """
        Initialize a new vehicle instance.

        Parameters:
        ----------
        manufacturer : str
            The manufacturer of the vehicle.
        model : str
            The model of the vehicle.
        year : int
            The manufacturing year of the vehicle.
        """
        self._manufacturer = manufacturer
        self._model = model
        self._year = year
        # Increment the vehicle count when a new instance is created
        Vehicle.vehicle_count += 1
    
    @classmethod
    def get_vehicle_count(cls) -> int:
        """
        Get the total count of vehicles.

        Returns:
        -------
        int
            The total number of vehicle instances.
        """
        return cls.vehicle_count
    
    @staticmethod
    def classify_vehicle(vehicle_type: str) -> str:
        """
        Classify the vehicle type.

        Parameters:
        ----------
        vehicle_type : str
            The type of the vehicle (e.g., 'car', 'truck', 'motorcycle').

        Returns:
        -------
        str
            A description of the vehicle type.

        Raises:
        ------
        ValueError
            If the vehicle type is invalid.
        """
        vehicle_type = vehicle_type.lower()
        valid_types = {
            "car": "This is a car",
            "truck": "This is a truck",
            "motorcycle": "This is a motorcycle"
        }
        
        if vehicle_type not in valid_types:
            raise ValueError("Invalid vehicle type. Must be 'car', 'truck', or 'motorcycle'")
        
        return valid_types[vehicle_type]


class ElectricVehicle(Vehicle):
    """
    A class representing an electric vehicle, inheriting from Vehicle.
    """
    def __init__(self, manufacturer: str, model: str, year: int):
        """
        Initialize a new electric vehicle instance.

        Parameters:
        ----------
        manufacturer : str
            The manufacturer of the electric vehicle.
        model : str
            The model of the electric vehicle.
        year : int
            The manufacturing year of the electric vehicle.
        """
        super().__init__(manufacturer, model, year)
    
    @staticmethod
    def classify_vehicle(vehicle_type: str) -> str:
        """
        Classify the type of electric vehicle.

        Parameters:
        ----------
        vehicle_type : str
            The type of the electric vehicle (e.g., 'car', 'truck', 'motorcycle').

        Returns:
        -------
        str
            A description of the electric vehicle type.

        Raises:
        ------
        ValueError
            If the vehicle type is invalid.
        """
        vehicle_type = vehicle_type.lower()
        valid_types = {
            "car": "This is an electric car",
            "truck": "This is an electric truck",
            "motorcycle": "This is an electric motorcycle"
        }
        
        if vehicle_type not in valid_types:
            raise ValueError("Invalid vehicle type. Must be 'car', 'truck', or 'motorcycle'")
        
        return valid_types[vehicle_type]



class ValidatedAttribute:
    """
    A class to manage attributes with validation for positive numeric values.

    Attributes:
        _value (Union[int, float]): The validated value.
    """

    def __init__(self, value: Union[int, float] = None) -> None:
        """Initializes the ValidatedAttribute instance."""
        self._value = None

    @property
    def value(self) -> Union[int, float]:
        """Returns the validated value."""
        return self._value

    @value.setter
    def value(self, value: Union[int, float]) -> None:
        """
        Sets the value with validation.

        Args:
            value (Union[int, float]): The new value.

        Raises:
            ValueError: If the value is invalid.
        """
        if not isinstance(value, (int, float)):
            raise ValueError('Value must be either int or float')
        if value <= 0:
            raise ValueError('Value must be positive')
        self._value = value


class DynamicClass:
    # Class-level variable
    static_value = 0
    
    # Using the descriptor for validation
    def __init__(self):
        pass

    def dynamic_attr(self, name, obj):
        """
        Dynamically sets an attribute.

        Args:
            name (str): The name of the attribute.
            obj: The value to assign.
        """
        setattr(self, name, obj)

