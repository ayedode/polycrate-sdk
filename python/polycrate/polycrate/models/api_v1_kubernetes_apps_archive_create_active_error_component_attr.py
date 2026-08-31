from typing import Literal

ApiV1KubernetesAppsArchiveCreateActiveErrorComponentAttr = Literal["active"]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsArchiveCreateActiveErrorComponentAttr
] = {
    "active",
}


def check_api_v1_kubernetes_apps_archive_create_active_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreateActiveErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
