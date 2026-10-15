from typing import Literal

S3BucketKind = Literal["generic"]

S3_BUCKET_KIND_VALUES: set[S3BucketKind] = {
    "generic",
}


def check_s3_bucket_kind(value: str) -> S3BucketKind:
    if value in S3_BUCKET_KIND_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {S3_BUCKET_KIND_VALUES!r}")
