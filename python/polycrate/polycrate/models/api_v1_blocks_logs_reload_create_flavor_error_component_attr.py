from typing import Literal

ApiV1BlocksLogsReloadCreateFlavorErrorComponentAttr = Literal["flavor"]

API_V1_BLOCKS_LOGS_RELOAD_CREATE_FLAVOR_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksLogsReloadCreateFlavorErrorComponentAttr
] = {
    "flavor",
}


def check_api_v1_blocks_logs_reload_create_flavor_error_component_attr(
    value: str,
) -> ApiV1BlocksLogsReloadCreateFlavorErrorComponentAttr:
    if value in API_V1_BLOCKS_LOGS_RELOAD_CREATE_FLAVOR_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_LOGS_RELOAD_CREATE_FLAVOR_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
