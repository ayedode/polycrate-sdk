from typing import Literal

ApiV1BlockRolloutConfigsArchiveCreateSloAvailabilityErrorComponentAttr = Literal["slo_availability"]

API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutConfigsArchiveCreateSloAvailabilityErrorComponentAttr
] = {
    "slo_availability",
}


def check_api_v1_block_rollout_configs_archive_create_slo_availability_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutConfigsArchiveCreateSloAvailabilityErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUT_CONFIGS_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
