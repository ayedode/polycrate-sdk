from typing import Literal

ApiV1BlockRolloutsUpdateDiscoveryTaskIdErrorComponentAttr = Literal["discovery_task_id"]

API_V1_BLOCK_ROLLOUTS_UPDATE_DISCOVERY_TASK_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsUpdateDiscoveryTaskIdErrorComponentAttr
] = {
    "discovery_task_id",
}


def check_api_v1_block_rollouts_update_discovery_task_id_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsUpdateDiscoveryTaskIdErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_UPDATE_DISCOVERY_TASK_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_UPDATE_DISCOVERY_TASK_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
