from typing import Literal

ApiV1KubernetesAddonsListUpdatedAtErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_ADDONS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsListUpdatedAtErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_addons_list_updated_at_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsListUpdatedAtErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_LIST_UPDATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
