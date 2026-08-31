from typing import Literal

ApiV1S3ClustersPartialUpdateEndpointSecureErrorComponentAttr = Literal["endpoint_secure"]

API_V1S3_CLUSTERS_PARTIAL_UPDATE_ENDPOINT_SECURE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersPartialUpdateEndpointSecureErrorComponentAttr
] = {
    "endpoint_secure",
}


def check_api_v1s3_clusters_partial_update_endpoint_secure_error_component_attr(
    value: str,
) -> ApiV1S3ClustersPartialUpdateEndpointSecureErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_PARTIAL_UPDATE_ENDPOINT_SECURE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_PARTIAL_UPDATE_ENDPOINT_SECURE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
