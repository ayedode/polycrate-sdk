from typing import Literal

ApiV1S3ClustersArchiveCreateAdminEndpointSecureErrorComponentCode = Literal["invalid", "null"]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_ADMIN_ENDPOINT_SECURE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1S3ClustersArchiveCreateAdminEndpointSecureErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1s3_clusters_archive_create_admin_endpoint_secure_error_component_code(
    value: str,
) -> ApiV1S3ClustersArchiveCreateAdminEndpointSecureErrorComponentCode:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_ADMIN_ENDPOINT_SECURE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_ADMIN_ENDPOINT_SECURE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
