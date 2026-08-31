from typing import Literal

ApiV1BlocksLogsReloadCreateUserSpecErrorComponentAttr = Literal["user_spec"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_USER_SPEC_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateUserSpecErrorComponentAttr
] = {
    "user_spec",
}


def check_api_v1_blocks_logs_reload_create_user_spec_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateUserSpecErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_USER_SPEC_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_USER_SPEC_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
