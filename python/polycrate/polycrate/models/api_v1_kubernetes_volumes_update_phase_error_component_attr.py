from typing import Literal

ApiV1KubernetesVolumesUpdatePhaseErrorComponentAttr = Literal["phase"]

API_V1_KUBERNETES_VOLUMES_UPDATE_PHASE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesUpdatePhaseErrorComponentAttr
] = {
    "phase",
}


def check_api_v1_kubernetes_volumes_update_phase_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesUpdatePhaseErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_UPDATE_PHASE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_UPDATE_PHASE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
