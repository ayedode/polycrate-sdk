from typing import Literal

ApiV1KubernetesAppsInstallCreateArchivedByErrorComponentAttr = Literal["archived_by"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsInstallCreateArchivedByErrorComponentAttr
] = {
    "archived_by",
}


def check_api_v1_kubernetes_apps_install_create_archived_by_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateArchivedByErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
