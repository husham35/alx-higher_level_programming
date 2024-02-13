#!/usr/bin/python3
"""Base class to handle"""

import json
from pathlib import Path
import csv
import turtle


class Base:
    """
    Base class definition
    Attributes:
        __nb_objects (int): number of objects instantiated by this class `Base`
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes the Base class
        Args:
            id (int): id of the objects of this class
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        serialize a list of dictionaries to JSON string
        Args:
            list_dictionaries: (list) list of dictionaries
        Returns:
            JSON string of the list of dictionaries
        """
        return json.dumps(list_dictionaries) if list_dictionaries else []

    @staticmethod
    def from_json_string(json_string):
        """
        deserialize JSON string from object
        Args:
            json_string: json string of the object to deserialize
        Returns: an object
        """
        return json.loads(json_string) if json_string else []

    @classmethod
    def save_to_file(cls, list_objs):
        """
        saves to file the JSON representation of `list_objs`
        Args:
            list_objs: (list) list of object to be written
        Returns: nothing
        """
        # filename = "{}.json".format(cls.__name__)
        # with open(filename, mode="w", encoding="utf-8") as json_file:
        #     if not list_objs:
        #         json_file.write(cls.to_json_string([]))
        #     else:
        #         dict_objs = [obj.to_dictionary() for obj in list_objs]
        #         json_file.write(cls.to_json_string(dict_objs))
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o.to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @classmethod
    def create(cls, **dictionary):
        """
        creates a new instance of the Base class with all attributes
        Args:
            **dictionary: (dict) dictionary of args to be used to
            create object
        Returns: an instance of this class to be inherited
        """
        dummy = None
        if cls.__name__ == "Rectangle":
            dummy = cls(8, 4)

        if cls.__name__ == "Square":
            dummy = cls(7)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        reads JSON file and creates an instance of the data read.
        Returns: a list of the data read from the JSON file
        """
        filename = "{}.json".format(cls.__name__)
        if not Path(filename).is_file():
            return []

        with open(filename, mode="r", encoding="utf-8") as json_file:
            instances = cls.from_json_string(json_file.read())

        return [cls.create(**instance) for instance in instances]

    @classmethod
    def save_from_file_csv(cls, list_objs):
        """
        saves serialized list of objects to a CSV file
        Args:
            list_objs: (list) list of objects to be saved to a CSV file
        Returns: nothing
        """
        filename = "{}.csv".format(cls.__name__)
        with open(filename, mode="w", encoding="utf-8") as csv_file:
            if cls.__name__ == "Rectangle":
                columns = ["id", "width", "height", "x", "y"]
            else:
                columns = ["id", "size", "x", "y"]

            writer = csv.DictWriter(csv_file, columns)
            writer.writerows([obj.to_dictionary() for obj in list_objs])

    @classmethod
    def load_from_file_csv(cls):
        """
        loads serialized list of objects from a CSV file
        Returns: list of objects read from the CSV file
        """
        filename = "{}.csv".format(cls.__name__)
        if not Path(filename).is_file():
            return []

        with open(filename, mode="r", encoding="utf-8") as csv_file:
            if cls.__name__ == "Rectangle":
                columns = ["id", "width", "height", "x", "y"]
            else:
                columns = ["id", "size", "x", "y"]

            reader = csv.DictReader(csv_file, columns)
            reader = [
                {key: int(value) for key, value in row.items()}
                for row in reader
            ]
            return [cls.create(**args) for args in reader]

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Draws rectangles and squares graphically on screen.
        Args:
            list_rectangles: a list or rectangles
            list_squares: a list of squares
        """
        with turtle.Screen() as screen:
            screen.setup(1200, 720)
            t_obj = turtle.Turtle()

            total_height = 0

            if list_rectangles:
                rec_width = list_rectangles[0].width * 2
                rec_height = list_rectangles[0].height * 2
                t_obj.begin_fill()
                t_obj.color("pink", "purple")
                t_obj.forward(rec_width)
                t_obj.left(90)
                t_obj.forward(rec_height)
                t_obj.left(90)
                t_obj.forward(rec_width)
                t_obj.left(90)
                t_obj.forward(rec_height)
                t_obj.end_fill()
                total_height += rec_height

            if len(list_rectangles) > 1:
                for rec in list_rectangles[1:]:
                    rec_h = rec.height * 2
                    rec_w = rec.width * 2
                    t_obj.forward(rec_h)
                    t_obj.left(90)

                    t_obj.begin_fill()
                    t_obj.color("pink", "purple")
                    t_obj.forward(rec_w)
                    t_obj.left(90)
                    t_obj.forward(rec_h)
                    t_obj.left(90)
                    t_obj.forward(rec_w)
                    t_obj.left(90)
                    t_obj.forward(rec_h)
                    t_obj.end_fill()
                    total_height += rec_h

            for sqr in list_squares:
                sqr_size = sqr.width * 2
                t_obj.right(180)
                t_obj.forward(total_height)
                t_obj.left(90)
                t_obj.forward(50)

                t_obj.begin_fill()
                t_obj.color("#39E745", "#39E745")
                for _ in range(4):
                    t_obj.forward(sqr_size)
                    t_obj.left(90)
                t_obj.end_fill()

            turtle.done()
