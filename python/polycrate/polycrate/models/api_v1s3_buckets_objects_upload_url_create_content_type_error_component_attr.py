from typing import Literal

ApiV1S3BucketsObjectsUploadUrlCreateContentTypeErrorComponentAttr = Literal["content_type"]

API_V1S3_BUCKETS_OBJECTS_UPLOAD_URL_CREATE_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3BucketsObjectsUploadUrlCreateContentTypeErrorComponentAttr
] = {
    "content_type",
}


def check_api_v1s3_buckets_objects_upload_url_create_content_type_error_component_attr(
    value: str,
) -> ApiV1S3BucketsObjectsUploadUrlCreateContentTypeErrorComponentAttr:
    if value in API_V1S3_BUCKETS_OBJECTS_UPLOAD_URL_CREATE_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_OBJECTS_UPLOAD_URL_CREATE_CONTENT_TYPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
