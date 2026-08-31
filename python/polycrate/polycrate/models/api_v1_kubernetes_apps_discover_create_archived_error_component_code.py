from typing import Literal

ApiV1KubernetesAppsDiscoverCreateArchivedErrorComponentCode = Literal["invalid", "null"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateArchivedErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_kubernetes_apps_discover_create_archived_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateArchivedErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_CODE_VALUES!r}"
    )
