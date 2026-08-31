from typing import Literal

ApiV1KubernetesAddonsArchiveCreateTemplateBlockErrorComponentAttr = Literal["template_block"]

API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1KubernetesAddonsArchiveCreateTemplateBlockErrorComponentAttr
] = {
    "template_block",
}


def check_api_v1_kubernetes_addons_archive_create_template_block_error_component_attr(
    value: str,
) -> ApiV1KubernetesAddonsArchiveCreateTemplateBlockErrorComponentAttr:
    if value in API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_KUBERNETES_ADDONS_ARCHIVE_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
