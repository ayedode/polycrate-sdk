from typing import Literal

ApiV1KubernetesVolumesUpdateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_KUBERNETES_VOLUMES_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesUpdateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_kubernetes_volumes_update_criticality_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesUpdateCriticalityErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_UPDATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
