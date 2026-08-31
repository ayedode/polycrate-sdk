from typing import Literal

ApiV1S3BucketsObjectsUploadUrlCreateContentTypeErrorComponentCode = Literal[
    "blank", "invalid", "null", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1S3_BUCKETS_OBJECTS_UPLOAD_URL_CREATE_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3BucketsObjectsUploadUrlCreateContentTypeErrorComponentCode
] = {
    "blank",
    "invalid",
    "null",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1s3_buckets_objects_upload_url_create_content_type_error_component_code(
    value: str,
) -> ApiV1S3BucketsObjectsUploadUrlCreateContentTypeErrorComponentCode:
    if value in API_V1S3_BUCKETS_OBJECTS_UPLOAD_URL_CREATE_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_OBJECTS_UPLOAD_URL_CREATE_CONTENT_TYPE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
