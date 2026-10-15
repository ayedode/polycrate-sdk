from typing import Literal

S3BucketVersioningRequestRequestStatus = Literal["Enabled", "Suspended"]

S3_BUCKET_VERSIONING_REQUEST_REQUEST_STATUS_VALUES: set[S3BucketVersioningRequestRequestStatus] = {
    "Enabled",
    "Suspended",
}


def check_s3_bucket_versioning_request_request_status(value: str) -> S3BucketVersioningRequestRequestStatus:
    if value in S3_BUCKET_VERSIONING_REQUEST_REQUEST_STATUS_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {S3_BUCKET_VERSIONING_REQUEST_REQUEST_STATUS_VALUES!r}"
    )
