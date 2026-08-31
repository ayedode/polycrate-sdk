from typing import Literal

ApiV1KubernetesAppsUninstallCreateSourceErrorComponentAttr = Literal["source"]

API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_SOURCE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUninstallCreateSourceErrorComponentAttr
] = {
    "source",
}


def check_api_v1_kubernetes_apps_uninstall_create_source_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUninstallCreateSourceErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_SOURCE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UNINSTALL_CREATE_SOURCE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
