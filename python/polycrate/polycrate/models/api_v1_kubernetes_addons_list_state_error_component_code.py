from typing import Literal

ApiV1KubernetesAddonsListStateErrorComponentCode = Literal["invalid_choice"]

API_V1_KUBERNETES_ADDONS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsListStateErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_kubernetes_addons_list_state_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsListStateErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_LIST_STATE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
