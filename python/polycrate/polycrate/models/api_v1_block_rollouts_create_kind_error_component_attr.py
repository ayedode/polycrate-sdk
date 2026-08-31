from typing import Literal

ApiV1BlockRolloutsCreateKindErrorComponentAttr = Literal["kind"]

API_V1_BLOCK_ROLLOUTS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1BlockRolloutsCreateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_block_rollouts_create_kind_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsCreateKindErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
