import pandas as pd
from feast import FeatureStore 
from feast.infra.offline_stores.file_source import SavedDatasetFileStorage

# Getting our FeatureStore
store = FeatureStore(repo_path=".")

# Read targets as an entity DataFrame
entity_df = pd.read_parquet(path="../data/target_df.parquet")


feature_list = [
    "df1_feature_view:MedInc",
    "df1_feature_view:HouseAge",
    "df2_feature_view:AveRooms",
    "df2_feature_view:AveBedrms",
    "df3_feature_view:Population",
    "df3_feature_view:AveOccup",
    "df4_feature_view:Latitude",
    "df4_feature_view:Longitude"
]


# Get historical features and join with entity_df
training_df = store.get_historical_features(
    entity_df=entity_df,
    features=feature_list
).to_df()

print("---- FEATURE SCHEMA ----\n")
print(training_df.info())

print()
print("---- EXAMPLE FEATURES ----\n")
print(training_df.tail())