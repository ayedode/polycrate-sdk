from typing import Literal

ApiV1S3ClustersPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1S3_CLUSTERS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1s3_clusters_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1S3ClustersPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
