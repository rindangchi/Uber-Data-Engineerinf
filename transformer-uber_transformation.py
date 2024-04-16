import pandas as pd
if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    # Specify your transformation logic here
    df = df.drop_duplicates().reset_index(drop=True)
    df['trip_id'] = df.index


    
    df['tpep_pickup_datetime'] = pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime'] = pd.to_datetime(df['tpep_dropoff_datetime'])

    #create date_time dimension table
    date_time_dim = df[['tpep_pickup_datetime','tpep_dropoff_datetime']].reset_index(drop=True)

    #create all columns for date_time dim table
    date_time_dim['tpep_pickup_datetime'] = date_time_dim['tpep_pickup_datetime']
    date_time_dim['pick_hour'] = date_time_dim['tpep_pickup_datetime'].dt.hour
    date_time_dim['pick_day'] = date_time_dim['tpep_pickup_datetime'].dt.day
    date_time_dim['pick_month'] = date_time_dim['tpep_pickup_datetime'].dt.month
    date_time_dim['pick_year'] = date_time_dim['tpep_pickup_datetime'].dt.year
    date_time_dim['pick_weekday'] = date_time_dim['tpep_pickup_datetime'].dt.weekday

    date_time_dim['tpep_dropoff_datetime'] = date_time_dim['tpep_dropoff_datetime']
    date_time_dim['drop_hour'] = date_time_dim['tpep_dropoff_datetime'].dt.hour
    date_time_dim['drop_day'] = date_time_dim['tpep_dropoff_datetime'].dt.day
    date_time_dim['drop_month'] = date_time_dim['tpep_dropoff_datetime'].dt.month
    date_time_dim['drop_year'] = date_time_dim['tpep_dropoff_datetime'].dt.year
    date_time_dim['drop_weekday'] = date_time_dim['tpep_dropoff_datetime'].dt.weekday

    #define primary key for date_time dim table
    date_time_dim['datetime_id'] = date_time_dim.index

    #arrange the columns to the correct order
    date_time_dim = date_time_dim[['datetime_id', 'tpep_pickup_datetime', 'pick_hour', 'pick_day','pick_month','pick_year', 'pick_weekday',
                                'tpep_dropoff_datetime', 'drop_hour', 'drop_day', 'drop_month', 'drop_year', 'drop_weekday']]

    #create passanger count dimension table
    passenger_count_dim = df[['passenger_count']].reset_index(drop=True)
    passenger_count_dim['passenger_count_id'] = passenger_count_dim.index
    passenger_count_dim = passenger_count_dim[['passenger_count_id', 'passenger_count']]

    #create trip distance dimension table
    trip_distance_dim = df[['trip_distance']].reset_index(drop=True)
    trip_distance_dim['trip_distance_id'] = trip_distance_dim.index
    trip_distance_dim = trip_distance_dim[['trip_distance_id', 'trip_distance']]

    rate_code_type = {
        1 : "Standard Rate",
        2 : "JKF",
        3 : "Newark",
        4 : "Nassau or Westchester",
        5 : "Negotiated fare",
        6 : "Group rate"
    }

    rate_code_dim = df[['RatecodeID']].reset_index(drop=True)
    rate_code_dim['rate_code_id'] = rate_code_dim.index
    rate_code_dim['rate_code_name'] = rate_code_dim['RatecodeID'].map(rate_code_type)
    rate_code_dim = rate_code_dim[['rate_code_id', 'RatecodeID', 'rate_code_name']]

    #pickup location dimension

    pickup_location_dim = df[['pickup_longitude', 'pickup_latitude']].reset_index(drop=True)
    pickup_location_dim['pickup_location_id'] = pickup_location_dim.index
    pickup_location_dim = pickup_location_dim[['pickup_location_id', 'pickup_latitude', 'pickup_longitude']]

    #drop_off location dimension

    dropoff_location_dim = df[['dropoff_longitude', 'dropoff_latitude']].reset_index(drop=True)
    dropoff_location_dim['dropoff_location_id'] = dropoff_location_dim.index
    dropoff_location_dim = dropoff_location_dim[['dropoff_location_id', 'dropoff_latitude', 'dropoff_longitude']]

    #payment type dimension table
    payment_type_name = {
        1: "Credit Card",
        2: "Cash",
        3: "No Charge",
        4: "Dispute",
        5: "Unknown",
        6: "Voided trip"
    }

    payment_type_dim = df[['payment_type']].reset_index(drop=True)
    payment_type_dim['payment_type_id'] = payment_type_dim.index
    payment_type_dim['payment_type_name'] = payment_type_dim['payment_type'].map(payment_type_name)
    payment_type_dim = payment_type_dim[['payment_type_id', 'payment_type', 'payment_type_name']]

        #create fact table 
    fact_table = df.merge(passenger_count_dim, left_on='trip_id', right_on='passenger_count_id') \
                .merge(trip_distance_dim, left_on='trip_id', right_on='trip_distance_id')\
                .merge(rate_code_dim, left_on='trip_id', right_on='rate_code_id')\
                .merge(pickup_location_dim, left_on='trip_id', right_on='pickup_location_id')\
                .merge(dropoff_location_dim, left_on='trip_id', right_on='dropoff_location_id')\
                .merge(date_time_dim, left_on='trip_id', right_on='datetime_id')\
                .merge(payment_type_dim, left_on='trip_id', right_on='payment_type_id')\
                [['trip_id', 'VendorID', 'datetime_id', 'passenger_count_id', 'trip_distance_id', 'rate_code_id', 'store_and_fwd_flag',
                'pickup_location_id', 'dropoff_location_id', 'payment_type_id', 'fare_amount', 'extra', 'mta_tax', 'tip_amount', 'tolls_amount',
                'improvement_surcharge', 'total_amount'
                ]]

 
    return {"date_time_dim" : date_time_dim.to_dict(orient="dict"),
    "trip_distance_dim" : trip_distance_dim.to_dict(orient="dict"),
    "passenger_count_dim" : passenger_count_dim.to_dict(orient="dict"),
    "rate_code_dim" : rate_code_dim.to_dict(orient="dict"),
    "pickup_location_dim" : pickup_location_dim.to_dict(orient="dict"),
    "dropoff_location_dim" : dropoff_location_dim.to_dict(orient="dict"),
    "payment_type_dim" : payment_type_dim.to_dict(orient="dict"),
    "fact_table" :  fact_table.to_dict(orient="dict")
    }


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
