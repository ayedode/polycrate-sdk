from typing import Literal

ApiV1BlockRolloutsUpdateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_BLOCK_ROLLOUTS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsUpdateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_block_rollouts_update_criticality_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsUpdateCriticalityErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_UPDATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
