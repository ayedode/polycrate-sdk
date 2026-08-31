from typing import Literal

ApiV1KubernetesAppsCreateArchivedByErrorComponentAttr = Literal["archived_by"]

API_V1_KUBERNETES_APPS_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsCreateArchivedByErrorComponentAttr
] = {
    "archived_by",
}


def check_api_v1_kubernetes_apps_create_archived_by_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsCreateArchivedByErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_ARCHIVED_BY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
