from typing import Literal

ApiV1KubernetesAppsUpdateNameErrorComponentAttr = Literal["name"]

API_V1_KUBERNETES_APPS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1KubernetesAppsUpdateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_kubernetes_apps_update_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUpdateNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
