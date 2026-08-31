from typing import Literal

ApiV1S3ClustersArchiveCreateAdminEndpointErrorComponentAttr = Literal["admin_endpoint"]

API_V1S3_CLUSTERS_ARCHIVE_CREATE_ADMIN_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersArchiveCreateAdminEndpointErrorComponentAttr
] = {
    "admin_endpoint",
}


def check_api_v1s3_clusters_archive_create_admin_endpoint_error_component_attr(
    value: str,
) -> ApiV1S3ClustersArchiveCreateAdminEndpointErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_ARCHIVE_CREATE_ADMIN_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_ARCHIVE_CREATE_ADMIN_ENDPOINT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
