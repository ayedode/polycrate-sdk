from typing import Literal

ApiV1BlockRolloutsCreateStateErrorComponentAttr = Literal["state"]

API_V1_BLOCK_ROLLOUTS_CREATE_STATE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlockRolloutsCreateStateErrorComponentAttr] = {
    "state",
}


def check_api_v1_block_rollouts_create_state_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsCreateStateErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
