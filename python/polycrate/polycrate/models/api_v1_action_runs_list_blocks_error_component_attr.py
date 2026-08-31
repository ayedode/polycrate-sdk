from typing import Literal

ApiV1ActionRunsListBlocksErrorComponentAttr = Literal["blocks"]

API_V1_ACTION_RUNS_LIST_BLOCKS_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ActionRunsListBlocksErrorComponentAttr] = {
    "blocks",
}


def check_api_v1_action_runs_list_blocks_error_component_attr(
    value: str,
) -> ApiV1ActionRunsListBlocksErrorComponentAttr:
    if value in API_V1_ACTION_RUNS_LIST_BLOCKS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ACTION_RUNS_LIST_BLOCKS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
