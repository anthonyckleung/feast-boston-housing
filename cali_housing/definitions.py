from google.protobuf.duration_pb2 import Duration 
from feast import Entity, Feature, FeatureView, FileSource, ValueType

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
    path = "./data/df1.parquet",
    event_timestamp_column="event_timestamp"
)

# Defining the first set of features
df1_fv = FeatureView(
    name="df1_feature_view",
    ttl=Duration(seconds=86400 * 3),  # i.e., 3 days
    entities = ['house_id'],
    features = [
        Feature(name="MedInc", dtype=ValueType.FLOAT),
        Feature(name="HouseAge", dtype=ValueType.INT64)
    ],
    batch_source = file_source1
)



###################
## FEATURE SET 2 ##
###################

# Declaring the source of the second set of features
file_source2 = FileSource(
    path = "./data/df2.parquet",
    event_timestamp_column="event_timestamp"
)

# Defining the first set of features
df2_fv = FeatureView(
    name="df2_feature_view",
    ttl=Duration(seconds=86400 * 3),
    entities = ['house_id'],
    features = [
        Feature(name="AveRooms", dtype=ValueType.FLOAT),
        Feature(name="AveBedrms", dtype=ValueType.FLOAT)
    ],
    batch_source = file_source2
)



###################
## FEATURE SET 3 ##
###################

# Declaring the source of the third set of features
file_source3 = FileSource(
    path = "./data/df3.parquet",
    event_timestamp_column="event_timestamp"
)

# Defining the first set of features
df3_fv = FeatureView(
    name="df3_feature_view",
    ttl=Duration(seconds=86400 * 3),
    entities = ['house_id'],
    features = [
        Feature(name="Population", dtype=ValueType.INT64),
        Feature(name="AveOccup", dtype=ValueType.FLOAT)
    ],
    batch_source = file_source3
)


###################
## FEATURE SET 4 ##
###################

# Declaring the source of the fourth set of features
file_source4 = FileSource(
    path = "./data/df4.parquet",
    event_timestamp_column="event_timestamp"
)

# Defining the first set of features
df4_fv = FeatureView(
    name="df4_feature_view",
    ttl=Duration(seconds=86400 * 3),
    entities = ['house_id'],
    features = [
        Feature(name="Latitude", dtype=ValueType.INT64),
        Feature(name="Longitude", dtype=ValueType.FLOAT)
    ],
    batch_source = file_source4
)

############
## TARGET ##
############

# Declaring the source of the fourth set of features
target_source = FileSource(
    path = "./data/target_df.parquet",
    event_timestamp_column="event_timestamp"
)

# Defining the first set of features
df4_fv = FeatureView(
    name="target_feature_view",
    ttl=Duration(seconds=86400 * 3),
    entities = ['house_id'],
    features = [
        Feature(name="target", dtype=ValueType.FLOAT)
    ],
    batch_source = target_source
)