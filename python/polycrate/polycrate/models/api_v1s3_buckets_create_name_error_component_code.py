from typing import Literal

ApiV1S3BucketsCreateNameErrorComponentCode = Literal[
    "blank", "invalid", "null", "null_characters_not_allowed", "required", "surrogate_characters_not_allowed"
]

API_V1S3_BUCKETS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES: set[ApiV1S3BucketsCreateNameErrorComponentCode] = {
    "blank",
    "invalid",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1s3_buckets_create_name_error_component_code(value: str) -> ApiV1S3BucketsCreateNameErrorComponentCode:
    if value in API_V1S3_BUCKETS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_CREATE_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
