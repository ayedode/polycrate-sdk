from typing import Literal

ApiV1BlocksArchiveCreateAutoRolloutErrorComponentAttr = Literal["auto_rollout"]

API_V1_BLOCKS_ARCHIVE_CREATE_AUTO_ROLLOUT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksArchiveCreateAutoRolloutErrorComponentAttr
] = {
    "auto_rollout",
}


def check_api_v1_blocks_archive_create_auto_rollout_error_component_attr(
    value: str,
) -> ApiV1BlocksArchiveCreateAutoRolloutErrorComponentAttr:
    if value in API_V1_BLOCKS_ARCHIVE_CREATE_AUTO_ROLLOUT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_ARCHIVE_CREATE_AUTO_ROLLOUT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
