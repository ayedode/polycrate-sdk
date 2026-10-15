from typing import Literal

S3BucketRequestKind = Literal["generic"]

S3_BUCKET_REQUEST_KIND_VALUES: set[S3BucketRequestKind] = {
    "generic",
}


def check_s3_bucket_request_kind(value: str) -> S3BucketRequestKind:
    if value in S3_BUCKET_REQUEST_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {S3_BUCKET_REQUEST_KIND_VALUES!r}")
