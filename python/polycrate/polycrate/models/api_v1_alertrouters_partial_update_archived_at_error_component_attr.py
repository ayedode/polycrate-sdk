from typing import Literal

ApiV1AlertroutersPartialUpdateArchivedAtErrorComponentAttr = Literal["archived_at"]

API_V1_ALERTROUTERS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersPartialUpdateArchivedAtErrorComponentAttr
] = {
    "archived_at",
}


def check_api_v1_alertrouters_partial_update_archived_at_error_component_attr(
    value: str,
) -> ApiV1AlertroutersPartialUpdateArchivedAtErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_PARTIAL_UPDATE_ARCHIVED_AT_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
