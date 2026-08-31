from typing import Literal

ApiV1BlockRolloutsPartialUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsPartialUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_block_rollouts_partial_update_kind_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsPartialUpdateKindErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
