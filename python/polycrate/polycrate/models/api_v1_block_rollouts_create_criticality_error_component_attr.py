from typing import Literal

ApiV1BlockRolloutsCreateCriticalityErrorComponentAttr = Literal["criticality"]

API_V1_BLOCK_ROLLOUTS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsCreateCriticalityErrorComponentAttr
] = {
    "criticality",
}


def check_api_v1_block_rollouts_create_criticality_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsCreateCriticalityErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_CRITICALITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
