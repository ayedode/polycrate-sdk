from typing import Literal

ApiV1BlockRolloutsPartialUpdateDiscoveryRunningErrorComponentAttr = Literal["discovery_running"]

API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_DISCOVERY_RUNNING_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsPartialUpdateDiscoveryRunningErrorComponentAttr
] = {
    "discovery_running",
}


def check_api_v1_block_rollouts_partial_update_discovery_running_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsPartialUpdateDiscoveryRunningErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_DISCOVERY_RUNNING_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_DISCOVERY_RUNNING_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
