from typing import Literal

ApiV1KubernetesAppsArchiveCreateModifiedByUserErrorComponentAttr = Literal["modified_by_user"]

API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsArchiveCreateModifiedByUserErrorComponentAttr
] = {
    "modified_by_user",
}


def check_api_v1_kubernetes_apps_archive_create_modified_by_user_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsArchiveCreateModifiedByUserErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_ARCHIVE_CREATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
