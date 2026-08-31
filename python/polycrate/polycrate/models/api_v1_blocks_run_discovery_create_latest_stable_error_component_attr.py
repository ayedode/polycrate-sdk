from typing import Literal

ApiV1BlocksRunDiscoveryCreateLatestStableErrorComponentAttr = Literal["latest_stable"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_LATEST_STABLE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateLatestStableErrorComponentAttr
] = {
    "latest_stable",
}


def check_api_v1_blocks_run_discovery_create_latest_stable_error_component_attr(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateLatestStableErrorComponentAttr:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_LATEST_STABLE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_LATEST_STABLE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
