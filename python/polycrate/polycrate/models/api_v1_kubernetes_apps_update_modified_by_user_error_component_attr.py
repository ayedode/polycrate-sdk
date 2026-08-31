from typing import Literal

ApiV1KubernetesAppsUpdateModifiedByUserErrorComponentAttr = Literal["modified_by_user"]

API_V1_KUBERNETES_APPS_UPDATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsUpdateModifiedByUserErrorComponentAttr
] = {
    "modified_by_user",
}


def check_api_v1_kubernetes_apps_update_modified_by_user_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsUpdateModifiedByUserErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_UPDATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_UPDATE_MODIFIED_BY_USER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
