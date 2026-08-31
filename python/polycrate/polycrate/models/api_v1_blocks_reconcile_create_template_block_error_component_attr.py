from typing import Literal

ApiV1BlocksReconcileCreateTemplateBlockErrorComponentAttr = Literal["template_block"]

API_V1_BLOCKS_RECONCILE_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksReconcileCreateTemplateBlockErrorComponentAttr
] = {
    "template_block",
}


def check_api_v1_blocks_reconcile_create_template_block_error_component_attr(
    value: str,
) -> ApiV1BlocksReconcileCreateTemplateBlockErrorComponentAttr:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_TEMPLATE_BLOCK_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
