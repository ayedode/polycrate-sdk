from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateConditionsErrorComponentAttr = Literal["conditions"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_CONDITIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateConditionsErrorComponentAttr
] = {
    "conditions",
}


def check_api_v1_block_rollout_configs_archive_create_conditions_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateConditionsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_CONDITIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_CONDITIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
