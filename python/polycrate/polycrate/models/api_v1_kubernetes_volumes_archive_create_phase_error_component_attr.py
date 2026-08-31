from typing import Literal

ApiV1KubernetesVolumesArchiveCreatePhaseErrorComponentAttr = Literal["phase"]

API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_PHASE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesArchiveCreatePhaseErrorComponentAttr
] = {
    "phase",
}


def check_api_v1_kubernetes_volumes_archive_create_phase_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesArchiveCreatePhaseErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_PHASE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_ARCHIVE_CREATE_PHASE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
