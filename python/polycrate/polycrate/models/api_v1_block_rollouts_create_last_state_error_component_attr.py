from typing import Literal

ApiV1BlockRolloutsCreateLastStateErrorComponentAttr = Literal["last_state"]

API_V1_BLOCK_ROLLOUTS_CREATE_LAST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsCreateLastStateErrorComponentAttr
] = {
    "last_state",
}


def check_api_v1_block_rollouts_create_last_state_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsCreateLastStateErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_LAST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_LAST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
