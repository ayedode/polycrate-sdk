from typing import Literal

ApiV1BlocksArchiveCreateAutoRolloutErrorComponentCode = Literal["invalid", "null"]

API_V1_BLOCKS_ARCHIVE_CREATE_AUTO_ROLLOUT_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlocksArchiveCreateAutoRolloutErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_blocks_archive_create_auto_rollout_error_component_code(
    value: str,
) -> ApiV1BlocksArchiveCreateAutoRolloutErrorComponentCode:
    if value in API_V1_BLOCKS_ARCHIVE_CREATE_AUTO_ROLLOUT_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_ARCHIVE_CREATE_AUTO_ROLLOUT_ERROR_COMPONENT_CODE_VALUES!r}"
    )
