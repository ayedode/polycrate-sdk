from typing import Literal

S3BucketRequestCriticalityType2Type1 = Literal["", "high", "low", "medium"]

S3_BUCKET_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES: set[S3BucketRequestCriticalityType2Type1] = {
    "",
    "high",
    "low",
    "medium",
}


def check_s3_bucket_request_criticality_type_2_type_1(value: str) -> S3BucketRequestCriticalityType2Type1:
    if value in S3_BUCKET_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {S3_BUCKET_REQUEST_CRITICALITY_TYPE_2_TYPE_1_VALUES!r}"
    )
