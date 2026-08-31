from typing import Literal

ApiV1KubernetesVolumesCreatePhaseErrorComponentAttr = Literal["phase"]

API_V1_KUBERNETES_VOLUMES_CREATE_PHASE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesCreatePhaseErrorComponentAttr
] = {
    "phase",
}


def check_api_v1_kubernetes_volumes_create_phase_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesCreatePhaseErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_CREATE_PHASE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_CREATE_PHASE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
