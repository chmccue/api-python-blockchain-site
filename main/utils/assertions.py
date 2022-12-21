from assertpy import assert_that


class CustomAsserts:

    @staticmethod
    def value_is_greater_than_0(value):
        assert_that(value, description="value must be greater than 0").is_greater_than(0)

    @staticmethod
    def value_equals(value1, value2):
        assert_that(value1 == value2, description="values expected to match")

    @staticmethod
    def value_greater_than(value1, value2):
        assert_that(value1 > value2, description="value1 expected to be greater than value2")
