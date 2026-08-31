from typing import Literal

ApiV1KubernetesControlplanesPartialUpdateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesControlplanesPartialUpdateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_kubernetes_controlplanes_partial_update_actual_availability_error_component_attr(
    value: str,
) -> ApiV1KubernetesControlplanesPartialUpdateActualAvailabilityErrorComponentAttr:
    if value in API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_CONTROLPLANES_PARTIAL_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
