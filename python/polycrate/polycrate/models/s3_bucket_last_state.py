from typing import Literal

S3BucketLastState = Literal["CRITICAL", "DEGRADED", "DOWN", "OK", "READY", "WARNING"]

S3_BUCKET_LAST_STATE_VALUES: set[S3BucketLastState] = {
    "CRITICAL",
    "DEGRADED",
    "DOWN",
    "OK",
    "READY",
    "WARNING",
}


def check_s3_bucket_last_state(value: str) -> S3BucketLastState:
    if value in S3_BUCKET_LAST_STATE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {S3_BUCKET_LAST_STATE_VALUES!r}")
