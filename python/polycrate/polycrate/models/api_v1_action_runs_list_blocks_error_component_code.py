from typing import Literal

ApiV1ActionRunsListBlocksErrorComponentCode = Literal["invalid_choice", "invalid_list", "invalid_pk_value"]

API_V1_ACTION_RUNS_LIST_BLOCKS_ERROR_COMPONENT_CODE_VALUES: set[ApiV1ActionRunsListBlocksErrorComponentCode] = {
    "invalid_choice",
    "invalid_list",
    "invalid_pk_value",
}


def check_api_v1_action_runs_list_blocks_error_component_code(
    value: str,
) -> ApiV1ActionRunsListBlocksErrorComponentCode:
    if value in API_V1_ACTION_RUNS_LIST_BLOCKS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTION_RUNS_LIST_BLOCKS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
