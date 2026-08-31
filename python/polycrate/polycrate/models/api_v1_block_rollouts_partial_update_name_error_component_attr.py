from typing import Literal

ApiV1BlockRolloutsPartialUpdateNameErrorComponentAttr = Literal["name"]

API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsPartialUpdateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_block_rollouts_partial_update_name_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsPartialUpdateNameErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
