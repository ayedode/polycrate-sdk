from typing import Literal

ApiV1KubernetesAppsCreateUninstallationFailedErrorComponentAttr = Literal["uninstallation_failed"]

API_V1_KUBERNETES_APPS_CREATE_UNINSTALLATION_FAILED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsCreateUninstallationFailedErrorComponentAttr
] = {
    "uninstallation_failed",
}


def check_api_v1_kubernetes_apps_create_uninstallation_failed_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsCreateUninstallationFailedErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_CREATE_UNINSTALLATION_FAILED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_UNINSTALLATION_FAILED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
