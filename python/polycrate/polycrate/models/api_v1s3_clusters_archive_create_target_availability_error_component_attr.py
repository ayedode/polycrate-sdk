from typing import Literal

ApiV1S3ClustersArchiveCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersArchiveCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1s3_clusters_archive_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1S3ClustersArchiveCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
