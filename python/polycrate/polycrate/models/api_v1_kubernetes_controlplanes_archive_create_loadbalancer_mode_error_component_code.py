from typing import Literal

ApiV1KubernetesControlplanesArchiveCreateLoadbalancerModeErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_LOADBALANCER_MODE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesArchiveCreateLoadbalancerModeErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_controlplanes_archive_create_loadbalancer_mode_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesArchiveCreateLoadbalancerModeErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_LOADBALANCER_MODE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_ARCHIVE_CREATE_LOADBALANCER_MODE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
