from typing import Literal

ApiV1S3BucketsListSearchErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1S3_BUCKETS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES: set[ApiV1S3BucketsListSearchErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1s3_buckets_list_search_error_component_code(value: str) -> ApiV1S3BucketsListSearchErrorComponentCode:
    if value in API_V1S3_BUCKETS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES!r}"
    )
