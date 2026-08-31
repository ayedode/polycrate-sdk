from typing import Literal

ApiV1S3ClustersPartialUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1S3_CLUSTERS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersPartialUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1s3_clusters_partial_update_criticality_error_component_code(
    value: str,
) -> ApiV1S3ClustersPartialUpdateCriticalityErrorComponentCode:
    if value in API_V1S3_CLUSTERS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
