from typing import Literal

ApiV1KubernetesControlplanesCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_KUBERNETES_CONTROLPLANES_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_kubernetes_controlplanes_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesCreateSloTargetErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
