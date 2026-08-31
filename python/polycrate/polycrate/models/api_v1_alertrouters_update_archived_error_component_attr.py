from typing import Literal

ApiV1AlertroutersUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_ALERTROUTERS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_alertrouters_update_archived_error_component_attr(
    value: str,
) -> ApiV1AlertroutersUpdateArchivedErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
