from typing import Literal

ApiV1BlockRolloutsPartialUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlockRolloutsPartialUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_block_rollouts_partial_update_archived_error_component_attr(
    value: str,
) -> ApiV1BlockRolloutsPartialUpdateArchivedErrorComponentAttr:
    if value in API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCK_ROLLOUTS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
