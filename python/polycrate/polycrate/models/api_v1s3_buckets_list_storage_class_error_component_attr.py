from typing import Literal

ApiV1S3BucketsListStorageClassErrorComponentAttr = Literal["storage_class"]

API_V1S3_BUCKETS_LIST_STORAGE_CLASS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3BucketsListStorageClassErrorComponentAttr
] = {
    "storage_class",
}


def check_api_v1s3_buckets_list_storage_class_error_component_attr(
    value: str,
) -> ApiV1S3BucketsListStorageClassErrorComponentAttr:
    if value in API_V1S3_BUCKETS_LIST_STORAGE_CLASS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_LIST_STORAGE_CLASS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
