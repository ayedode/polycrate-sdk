from typing import Literal

S3BucketVersioningRequestStatusEnum = Literal["Enabled", "Suspended"]

S3_BUCKET_VERSIONING_REQUEST_STATUS_ENUM_VALUES: set[S3BucketVersioningRequestStatusEnum] = {
    "Enabled",
    "Suspended",
}


def check_s3_bucket_versioning_request_status_enum(value: str) -> S3BucketVersioningRequestStatusEnum:
    if value in S3_BUCKET_VERSIONING_REQUEST_STATUS_ENUM_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {S3_BUCKET_VERSIONING_REQUEST_STATUS_ENUM_VALUES!r}")
