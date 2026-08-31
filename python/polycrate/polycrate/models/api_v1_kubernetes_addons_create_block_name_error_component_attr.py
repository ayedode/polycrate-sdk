from typing import Literal

ApiV1KubernetesAddonsCreateBlockNameErrorComponentAttr = Literal["block_name"]

API_V1_KUBERNETES_ADDONS_CREATE_BLOCK_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsCreateBlockNameErrorComponentAttr
] = {
    "block_name",
}


def check_api_v1_kubernetes_addons_create_block_name_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsCreateBlockNameErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_CREATE_BLOCK_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_CREATE_BLOCK_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
