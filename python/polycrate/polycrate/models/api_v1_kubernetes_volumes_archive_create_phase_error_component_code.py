from typing import Literal

ApiV1KubernetesVolumesArchiveCreatePhaseErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_PHASE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesVolumesArchiveCreatePhaseErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_kubernetes_volumes_archive_create_phase_error_component_code(
    value: str,
) -> ApiV1KubernetesVolumesArchiveCreatePhaseErrorComponentCode:
    if value in API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_PHASE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_PHASE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
