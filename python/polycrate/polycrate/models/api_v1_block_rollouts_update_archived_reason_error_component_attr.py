from typing import Literal

ApiV1BlockRolloutsUpdateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_BLOCK_ROLLOUTS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsUpdateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_block_rollouts_update_archived_reason_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsUpdateArchivedReasonErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
