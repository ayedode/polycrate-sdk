from typing import Literal

ApiV1S3BucketsListStorageClassErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1S3_BUCKETS_LIST_STORAGE_CLASS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3BucketsListStorageClassErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1s3_buckets_list_storage_class_error_component_code(
    value: str,
) -> ApiV1S3BucketsListStorageClassErrorComponentCode:
    if value in API_V1S3_BUCKETS_LIST_STORAGE_CLASS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_LIST_STORAGE_CLASS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
