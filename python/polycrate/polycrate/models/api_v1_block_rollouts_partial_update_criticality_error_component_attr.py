from typing import Literal

ApiV1BlockRolloutsPartialUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsPartialUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_block_rollouts_partial_update_criticality_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsPartialUpdateCriticalityErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
