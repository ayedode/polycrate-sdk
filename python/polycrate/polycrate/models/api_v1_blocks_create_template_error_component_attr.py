from typing import Literal

ApiV1BlocksCreateTemplateErrorComponentAttr = Literal["template"]

API_V1_BLOCKS_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlocksCreateTemplateErrorComponentAttr] = {
    "template",
}


def check_api_v1_blocks_create_template_error_component_attr(value: str) -> ApiV1BlocksCreateTemplateErrorComponentAttr:
    if value in API_V1_BLOCKS_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
