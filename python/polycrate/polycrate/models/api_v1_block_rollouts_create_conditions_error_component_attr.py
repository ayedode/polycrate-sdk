from typing import Literal

ApiV1BlockRolloutsCreateConditionsErrorComponentAttr = Literal["conditions"]

API_V1_BLOCK_ROLLOUTS_CREATE_CONDITIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsCreateConditionsErrorComponentAttr
] = {
    "conditions",
}


def check_api_v1_block_rollouts_create_conditions_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsCreateConditionsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_CONDITIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_CONDITIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
