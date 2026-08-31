from typing import Literal

ApiV1S3ClustersCreateActiveErrorComponentCode = Literal["invalid", "null"]

API_V1S3_CLUSTERS_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES: set[ApiV1S3ClustersCreateActiveErrorComponentCode] = {
    "invalid",
    "null",
}


def check_api_v1s3_clusters_create_active_error_component_code(
    value: str,
) -> ApiV1S3ClustersCreateActiveErrorComponentCode:
    if value in API_V1S3_CLUSTERS_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_ACTIVE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
