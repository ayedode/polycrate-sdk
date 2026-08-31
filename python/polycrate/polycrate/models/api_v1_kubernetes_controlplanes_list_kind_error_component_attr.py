from typing import Literal

ApiV1KubernetesControlplanesListKindErrorComponentAttr = Literal["kind"]

API_V1_KUBERNETES_CONTROLPLANES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesListKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_kubernetes_controlplanes_list_kind_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesListKindErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_LIST_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
