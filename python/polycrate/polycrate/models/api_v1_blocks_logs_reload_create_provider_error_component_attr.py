from typing import Literal

ApiV1BlocksLogsReloadCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_blocks_logs_reload_create_provider_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateProviderErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
