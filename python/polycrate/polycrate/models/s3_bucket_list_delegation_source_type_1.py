from typing import Literal

S3BucketListDelegationSourceType1 = Literal["loopback_lb", "loopback_object_store"]

S3_BUCKET_LIST_DELEGATION_SOURCE_TYPE_1_VALUES: set[S3BucketListDelegationSourceType1] = {
    "loopback_lb",
    "loopback_object_store",
}


def check_s3_bucket_list_delegation_source_type_1(value: str) -> S3BucketListDelegationSourceType1:
    if value in S3_BUCKET_LIST_DELEGATION_SOURCE_TYPE_1_VALUES:
        return value
    raise TypeError(f"Unexpected value {value!r}. Expected one of {S3_BUCKET_LIST_DELEGATION_SOURCE_TYPE_1_VALUES!r}")
