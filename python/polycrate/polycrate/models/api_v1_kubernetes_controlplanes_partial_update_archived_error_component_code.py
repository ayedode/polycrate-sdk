from typing import Literal

ApiV1KubernetesControlplanesPartialUpdateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesControlplanesPartialUpdateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_controlplanes_partial_update_archived_error_component_code(
    value: str,
) -> ApiV1KubernetesControlplanesPartialUpdateArchivedErrorComponentCode:
    if value in API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
