from typing import Literal

ApiV1S3ClustersCreateDiscoveryEnabledErrorComponentAttr = Literal["discovery_enabled"]

API_V1S3_CLUSTERS_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersCreateDiscoveryEnabledErrorComponentAttr
] = {
    "discovery_enabled",
}


def check_api_v1s3_clusters_create_discovery_enabled_error_component_attr(
    value: str,
) -> ApiV1S3ClustersCreateDiscoveryEnabledErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_CREATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
