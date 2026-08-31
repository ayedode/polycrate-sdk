from typing import Literal

ApiV1S3ClustersCreateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1S3_CLUSTERS_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersCreateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1s3_clusters_create_actual_availability_error_component_attr(
    value: str,
) -> ApiV1S3ClustersCreateActualAvailabilityErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
