from typing import Literal

ApiV1S3ClustersUpdatePlatformServiceErrorComponentAttr = Literal["platform_service"]

API_V1S3_CLUSTERS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersUpdatePlatformServiceErrorComponentAttr
] = {
    "platform_service",
}


def check_api_v1s3_clusters_update_platform_service_error_component_attr(
    value: str,
) -> ApiV1S3ClustersUpdatePlatformServiceErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_UPDATE_PLATFORM_SERVICE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
