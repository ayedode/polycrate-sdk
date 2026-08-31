from typing import Literal

ApiV1KubernetesVolumesPartialUpdatePhaseErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_PHASE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesPartialUpdatePhaseErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_volumes_partial_update_phase_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesPartialUpdatePhaseErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_PHASE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_PHASE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
