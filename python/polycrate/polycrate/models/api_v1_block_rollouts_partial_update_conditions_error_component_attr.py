from typing import Literal

ApiV1BlockRolloutsPartialUpdateConditionsErrorComponentAttr = Literal["conditions"]

API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_CONDITIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsPartialUpdateConditionsErrorComponentAttr
] = {
    "conditions",
}


def check_api_v1_block_rollouts_partial_update_conditions_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsPartialUpdateConditionsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_CONDITIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_CONDITIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
