from typing import Literal

ApiV1S3ClustersCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1S3_CLUSTERS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1s3_clusters_create_criticality_error_component_code(
    value: str,
) -> ApiV1S3ClustersCreateCriticalityErrorComponentCode:
    if value in API_V1S3_CLUSTERS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
