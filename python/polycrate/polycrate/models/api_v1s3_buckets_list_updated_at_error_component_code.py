from typing import Literal

ApiV1S3BucketsListUpdatedAtErrorComponentCode = Literal["invalid"]

API_V1S3_BUCKETS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES: set[ApiV1S3BucketsListUpdatedAtErrorComponentCode] = {
    "invalid",
}


def check_api_v1s3_buckets_list_updated_at_error_component_code(
    value: str,
) -> ApiV1S3BucketsListUpdatedAtErrorComponentCode:
    if value in API_V1S3_BUCKETS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
