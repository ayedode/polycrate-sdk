from typing import Literal

ApiV1KubernetesAppsArchiveCreateScopeErrorComponentAttr = Literal["scope"]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsArchiveCreateScopeErrorComponentAttr
] = {
    "scope",
}


def check_api_v1_kubernetes_apps_archive_create_scope_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreateScopeErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_SCOPE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
