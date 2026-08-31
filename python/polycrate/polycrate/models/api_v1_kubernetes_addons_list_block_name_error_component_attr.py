from typing import Literal

ApiV1KubernetesAddonsListBlockNameErrorComponentAttr = Literal["block_name"]

API_V1_KUBERNETES_ADDONS_LIST_BLOCK_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsListBlockNameErrorComponentAttr
] = {
    "block_name",
}


def check_api_v1_kubernetes_addons_list_block_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsListBlockNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_LIST_BLOCK_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_LIST_BLOCK_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
