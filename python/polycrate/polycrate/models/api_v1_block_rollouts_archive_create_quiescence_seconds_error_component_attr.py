from typing import Literal

ApiV1BlockRolloutsArchiveCreateQuiescenceSecondsErrorComponentAttr = Literal["quiescence_seconds"]

API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_QUIESCENCE_SECONDS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsArchiveCreateQuiescenceSecondsErrorComponentAttr
] = {
    "quiescence_seconds",
}


def check_api_v1_block_rollouts_archive_create_quiescence_seconds_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsArchiveCreateQuiescenceSecondsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_QUIESCENCE_SECONDS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_QUIESCENCE_SECONDS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
