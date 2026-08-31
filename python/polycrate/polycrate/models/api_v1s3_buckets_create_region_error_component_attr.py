from typing import Literal

ApiV1S3BucketsCreateRegionErrorComponentAttr = Literal["region"]

API_V1S3_BUCKETS_CREATE_REGION_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1S3BucketsCreateRegionErrorComponentAttr] = {
    "region",
}


def check_api_v1s3_buckets_create_region_error_component_attr(
    value: str,
) -> ApiV1S3BucketsCreateRegionErrorComponentAttr:
    if value in API_V1S3_BUCKETS_CREATE_REGION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_CREATE_REGION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
