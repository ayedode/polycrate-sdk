from typing import Literal

ApiV1BlocksReconcileCreateTemplateErrorComponentAttr = Literal["template"]

API_V1_BLOCKS_RECONCILE_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksReconcileCreateTemplateErrorComponentAttr
] = {
    "template",
}


def check_api_v1_blocks_reconcile_create_template_error_component_attr(
    value: str,
) -> ApiV1BlocksReconcileCreateTemplateErrorComponentAttr:
    if value in API_V1_BLOCKS_RECONCILE_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RECONCILE_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
