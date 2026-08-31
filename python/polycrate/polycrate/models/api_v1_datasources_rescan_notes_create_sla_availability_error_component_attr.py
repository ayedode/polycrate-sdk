from typing import Literal

ApiV1DatasourcesRescanNotesCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_DATASOURCES_RESCAN_NOTES_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1DatasourcesRescanNotesCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_datasources_rescan_notes_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1DatasourcesRescanNotesCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_DATASOURCES_RESCAN_NOTES_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DATASOURCES_RESCAN_NOTES_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
