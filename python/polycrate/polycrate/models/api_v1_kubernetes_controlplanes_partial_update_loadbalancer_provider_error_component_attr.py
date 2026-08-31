from typing import Literal

ApiV1KubernetesControlplanesPartialUpdateLoadbalancerProviderErrorComponentAttr = Literal["loadbalancer_provider"]

API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_LOADBALANCER_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesPartialUpdateLoadbalancerProviderErrorComponentAttr
] = {
    "loadbalancer_provider",
}


def check_api_v1_kubernetes_controlplanes_partial_update_loadbalancer_provider_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesPartialUpdateLoadbalancerProviderErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_LOADBALANCER_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_LOADBALANCER_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
