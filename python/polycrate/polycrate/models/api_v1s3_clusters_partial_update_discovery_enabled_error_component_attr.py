from typing import Literal

ApiV1S3ClustersPartialUpdateDiscoveryEnabledErrorComponentAttr = Literal["discovery_enabled"]

API_V1S3_CLUSTERS_PARTIAL_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1S3ClustersPartialUpdateDiscoveryEnabledErrorComponentAttr
] = {
    "discovery_enabled",
}


def check_api_v1s3_clusters_partial_update_discovery_enabled_error_component_attr(
    value: str,
) -> ApiV1S3ClustersPartialUpdateDiscoveryEnabledErrorComponentAttr:
    if value in API_V1S3_CLUSTERS_PARTIAL_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1S3_CLUSTERS_PARTIAL_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
