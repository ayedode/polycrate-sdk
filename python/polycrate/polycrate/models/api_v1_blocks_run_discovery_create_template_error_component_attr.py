from typing import Literal

ApiV1BlocksRunDiscoveryCreateTemplateErrorComponentAttr = Literal["template"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateTemplateErrorComponentAttr
] = {
    "template",
}


def check_api_v1_blocks_run_discovery_create_template_error_component_attr(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateTemplateErrorComponentAttr:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
