from typing import Literal

ApiV1KubernetesVolumesPartialUpdatePhaseErrorComponentAttr = Literal["phase"]

API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_PHASE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesPartialUpdatePhaseErrorComponentAttr
] = {
    "phase",
}


def check_api_v1_kubernetes_volumes_partial_update_phase_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesPartialUpdatePhaseErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_PHASE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_PARTIAL_UPDATE_PHASE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
