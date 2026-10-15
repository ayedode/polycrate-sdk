from typing import Literal

S3BucketState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

S3_BUCKET_STATE_VALUES: set[S3BucketState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_s3_bucket_state(value: str) -> S3BucketState:
    if value in S3_BUCKET_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {S3_BUCKET_STATE_VALUES!r}")
