from typing import Literal

ApiV1KubernetesAppsUninstallCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUninstallCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_kubernetes_apps_uninstall_create_archived_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUninstallCreateArchivedErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
