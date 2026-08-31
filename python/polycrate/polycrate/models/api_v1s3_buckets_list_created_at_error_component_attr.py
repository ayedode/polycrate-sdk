from typing import Literal

ApiV1S3BucketsListCreatedAtErrorComponentAttr = Literal["created_at"]

API_V1S3_BUCKETS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3BucketsListCreatedAtErrorComponentAttr] = {
    "created_at",
}


def check_api_v1s3_buckets_list_created_at_error_component_attr(
    value: str,
) -> ApiV1S3BucketsListCreatedAtErrorComponentAttr:
    if value in API_V1S3_BUCKETS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_LIST_CREATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
