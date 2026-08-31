from typing import Literal

ApiV1KubernetesControlplanesCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_KUBERNETES_CONTROLPLANES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_kubernetes_controlplanes_create_criticality_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesCreateCriticalityErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
