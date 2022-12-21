from assertpy import assert_that, soft_assertions
from cerberus import Validator


class SchemaValidators:

    @staticmethod
    def one_dataset_has_expected_schema(schema, dataset):
        validator = Validator(schema, require_all=True)
        schema_check_valid = validator.validate(dataset)
        assert_that(schema_check_valid, description=validator.errors).is_true()

    @staticmethod
    def all_datasets_have_expected_schema(schema, datasets, nested_data=True):
        validator = Validator(schema, require_all=True)
        with soft_assertions():
            for dataset in datasets:
                if nested_data:
                    schema_check_valid = validator.validate(datasets[dataset])
                else:
                    schema_check_valid = validator.validate(dataset)
                assert_that(schema_check_valid, description=validator.errors).is_true()
