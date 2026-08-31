from typing import Literal

ApiV1KubernetesAppsPartialUpdateBlockErrorComponentAttr = Literal["block"]

API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAppsPartialUpdateBlockErrorComponentAttr
] = {
    "block",
}


def check_api_v1_kubernetes_apps_partial_update_block_error_component_attr(
    value: str,
) -> ApiV1KubernetesAppsPartialUpdateBlockErrorComponentAttr:
    if value in API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_APPS_PARTIAL_UPDATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
