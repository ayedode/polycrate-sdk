from typing import Literal

ApiV1BlocksPartialUpdateTemplateErrorComponentAttr = Literal["template"]

API_V1_BLOCKS_PARTIAL_UPDATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksPartialUpdateTemplateErrorComponentAttr
] = {
    "template",
}


def check_api_v1_blocks_partial_update_template_error_component_attr(
    value: str,
) -> ApiV1BlocksPartialUpdateTemplateErrorComponentAttr:
    if value in API_V1_BLOCKS_PARTIAL_UPDATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_PARTIAL_UPDATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
