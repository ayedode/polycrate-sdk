from typing import Literal

ApiV1BlockRolloutsListSearchErrorComponentCode = Literal["null_characters_not_allowed"]

API_V1_BLOCK_ROLLOUTS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES: set[ApiV1BlockRolloutsListSearchErrorComponentCode] = {
    "null_characters_not_allowed",
}


def check_api_v1_block_rollouts_list_search_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsListSearchErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_LIST_SEARCH_ERROR_COMPONENT_CODE_VALUES!r}"
    )
