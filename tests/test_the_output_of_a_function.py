from pandera import Column, Check, DataFrameSchema, check_output
from pandas import DataFrame 



out_schema = DataFrameSchema(

    {
        "val1": Column(int, Check.in_range(-2, 3)),
        "val2": Column(int, Check.in_range(-2, 3)),
        "val3": Column(float, Check.in_range(-2, 3))
    } 

)


@check_output(out_schema)
def processing_fn(df):
    processed = df.assign(val3=df.val1/df.val2)
    return processed 


if __name__ == '__main__':
    df = DataFrame({"val1": [1, 1, -1, -2, 2], "val2": [1, 1, -1, -2, 2]})

    processing_fn(df)
