from typing import Literal

ApiV1ConditionsArchiveCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_CONDITIONS_ARCHIVE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ConditionsArchiveCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_conditions_archive_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1ConditionsArchiveCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_CONDITIONS_ARCHIVE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONDITIONS_ARCHIVE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
