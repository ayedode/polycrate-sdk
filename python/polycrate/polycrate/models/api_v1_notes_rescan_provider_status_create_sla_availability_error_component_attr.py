from typing import Literal

ApiV1NotesRescanProviderStatusCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1NotesRescanProviderStatusCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_notes_rescan_provider_status_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1NotesRescanProviderStatusCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_NOTES_RESCAN_PROVIDER_STATUS_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
