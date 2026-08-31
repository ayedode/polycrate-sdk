from typing import Literal

ApiV1KubernetesVolumesUpdatePhaseErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_VOLUMES_UPDATE_PHASE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesUpdatePhaseErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_volumes_update_phase_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesUpdatePhaseErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_UPDATE_PHASE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_UPDATE_PHASE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
