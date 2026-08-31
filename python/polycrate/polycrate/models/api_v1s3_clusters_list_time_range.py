from typing import Literal

ApiV1S3ClustersListTimeRange = Literal["12h", "1h", "24h", "30d", "6h", "7d", "90d"]

API_V1S3_CLUSTERS_LIST_TIME_RANGE_VALUES: set[ApiV1S3ClustersListTimeRange] = {
    "12h",
    "1h",
    "24h",
    "30d",
    "6h",
    "7d",
    "90d",
}


def check_api_v1s3_clusters_list_time_range(value: str) -> ApiV1S3ClustersListTimeRange:
    if value in API_V1S3_CLUSTERS_LIST_TIME_RANGE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_LIST_TIME_RANGE_VALUES!r}")
