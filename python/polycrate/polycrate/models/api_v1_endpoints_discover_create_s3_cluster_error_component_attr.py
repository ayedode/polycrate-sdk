from typing import Literal

ApiV1EndpointsDiscoverCreateS3ClusterErrorComponentAttr = Literal["s3_cluster"]

API_V1_ENDPOINTS_DISCOVER_CREATE_S3_CLUSTER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsDiscoverCreateS3ClusterErrorComponentAttr
] = {
    "s3_cluster",
}


def check_api_v1_endpoints_discover_create_s3_cluster_error_component_attr(
    value: str,
) -> ApiV1EndpointsDiscoverCreateS3ClusterErrorComponentAttr:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_S3_CLUSTER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_S3_CLUSTER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
