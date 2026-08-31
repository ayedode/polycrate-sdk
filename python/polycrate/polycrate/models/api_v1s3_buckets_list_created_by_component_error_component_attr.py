from typing import Literal

ApiV1S3BucketsListCreatedByComponentErrorComponentAttr = Literal["created_by_component"]

API_V1S3_BUCKETS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3BucketsListCreatedByComponentErrorComponentAttr
] = {
    "created_by_component",
}


def check_api_v1s3_buckets_list_created_by_component_error_component_attr(
    value: str,
) -> ApiV1S3BucketsListCreatedByComponentErrorComponentAttr:
    if value in API_V1S3_BUCKETS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_LIST_CREATED_BY_COMPONENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
