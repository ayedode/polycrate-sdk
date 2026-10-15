from typing import Literal

S3BucketVersioningStatus = Literal["enabled", "Enabled", "off", "suspended", "Suspended"]

S3_BUCKET_VERSIONING_STATUS_VALUES: set[S3BucketVersioningStatus] = {
    "enabled",
    "Enabled",
    "off",
    "suspended",
    "Suspended",
}


def check_s3_bucket_versioning_status(value: str) -> S3BucketVersioningStatus:
    if value in S3_BUCKET_VERSIONING_STATUS_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {S3_BUCKET_VERSIONING_STATUS_VALUES!r}")
