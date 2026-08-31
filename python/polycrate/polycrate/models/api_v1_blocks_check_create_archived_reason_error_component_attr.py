from typing import Literal

ApiV1BlocksCheckCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_BLOCKS_CHECK_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1BlocksCheckCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_blocks_check_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1BlocksCheckCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_BLOCKS_CHECK_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_BLOCKS_CHECK_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
