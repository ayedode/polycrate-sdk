from typing import Literal

ApiV1BlocksLogsReloadCreateTemplateErrorComponentAttr = Literal["template"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateTemplateErrorComponentAttr
] = {
    "template",
}


def check_api_v1_blocks_logs_reload_create_template_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateTemplateErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_TEMPLATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
