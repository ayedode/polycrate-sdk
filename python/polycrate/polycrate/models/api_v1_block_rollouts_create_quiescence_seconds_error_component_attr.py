from typing import Literal

ApiV1BlockRolloutsCreateQuiescenceSecondsErrorComponentAttr = Literal["quiescence_seconds"]

API_V1_BLOCK_ROLLOUTS_CREATE_QUIESCENCE_SECONDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsCreateQuiescenceSecondsErrorComponentAttr
] = {
    "quiescence_seconds",
}


def check_api_v1_block_rollouts_create_quiescence_seconds_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsCreateQuiescenceSecondsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_QUIESCENCE_SECONDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_QUIESCENCE_SECONDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
