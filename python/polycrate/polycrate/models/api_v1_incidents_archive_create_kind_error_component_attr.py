from typing import Literal

ApiV1IncidentsArchiveCreateKindErrorComponentAttr = Literal["kind"]

API_V1_INCIDENTS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IncidentsArchiveCreateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_incidents_archive_create_kind_error_component_attr(
    value: str,
) -> ApiV1IncidentsArchiveCreateKindErrorComponentAttr:
    if value in API_V1_INCIDENTS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_INCIDENTS_ARCHIVE_CREATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
