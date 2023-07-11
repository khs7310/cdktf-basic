class alb_controller:
    def __str__(self):
        return "alb_controller object"

# Create a dictionary and add an instance of alb_controller
my_dict = {}
my_dict["a"] = alb_controller()

# Access the instance and get its string representation
obj_name = str(my_dict["a"])
print(obj_name)  # Output: alb_controller object