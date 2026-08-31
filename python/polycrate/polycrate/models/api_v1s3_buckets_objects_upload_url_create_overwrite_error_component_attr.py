from typing import Literal

ApiV1S3BucketsObjectsUploadUrlCreateOverwriteErrorComponentAttr = Literal["overwrite"]

API_V1S3_BUCKETS_OBJECTS_UPLOAD_URL_CREATE_OVERWRITE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3BucketsObjectsUploadUrlCreateOverwriteErrorComponentAttr
] = {
    "overwrite",
}


def check_api_v1s3_buckets_objects_upload_url_create_overwrite_error_component_attr(
    value: str,
) -> ApiV1S3BucketsObjectsUploadUrlCreateOverwriteErrorComponentAttr:
    if value in API_V1S3_BUCKETS_OBJECTS_UPLOAD_URL_CREATE_OVERWRITE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_OBJECTS_UPLOAD_URL_CREATE_OVERWRITE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
