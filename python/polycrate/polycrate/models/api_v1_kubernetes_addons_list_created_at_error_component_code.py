from typing import Literal

ApiV1KubernetesAddonsListCreatedAtErrorComponentCode = Literal["invalid"]

API_V1_KUBERNETES_ADDONS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsListCreatedAtErrorComponentCode
] = {
    "invalid",
}


def check_api_v1_kubernetes_addons_list_created_at_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsListCreatedAtErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_LIST_CREATED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
