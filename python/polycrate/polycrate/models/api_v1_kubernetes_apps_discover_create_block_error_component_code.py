from typing import Literal

ApiV1KubernetesAppsDiscoverCreateBlockErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_KUBERNETES_APPS_DISCOVER_CREATE_BLOCK_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAppsDiscoverCreateBlockErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_kubernetes_apps_discover_create_block_error_component_code(
    value: str,
) -> ApiV1KubernetesAppsDiscoverCreateBlockErrorComponentCode:
    if value in API_V1_KUBERNETES_APPS_DISCOVER_CREATE_BLOCK_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_DISCOVER_CREATE_BLOCK_ERROR_COMPONENT_CODE_VALUES!r}"
    )
