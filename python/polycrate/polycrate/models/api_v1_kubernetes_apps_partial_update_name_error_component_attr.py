from typing import Literal

ApiV1KubernetesAppsPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsPartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_kubernetes_apps_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdateNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
