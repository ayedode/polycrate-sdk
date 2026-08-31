from typing import Literal

ApiV1KubernetesAppsPartialUpdateActualAvailabilityErrorComponentAttr = Literal["actual_availability"]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsPartialUpdateActualAvailabilityErrorComponentAttr
] = {
    "actual_availability",
}


def check_api_v1_kubernetes_apps_partial_update_actual_availability_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdateActualAvailabilityErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_ACTUAL_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
