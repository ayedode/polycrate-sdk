from typing import Literal

S3BucketRegionResponseState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

S3_BUCKET_REGION_RESPONSE_STATE_VALUES: set[S3BucketRegionResponseState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_s3_bucket_region_response_state(value: str) -> S3BucketRegionResponseState:
    if value in S3_BUCKET_REGION_RESPONSE_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {S3_BUCKET_REGION_RESPONSE_STATE_VALUES!r}")
