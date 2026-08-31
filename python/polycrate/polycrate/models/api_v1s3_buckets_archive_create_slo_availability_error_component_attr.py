from typing import Literal

ApiV1S3BucketsArchiveCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1S3_BUCKETS_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3BucketsArchiveCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1s3_buckets_archive_create_slo_availability_error_component_attr(
    value: str,
) -> ApiV1S3BucketsArchiveCreateSloAvailabilityErrorComponentAttr:
    if value in API_V1S3_BUCKETS_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_BUCKETS_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
