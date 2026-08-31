from typing import Literal

ApiV1BlocksDiscoverCreateTemplateErrorComponentAttr = Literal["template"]

API_V1_BLOCKS_DISCOVER_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksDiscoverCreateTemplateErrorComponentAttr
] = {
    "template",
}


def check_api_v1_blocks_discover_create_template_error_component_attr(
    value: str,
) -> ApiV1BlocksDiscoverCreateTemplateErrorComponentAttr:
    if value in API_V1_BLOCKS_DISCOVER_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_DISCOVER_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
