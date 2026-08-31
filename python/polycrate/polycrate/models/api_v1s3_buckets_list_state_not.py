from typing import Literal

ApiV1S3BucketsListStateNot = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

API_V1S3_BUCKETS_LIST_STATE_NOT_VALUES: set[ApiV1S3BucketsListStateNot] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_api_v1s3_buckets_list_state_not(value: str) -> ApiV1S3BucketsListStateNot:
    if value in API_V1S3_BUCKETS_LIST_STATE_NOT_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_LIST_STATE_NOT_VALUES!r}")
