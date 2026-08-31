from typing import Literal

ApiV1KubernetesAppsUninstallCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUninstallCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_kubernetes_apps_uninstall_create_description_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUninstallCreateDescriptionErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
