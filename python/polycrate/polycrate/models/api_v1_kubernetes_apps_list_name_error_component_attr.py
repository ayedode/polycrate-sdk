from typing import Literal

ApiV1KubernetesAppsListNameErrorComponentAttr = Literal["name"]

API_V1_KUBERNETES_APPS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1KubernetesAppsListNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_kubernetes_apps_list_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsListNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_LIST_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
