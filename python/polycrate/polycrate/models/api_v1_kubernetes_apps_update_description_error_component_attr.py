from typing import Literal

ApiV1KubernetesAppsUpdateDescriptionErrorComponentAttr = Literal["description"]

API_V1_KUBERNETES_APPS_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUpdateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_kubernetes_apps_update_description_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUpdateDescriptionErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
