from typing import Literal

ApiV1KubernetesControlplanesArchiveCreateLoadbalancerModeErrorComponentAttr = Literal["loadbalancer_mode"]

API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_LOADBALANCER_MODE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesArchiveCreateLoadbalancerModeErrorComponentAttr
] = {
    "loadbalancer_mode",
}


def check_api_v1_kubernetes_controlplanes_archive_create_loadbalancer_mode_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesArchiveCreateLoadbalancerModeErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_LOADBALANCER_MODE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_LOADBALANCER_MODE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
