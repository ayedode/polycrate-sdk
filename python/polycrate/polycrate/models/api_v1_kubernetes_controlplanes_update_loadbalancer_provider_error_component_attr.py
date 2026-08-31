from typing import Literal

ApiV1KubernetesControlplanesUpdateLoadbalancerProviderErrorComponentAttr = Literal["loadbalancer_provider"]

API_V1_KUBERNETES_CONTROLPLANES_UPDATE_LOADBALANCER_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesUpdateLoadbalancerProviderErrorComponentAttr
] = {
    "loadbalancer_provider",
}


def check_api_v1_kubernetes_controlplanes_update_loadbalancer_provider_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesUpdateLoadbalancerProviderErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_UPDATE_LOADBALANCER_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_UPDATE_LOADBALANCER_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
