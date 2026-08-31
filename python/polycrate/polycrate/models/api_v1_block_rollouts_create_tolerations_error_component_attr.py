from typing import Literal

ApiV1BlockRolloutsCreateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_BLOCK_ROLLOUTS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsCreateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_block_rollouts_create_tolerations_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsCreateTolerationsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
