from typing import Literal

ApiV1S3BucketsObjectsFolderCreatePrefixErrorComponentAttr = Literal["prefix"]

API_V1S3_BUCKETS_OBJECTS_FOLDER_CREATE_PREFIX_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3BucketsObjectsFolderCreatePrefixErrorComponentAttr
] = {
    "prefix",
}


def check_api_v1s3_buckets_objects_folder_create_prefix_error_component_attr(
    value: str,
) -> ApiV1S3BucketsObjectsFolderCreatePrefixErrorComponentAttr:
    if value in API_V1S3_BUCKETS_OBJECTS_FOLDER_CREATE_PREFIX_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_OBJECTS_FOLDER_CREATE_PREFIX_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
