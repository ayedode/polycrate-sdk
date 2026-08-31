from typing import Literal

ApiV1KubernetesControlplanesUpdateDiscoveryEnabledErrorComponentAttr = Literal["discovery_enabled"]

API_V1_KUBERNETES_CONTROLPLANES_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesUpdateDiscoveryEnabledErrorComponentAttr
] = {
    "discovery_enabled",
}


def check_api_v1_kubernetes_controlplanes_update_discovery_enabled_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesUpdateDiscoveryEnabledErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_UPDATE_DISCOVERY_ENABLED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
