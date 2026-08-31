from typing import Literal

ApiV1BlockRolloutsArchiveCreateSlaTargetErrorComponentAttr = Literal["sla_target"]

API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsArchiveCreateSlaTargetErrorComponentAttr
] = {
    "sla_target",
}


def check_api_v1_block_rollouts_archive_create_sla_target_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsArchiveCreateSlaTargetErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_ARCHIVE_CREATE_SLA_TARGET_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
