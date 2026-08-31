from typing import Literal

ApiV1BlocksRepairCreateTemplateErrorComponentAttr = Literal["template"]

API_V1_BLOCKS_REPAIR_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRepairCreateTemplateErrorComponentAttr
] = {
    "template",
}


def check_api_v1_blocks_repair_create_template_error_component_attr(
    value: str,
) -> ApiV1BlocksRepairCreateTemplateErrorComponentAttr:
    if value in API_V1_BLOCKS_REPAIR_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_REPAIR_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
