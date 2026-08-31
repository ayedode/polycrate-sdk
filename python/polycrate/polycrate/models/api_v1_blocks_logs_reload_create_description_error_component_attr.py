from typing import Literal

ApiV1BlocksLogsReloadCreateDescriptionErrorComponentAttr = Literal["description"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateDescriptionErrorComponentAttr
] = {
    "description",
}


def check_api_v1_blocks_logs_reload_create_description_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateDescriptionErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_DESCRIPTION_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
