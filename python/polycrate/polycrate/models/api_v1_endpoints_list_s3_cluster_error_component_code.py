from typing import Literal

ApiV1EndpointsListS3ClusterErrorComponentCode = Literal["invalid", "null_characters_not_allowed"]

API_V1_ENDPOINTS_LIST_S3_CLUSTER_ERROR_COMPONENT_CODE_VALUES: set[ApiV1EndpointsListS3ClusterErrorComponentCode] = {
    "invalid",
    "null_characters_not_allowed",
}


def check_api_v1_endpoints_list_s3_cluster_error_component_code(
    value: str,
) -> ApiV1EndpointsListS3ClusterErrorComponentCode:
    if value in API_V1_ENDPOINTS_LIST_S3_CLUSTER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_LIST_S3_CLUSTER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
