from typing import Literal

ApiV1KubernetesControlplanesUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_KUBERNETES_CONTROLPLANES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_kubernetes_controlplanes_update_criticality_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesUpdateCriticalityErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
