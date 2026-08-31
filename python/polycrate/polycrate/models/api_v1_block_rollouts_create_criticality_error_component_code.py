from typing import Literal

ApiV1BlockRolloutsCreateCriticalityErrorComponentCode = Literal["invalid_choice"]

API_V1_BLOCK_ROLLOUTS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsCreateCriticalityErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_block_rollouts_create_criticality_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsCreateCriticalityErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_CRITICALITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
