from typing import Literal

ApiV1S3BucketsObjectsUploadUrlCreateKeyErrorComponentAttr = Literal["key"]

API_V1S3_BUCKETS_OBJECTS_UPLOAD_URL_CREATE_KEY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3BucketsObjectsUploadUrlCreateKeyErrorComponentAttr
] = {
    "key",
}


def check_api_v1s3_buckets_objects_upload_url_create_key_error_component_attr(
    value: str,
) -> ApiV1S3BucketsObjectsUploadUrlCreateKeyErrorComponentAttr:
    if value in API_V1S3_BUCKETS_OBJECTS_UPLOAD_URL_CREATE_KEY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_OBJECTS_UPLOAD_URL_CREATE_KEY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
