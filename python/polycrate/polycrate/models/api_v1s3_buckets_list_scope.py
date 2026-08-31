from typing import Literal

ApiV1S3BucketsListScope = Literal["system", "user"]

API_V1S3_BUCKETS_LIST_SCOPE_VALUES: set[ApiV1S3BucketsListScope] = {
    "system",
    "user",
}


def check_api_v1s3_buckets_list_scope(value: str) -> ApiV1S3BucketsListScope:
    if value in API_V1S3_BUCKETS_LIST_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_LIST_SCOPE_VALUES!r}")
