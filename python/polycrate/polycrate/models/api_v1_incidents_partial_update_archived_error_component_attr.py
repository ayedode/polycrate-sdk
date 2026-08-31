from typing import Literal

ApiV1IncidentsPartialUpdateArchivedErrorComponentAttr = Literal["archived"]

API_V1_INCIDENTS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsPartialUpdateArchivedErrorComponentAttr
] = {
    "archived",
}


def check_api_v1_incidents_partial_update_archived_error_component_attr(
    value: str,
) -> ApiV1IncidentsPartialUpdateArchivedErrorComponentAttr:
    if value in API_V1_INCIDENTS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_PARTIAL_UPDATE_ARCHIVED_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
