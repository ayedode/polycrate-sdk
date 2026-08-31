from typing import Literal

ApiV1S3BucketsUpdateAnnotationsErrorComponentCode = Literal["invalid"]

API_V1S3_BUCKETS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3BucketsUpdateAnnotationsErrorComponentCode
] = {
    "invalid",
}


def check_api_v1s3_buckets_update_annotations_error_component_code(
    value: str,
) -> ApiV1S3BucketsUpdateAnnotationsErrorComponentCode:
    if value in API_V1S3_BUCKETS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
