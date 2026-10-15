from typing import Literal

S3BucketCriticalityType1 = Literal["", "high", "low", "medium"]

S3_BUCKET_CRITICALITY_TYPE_1_VALUES: set[S3BucketCriticalityType1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_s3_bucket_criticality_type_1(value: str) -> S3BucketCriticalityType1:
    if value in S3_BUCKET_CRITICALITY_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {S3_BUCKET_CRITICALITY_TYPE_1_VALUES!r}")
