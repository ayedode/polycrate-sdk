from typing import Literal

ApiV1KubernetesAppsCreateArchivedErrorComponentAttr = Literal["archived"]

API_V1_KUBERNETES_APPS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsCreateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_kubernetes_apps_create_archived_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsCreateArchivedErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_CREATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
