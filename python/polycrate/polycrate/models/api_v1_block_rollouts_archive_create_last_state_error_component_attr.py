from typing import Literal

ApiV1BlockRolloutsArchiveCreateLastStateErrorComponentAttr = Literal["last_state"]

API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_LAST_STATE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsArchiveCreateLastStateErrorComponentAttr
] = {
    "last_state",
}


def check_api_v1_block_rollouts_archive_create_last_state_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsArchiveCreateLastStateErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_LAST_STATE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_LAST_STATE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
