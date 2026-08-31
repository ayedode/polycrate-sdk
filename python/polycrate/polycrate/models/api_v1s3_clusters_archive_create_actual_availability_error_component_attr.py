from typing import Literal

ApiV1S3ClustersArchiveCreateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersArchiveCreateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1s3_clusters_archive_create_actual_availability_error_component_attr(
    value: str,
) -> ApiV1S3ClustersArchiveCreateActualAvailabilityErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
