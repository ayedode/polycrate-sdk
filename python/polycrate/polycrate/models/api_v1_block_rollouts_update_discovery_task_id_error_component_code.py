from typing import Literal

ApiV1BlockRolloutsUpdateDiscoveryTaskIdErrorComponentCode = Literal[
    "invalid", "null_characters_not_allowed", "surrogate_characters_not_allowed"
]

API_V1_BLOCK_ROLLOUTS_UPDATE_DISCOVERY_TASK_ID_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsUpdateDiscoveryTaskIdErrorComponentCode
] = {
    "invalid",
    "null_characters_not_allowed",
    "surrogate_characters_not_allowed",
}


def check_api_v1_block_rollouts_update_discovery_task_id_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsUpdateDiscoveryTaskIdErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_UPDATE_DISCOVERY_TASK_ID_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_UPDATE_DISCOVERY_TASK_ID_ERROR_COMPONENT_CODE_VALUES!r}"
    )
