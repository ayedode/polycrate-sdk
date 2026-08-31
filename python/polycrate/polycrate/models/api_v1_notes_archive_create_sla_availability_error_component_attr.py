from typing import Literal

ApiV1NotesArchiveCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_NOTES_ARCHIVE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesArchiveCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_notes_archive_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1NotesArchiveCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_NOTES_ARCHIVE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_ARCHIVE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
