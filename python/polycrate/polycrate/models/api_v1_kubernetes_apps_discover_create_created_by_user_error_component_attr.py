from typing import Literal

ApiV1KubernetesAppsDiscoverCreateCreatedByUserErrorComponentAttr = Literal["created_by_user"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateCreatedByUserErrorComponentAttr
] = {
    "created_by_user",
}


def check_api_v1_kubernetes_apps_discover_create_created_by_user_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateCreatedByUserErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_CREATED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
