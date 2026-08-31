from typing import Literal

ApiV1KubernetesAppsInstallCreateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_KUBERNETES_APPS_INSTALL_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsInstallCreateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_kubernetes_apps_install_create_archived_at_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsInstallCreateArchivedAtErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_INSTALL_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_INSTALL_CREATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
