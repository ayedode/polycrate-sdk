from typing import Literal

ApiV1BlockRolloutsArchiveCreateSloTargetErrorComponentAttr = Literal["slo_target"]

API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsArchiveCreateSloTargetErrorComponentAttr
] = {
    "slo_target",
}


def check_api_v1_block_rollouts_archive_create_slo_target_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsArchiveCreateSloTargetErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_SLO_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
