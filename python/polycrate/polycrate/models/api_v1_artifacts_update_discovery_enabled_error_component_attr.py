from typing import Literal

ApiV1ArtifactsUpdateDiscoveryEnabledErrorComponentAttr = Literal["discovery_enabled"]

API_V1_ARTIFACTS_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ArtifactsUpdateDiscoveryEnabledErrorComponentAttr
] = {
    "discovery_enabled",
}


def check_api_v1_artifacts_update_discovery_enabled_error_component_attr(
    value: str,
) -> ApiV1ArtifactsUpdateDiscoveryEnabledErrorComponentAttr:
    if value in API_V1_ARTIFACTS_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ARTIFACTS_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
