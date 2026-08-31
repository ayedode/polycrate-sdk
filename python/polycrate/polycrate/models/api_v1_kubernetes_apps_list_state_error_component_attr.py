from typing import Literal

ApiV1KubernetesAppsListStateErrorComponentAttr = Literal["state"]

API_V1_KUBERNETES_APPS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1KubernetesAppsListStateErrorComponentAttr] = {
    "state",
}


def check_api_v1_kubernetes_apps_list_state_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsListStateErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_LIST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
