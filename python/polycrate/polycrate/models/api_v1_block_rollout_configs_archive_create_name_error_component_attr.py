from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateNameErrorComponentAttr = Literal["name"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateNameErrorComponentAttr
] = {
    "name",
}


def check_api_v1_block_rollout_configs_archive_create_name_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateNameErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
