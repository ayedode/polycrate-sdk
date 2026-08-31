from typing import Literal

ApiV1S3BucketsObjectsUploadUrlCreateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1S3_BUCKETS_OBJECTS_UPLOAD_URL_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3BucketsObjectsUploadUrlCreateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1s3_buckets_objects_upload_url_create_non_field_errors_error_component_code(
    value: str,
) -> ApiV1S3BucketsObjectsUploadUrlCreateNonFieldErrorsErrorComponentCode:
    if value in API_V1S3_BUCKETS_OBJECTS_UPLOAD_URL_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_OBJECTS_UPLOAD_URL_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
