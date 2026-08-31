from typing import Literal

ApiV1S3ClustersUpdateEndpointSecureErrorComponentCode = Literal["invalid", "null"]

API_V1S3_CLUSTERS_UPDATE_ENDPOINT_SECURE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersUpdateEndpointSecureErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1s3_clusters_update_endpoint_secure_error_component_code(
    value: str,
) -> ApiV1S3ClustersUpdateEndpointSecureErrorComponentCode:
    if value in API_V1S3_CLUSTERS_UPDATE_ENDPOINT_SECURE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_ENDPOINT_SECURE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
