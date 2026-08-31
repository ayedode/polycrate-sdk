from typing import Literal

ApiV1KubernetesVolumesUpdateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_KUBERNETES_VOLUMES_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesVolumesUpdateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_kubernetes_volumes_update_actual_availability_error_component_attr(
    value: str,
) -> ApiV1KubernetesVolumesUpdateActualAvailabilityErrorComponentAttr:
    if value in API_V1_KUBERNETES_VOLUMES_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_VOLUMES_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
