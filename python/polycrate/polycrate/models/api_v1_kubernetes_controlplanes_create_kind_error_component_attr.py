from typing import Literal

ApiV1KubernetesControlplanesCreateKindErrorComponentAttr = Literal["kind"]

API_V1_KUBERNETES_CONTROLPLANES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_kubernetes_controlplanes_create_kind_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesCreateKindErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
