from typing import Literal

ApiV1S3ClustersUpdateCreatedByComponentErrorComponentCode = Literal["invalid_choice"]

API_V1S3_CLUSTERS_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersUpdateCreatedByComponentErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1s3_clusters_update_created_by_component_error_component_code(
    value: str,
) -> ApiV1S3ClustersUpdateCreatedByComponentErrorComponentCode:
    if value in API_V1S3_CLUSTERS_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_CREATED_BY_COMPONENT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
