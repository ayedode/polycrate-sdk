from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateFailureThresholdPercentErrorComponentAttr = Literal["failure_threshold_percent"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_FAILURE_THRESHOLD_PERCENT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateFailureThresholdPercentErrorComponentAttr
] = {
    "failure_threshold_percent",
}


def check_api_v1_block_rollout_configs_archive_create_failure_threshold_percent_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateFailureThresholdPercentErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_FAILURE_THRESHOLD_PERCENT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_FAILURE_THRESHOLD_PERCENT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
