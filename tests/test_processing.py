from pandas import DataFrame 
from pandas.testing import assert_frame_equal 
from pandera import DataFrameSchema, Column, Check, check_output
import pytest
import hypothesis


# validation schema for input data
schema = DataFrameSchema(
    {
        "val1": Column(int, Check.in_range(-2, 3)),
        "val2": Column(int, Check.in_range(-2, 3)),
    }
)

# validation schema for the output data
out_schema = DataFrameSchema(

    # validate the val3 attribute
    {
        "val3": Column(float, Check.in_range(-2, 3))
    }
)


# the check_output function validates the output of the function
# against out_schema
@check_output(out_schema)
def processing_fn(df):
    processed = df.assign(val3=df.val1/df.val2)

    return processed



# def test_processing_fn():
# 
#     # Create some test data 
#     df = DataFrame({"val1": [1, 1, -1, -2, 2], "val2": [1, 2, -2, -1, 2]})
# 
#     # use the function 
#     result = processing_fn(df)
# 
# 
#     # create the expected output 
#     expected = df.copy()
#     expected["val3"] = [1, 0.5, 0.5, 2, 1]
# 
# 
#     # Test 
#     # Test passes but you'd like to run this with a variety 
#     # of examples
#     assert_frame_equal(result, expected, check_dtype=False)
# 


# Use hypothesis to test your function against a variety of inputs
@hypothesis.given(schema.strategy(size=5))
def test_processing_fn(dataframe):
    processing_fn(dataframe)
  
