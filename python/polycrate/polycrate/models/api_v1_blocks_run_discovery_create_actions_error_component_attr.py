from typing import Literal

ApiV1BlocksRunDiscoveryCreateActionsErrorComponentAttr = Literal["actions"]

API_V1_BLOCKS_RUN_DISCOVERY_CREATE_ACTIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksRunDiscoveryCreateActionsErrorComponentAttr
] = {
    "actions",
}


def check_api_v1_blocks_run_discovery_create_actions_error_component_attr(
    value: str,
) -> ApiV1BlocksRunDiscoveryCreateActionsErrorComponentAttr:
    if value in API_V1_BLOCKS_RUN_DISCOVERY_CREATE_ACTIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_RUN_DISCOVERY_CREATE_ACTIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
