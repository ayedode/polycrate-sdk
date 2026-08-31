from typing import Literal

ApiV1S3ClustersCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1S3_CLUSTERS_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1s3_clusters_create_slo_availability_error_component_attr(
    value: str,
) -> ApiV1S3ClustersCreateSloAvailabilityErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
