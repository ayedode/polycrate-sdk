from typing import Literal

ApiV1EndpointsDiscoverCreateS3ClusterErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_ENDPOINTS_DISCOVER_CREATE_S3_CLUSTER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1EndpointsDiscoverCreateS3ClusterErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_endpoints_discover_create_s3_cluster_error_component_code(
    value: str,
) -> ApiV1EndpointsDiscoverCreateS3ClusterErrorComponentCode:
    if value in API_V1_ENDPOINTS_DISCOVER_CREATE_S3_CLUSTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_DISCOVER_CREATE_S3_CLUSTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
