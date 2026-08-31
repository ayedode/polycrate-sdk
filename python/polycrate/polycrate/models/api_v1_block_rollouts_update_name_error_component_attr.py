from typing import Literal

ApiV1BlockRolloutsUpdateNameErrorComponentAttr = Literal["name"]

API_V1_BLOCK_ROLLOUTS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlockRolloutsUpdateNameErrorComponentAttr] = {
    "name",
}


def check_api_v1_block_rollouts_update_name_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsUpdateNameErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_UPDATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
