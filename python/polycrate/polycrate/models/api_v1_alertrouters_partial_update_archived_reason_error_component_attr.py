from typing import Literal

ApiV1AlertroutersPartialUpdateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_ALERTROUTERS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersPartialUpdateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_alertrouters_partial_update_archived_reason_error_component_attr(
    value: str,
) -> ApiV1AlertroutersPartialUpdateArchivedReasonErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_PARTIAL_UPDATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
