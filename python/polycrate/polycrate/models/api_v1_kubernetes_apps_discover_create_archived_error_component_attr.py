from typing import Literal

ApiV1KubernetesAppsDiscoverCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_kubernetes_apps_discover_create_archived_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateArchivedErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
