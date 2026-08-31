from typing import Literal

ApiV1KubernetesVolumesListPhaseErrorComponentAttr = Literal["phase"]

API_V1_KUBERNETES_VOLUMES_LIST_PHASE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesListPhaseErrorComponentAttr
] = {
    "phase",
}


def check_api_v1_kubernetes_volumes_list_phase_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesListPhaseErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_LIST_PHASE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_LIST_PHASE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
