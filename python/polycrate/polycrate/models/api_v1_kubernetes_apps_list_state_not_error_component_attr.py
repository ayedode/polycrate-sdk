from typing import Literal

ApiV1KubernetesAppsListStateNotErrorComponentAttr = Literal["state_not"]

API_V1_KUBERNETES_APPS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsListStateNotErrorComponentAttr
] = {
    "state_not",
}


def check_api_v1_kubernetes_apps_list_state_not_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsListStateNotErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_LIST_STATE_NOT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
