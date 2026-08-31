from typing import Literal

ApiV1KubernetesAppsUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_KUBERNETES_APPS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_kubernetes_apps_update_criticality_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUpdateCriticalityErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
