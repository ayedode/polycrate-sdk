from typing import Literal

ApiV1KubernetesAddonsListBlockNameErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_KUBERNETES_ADDONS_LIST_BLOCK_NAME_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1KubernetesAddonsListBlockNameErrorComponentCode
] = {
    "null_characters_not_allowed",
}


def check_api_v1_kubernetes_addons_list_block_name_error_component_code(
    value: str,
) -> ApiV1KubernetesAddonsListBlockNameErrorComponentCode:
    if value in API_V1_KUBERNETES_ADDONS_LIST_BLOCK_NAME_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_LIST_BLOCK_NAME_ERROR_COMPONENT_CODE_VALUES!r}"
    )
