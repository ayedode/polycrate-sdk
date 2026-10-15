from typing import Literal

S3BucketScope = Literal["system", "user"]

S3_BUCKET_SCOPE_VALUES: set[S3BucketScope] = {
    "system",
    "user",
}


def check_s3_bucket_scope(value: str) -> S3BucketScope:
    if value in S3_BUCKET_SCOPE_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {S3_BUCKET_SCOPE_VALUES!r}")
