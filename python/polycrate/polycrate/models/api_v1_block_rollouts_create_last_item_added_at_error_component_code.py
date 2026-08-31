from typing import Literal

ApiV1BlockRolloutsCreateLastItemAddedAtErrorComponentCode = Literal["date", "invalid", "make_aware", "overflow"]

API_V1_BLOCK_ROLLOUTS_CREATE_LAST_ITEM_ADDED_AT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsCreateLastItemAddedAtErrorComponentCode
] = {
    "date",
    "invalid",
    "make_aware",
    "overflow",
}


def check_api_v1_block_rollouts_create_last_item_added_at_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsCreateLastItemAddedAtErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_LAST_ITEM_ADDED_AT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_LAST_ITEM_ADDED_AT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
