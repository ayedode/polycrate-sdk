from typing import Literal

ApiV1S3ClustersUpdateAdminEndpointSecureErrorComponentAttr = Literal["admin_endpoint_secure"]

API_V1S3_CLUSTERS_UPDATE_ADMIN_ENDPOINT_SECURE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersUpdateAdminEndpointSecureErrorComponentAttr
] = {
    "admin_endpoint_secure",
}


def check_api_v1s3_clusters_update_admin_endpoint_secure_error_component_attr(
    value: str,
) -> ApiV1S3ClustersUpdateAdminEndpointSecureErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_UPDATE_ADMIN_ENDPOINT_SECURE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_ADMIN_ENDPOINT_SECURE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
