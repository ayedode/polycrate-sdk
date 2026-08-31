from typing import Literal

ApiV1AlertcategoriesArchiveCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertcategoriesArchiveCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_alertcategories_archive_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1AlertcategoriesArchiveCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTCATEGORIES_ARCHIVE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
