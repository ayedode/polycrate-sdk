from typing import Literal

ApiV1BlockRolloutsPartialUpdateStatusErrorComponentAttr = Literal["status"]

API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsPartialUpdateStatusErrorComponentAttr
] = {
    "status",
}


def check_api_v1_block_rollouts_partial_update_status_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsPartialUpdateStatusErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_STATUS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
