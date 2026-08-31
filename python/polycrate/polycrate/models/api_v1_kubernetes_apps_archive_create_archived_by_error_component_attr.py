from typing import Literal

ApiV1KubernetesAppsArchiveCreateArchivedByErrorComponentAttr = Literal["archived_by"]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsArchiveCreateArchivedByErrorComponentAttr
] = {
    "archived_by",
}


def check_api_v1_kubernetes_apps_archive_create_archived_by_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreateArchivedByErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
