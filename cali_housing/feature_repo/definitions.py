from datetime import timedelta
from feast import Entity, FeatureView, FileSource, ValueType,  Field
from feast.types import Float32, Float64, Int64

# Declaring an entity for the dataset
house = Entity(
    name="house_id",
    value_type=ValueType.INT64,
    description="The ID of the house"
)

###################
## FEATURE SET 1 ##
###################

# Declaring the source of the first set of features
file_source1 = FileSource(
    path = "../data/df1.parquet",
    event_timestamp_column="event_timestamp"
)

# Defining the first set of features
df1_fv = FeatureView(
    name="df1_feature_view",
    ttl=timedelta(days=3),  # i.e., 3 days
    entities = [house],
    schema = [
        Field(name="MedInc", dtype=Float32),
        Field(name="HouseAge", dtype=Int64)
    ],
    source = file_source1
)



###################
## FEATURE SET 2 ##
###################

# Declaring the source of the second set of features
file_source2 = FileSource(
    path = "../data/df2.parquet",
    event_timestamp_column="event_timestamp"
)

# Defining the first set of features
df2_fv = FeatureView(
    name="df2_feature_view",
    ttl=timedelta(days=3),
    entities = [house],
    schema = [
        Field(name="AveRooms", dtype=Float32),
        Field(name="AveBedrms", dtype=Float32)
    ],
    source = file_source2
)



###################
## FEATURE SET 3 ##
###################

# Declaring the source of the third set of features
file_source3 = FileSource(
    path = "../data/df3.parquet",
    event_timestamp_column="event_timestamp"
)

# Defining the first set of features
df3_fv = FeatureView(
    name="df3_feature_view",
    ttl=timedelta(days=3),
    entities = [house],
    schema = [
        Field(name="Population", dtype=Int64),
        Field(name="AveOccup", dtype=Float32)
    ],
    source = file_source3
)


###################
## FEATURE SET 4 ##
###################

# Declaring the source of the fourth set of features
file_source4 = FileSource(
    path = "../data/df4.parquet",
    event_timestamp_column="event_timestamp"
)

# Defining the first set of features
df4_fv = FeatureView(
    name="df4_feature_view",
    ttl=timedelta(days=3),
    entities = [house],
    schema = [
        Field(name="Latitude", dtype=Int64),
        Field(name="Longitude", dtype=Float32)
    ],
    source = file_source4
)

############
## TARGET ##
############

# Declaring the source of the fourth set of features
target_source = FileSource(
    path = "../data/target_df.parquet",
    event_timestamp_column="event_timestamp"
)

# Defining the first set of features
target_fv = FeatureView(
    name="target_feature_view",
    ttl=timedelta(days=3),
    entities = [house],
    schema = [
        Field(name="target", dtype=Float32)
    ],
    source = target_source
)