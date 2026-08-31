from typing import Literal

ApiV1S3ClustersCreateEndpointSecureErrorComponentAttr = Literal["endpoint_secure"]

API_V1S3_CLUSTERS_CREATE_ENDPOINT_SECURE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersCreateEndpointSecureErrorComponentAttr
] = {
    "endpoint_secure",
}


def check_api_v1s3_clusters_create_endpoint_secure_error_component_attr(
    value: str,
) -> ApiV1S3ClustersCreateEndpointSecureErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_CREATE_ENDPOINT_SECURE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_ENDPOINT_SECURE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
