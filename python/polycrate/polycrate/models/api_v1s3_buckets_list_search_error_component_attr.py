from typing import Literal

ApiV1S3BucketsListSearchErrorComponentAttr = Literal["search"]

API_V1S3_BUCKETS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3BucketsListSearchErrorComponentAttr] = {
    "search",
}


def check_api_v1s3_buckets_list_search_error_component_attr(value: str) -> ApiV1S3BucketsListSearchErrorComponentAttr:
    if value in API_V1S3_BUCKETS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_LIST_SEARCH_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
