from typing import Literal

ApiV1KubernetesAppsListUpdatedAtErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_APPS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsListUpdatedAtErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_apps_list_updated_at_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsListUpdatedAtErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
