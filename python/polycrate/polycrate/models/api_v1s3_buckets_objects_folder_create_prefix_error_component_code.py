from typing import Literal

ApiV1S3BucketsObjectsFolderCreatePrefixErrorComponentCode = Literal[
    "blank", "invalid", "null", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1S3_BUCKETS_OBJECTS_FOLDER_CREATE_PREFIX_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3BucketsObjectsFolderCreatePrefixErrorComponentCode
] = {
    "blank",
    "invalid",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1s3_buckets_objects_folder_create_prefix_error_component_code(
    value: str,
) -> ApiV1S3BucketsObjectsFolderCreatePrefixErrorComponentCode:
    if value in API_V1S3_BUCKETS_OBJECTS_FOLDER_CREATE_PREFIX_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_OBJECTS_FOLDER_CREATE_PREFIX_ERROR_COMPONENT_CODE_VALUES!r}"
    )
