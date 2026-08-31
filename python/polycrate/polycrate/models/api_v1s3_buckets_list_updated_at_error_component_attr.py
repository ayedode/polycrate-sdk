from typing import Literal

ApiV1S3BucketsListUpdatedAtErrorComponentAttr = Literal["updated_at"]

API_V1S3_BUCKETS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3BucketsListUpdatedAtErrorComponentAttr] = {
    "updated_at",
}


def check_api_v1s3_buckets_list_updated_at_error_component_attr(
    value: str,
) -> ApiV1S3BucketsListUpdatedAtErrorComponentAttr:
    if value in API_V1S3_BUCKETS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_LIST_UPDATED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
