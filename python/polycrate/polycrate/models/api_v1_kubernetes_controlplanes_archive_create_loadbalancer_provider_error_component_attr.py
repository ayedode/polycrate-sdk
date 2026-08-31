from typing import Literal

ApiV1KubernetesControlplanesArchiveCreateLoadbalancerProviderErrorComponentAttr = Literal["loadbalancer_provider"]

API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_LOADBALANCER_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesArchiveCreateLoadbalancerProviderErrorComponentAttr
] = {
    "loadbalancer_provider",
}


def check_api_v1_kubernetes_controlplanes_archive_create_loadbalancer_provider_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesArchiveCreateLoadbalancerProviderErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_LOADBALANCER_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_LOADBALANCER_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
