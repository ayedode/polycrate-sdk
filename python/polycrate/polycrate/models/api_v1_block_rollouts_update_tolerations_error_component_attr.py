from typing import Literal

ApiV1BlockRolloutsUpdateTolerationsErrorComponentAttr = Literal["tolerations"]

API_V1_BLOCK_ROLLOUTS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsUpdateTolerationsErrorComponentAttr
] = {
    "tolerations",
}


def check_api_v1_block_rollouts_update_tolerations_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsUpdateTolerationsErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_UPDATE_TOLERATIONS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
