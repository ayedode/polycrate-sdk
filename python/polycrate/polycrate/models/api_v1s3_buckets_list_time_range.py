from typing import Literal

ApiV1S3BucketsListTimeRange = Literal["12h", "1h", "24h", "30d", "6h", "7d", "90d"]

API_V1S3_BUCKETS_LIST_TIME_RANGE_VALUES: set[ApiV1S3BucketsListTimeRange] = {
    "12h",
    "1h",
    "24h",
    "30d",
    "6h",
    "7d",
    "90d",
}


def check_api_v1s3_buckets_list_time_range(value: str) -> ApiV1S3BucketsListTimeRange:
    if value in API_V1S3_BUCKETS_LIST_TIME_RANGE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_LIST_TIME_RANGE_VALUES!r}")
