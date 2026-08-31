from typing import Literal

ApiV1KubernetesAddonsUpdateBlockNameErrorComponentAttr = Literal["block_name"]

API_V1_KUBERNETES_ADDONS_UPDATE_BLOCK_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsUpdateBlockNameErrorComponentAttr
] = {
    "block_name",
}


def check_api_v1_kubernetes_addons_update_block_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsUpdateBlockNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_UPDATE_BLOCK_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_UPDATE_BLOCK_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
