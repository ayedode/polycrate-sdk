from typing import Literal

ApiV1BlockRolloutsArchiveCreateTotalItemsErrorComponentCode = Literal[
    "invalid", "max_string_length", "max_value", "min_value", "null"
]

API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_TOTAL_ITEMS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsArchiveCreateTotalItemsErrorComponentCode
] = {
    "invalid",
    "max_string_length",
    "max_value",
    "min_value",
    "null",
}


def check_api_v1_block_rollouts_archive_create_total_items_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsArchiveCreateTotalItemsErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_TOTAL_ITEMS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_TOTAL_ITEMS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
