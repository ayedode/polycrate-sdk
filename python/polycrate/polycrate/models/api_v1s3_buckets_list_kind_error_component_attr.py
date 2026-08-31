from typing import Literal

ApiV1S3BucketsListKindErrorComponentAttr = Literal["kind"]

API_V1S3_BUCKETS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3BucketsListKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1s3_buckets_list_kind_error_component_attr(value: str) -> ApiV1S3BucketsListKindErrorComponentAttr:
    if value in API_V1S3_BUCKETS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
