from typing import Literal

ApiV1BlocksLogsReloadCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_blocks_logs_reload_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateProviderIdErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
