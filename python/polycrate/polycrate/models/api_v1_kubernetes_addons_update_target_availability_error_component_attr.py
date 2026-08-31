from typing import Literal

ApiV1KubernetesAddonsUpdateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_KUBERNETES_ADDONS_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsUpdateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_kubernetes_addons_update_target_availability_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsUpdateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_UPDATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
