from typing import Literal

ApiV1BlockRolloutsCreateProviderErrorComponentCode = Literal["invalid_choice", "null"]

API_V1_BLOCK_ROLLOUTS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1BlockRolloutsCreateProviderErrorComponentCode
] = {
    "invalid_choice",
    "null",
}


def check_api_v1_block_rollouts_create_provider_error_component_code(
    value: str,
) -> ApiV1BlockRolloutsCreateProviderErrorComponentCode:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_PROVIDER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
