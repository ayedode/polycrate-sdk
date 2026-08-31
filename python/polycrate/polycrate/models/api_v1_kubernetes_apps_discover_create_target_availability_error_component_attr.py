from typing import Literal

ApiV1KubernetesAppsDiscoverCreateTargetAvailabilityErrorComponentAttr = Literal["target_availability"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateTargetAvailabilityErrorComponentAttr
] = {
    "target_availability",
}


def check_api_v1_kubernetes_apps_discover_create_target_availability_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateTargetAvailabilityErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_TARGET_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
