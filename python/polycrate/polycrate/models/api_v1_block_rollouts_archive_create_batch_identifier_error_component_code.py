from typing import Literal

ApiV1BlockRolloutsArchiveCreateBatchIdentifierErrorComponentCode = Literal[
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
]

API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_BATCH_IDENTIFIER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsArchiveCreateBatchIdentifierErrorComponentCode
] = {
    "blank",
    "invalid",
    "max_length",
    "null",
    "null_characters_not_allowed",
    "required",
    "surrogate_characters_not_allowed",
}


def check_api_v1_block_rollouts_archive_create_batch_identifier_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsArchiveCreateBatchIdentifierErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_BATCH_IDENTIFIER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_BATCH_IDENTIFIER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
