from typing import Literal

ApiV1S3BucketsUpdateAnnotationsErrorComponentAttr = Literal["annotations"]

API_V1S3_BUCKETS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3BucketsUpdateAnnotationsErrorComponentAttr
] = {
    "annotations",
}


def check_api_v1s3_buckets_update_annotations_error_component_attr(
    value: str,
) -> ApiV1S3BucketsUpdateAnnotationsErrorComponentAttr:
    if value in API_V1S3_BUCKETS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_UPDATE_ANNOTATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
