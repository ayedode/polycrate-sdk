from typing import Literal

ApiV1CredentialsArchiveCreateSlaAvailabilityErrorComponentAttr = Literal["sla_availability"]

API_V1_CREDENTIALS_ARCHIVE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CredentialsArchiveCreateSlaAvailabilityErrorComponentAttr
] = {
    "sla_availability",
}


def check_api_v1_credentials_archive_create_sla_availability_error_component_attr(
    value: str,
) -> ApiV1CredentialsArchiveCreateSlaAvailabilityErrorComponentAttr:
    if value in API_V1_CREDENTIALS_ARCHIVE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_ARCHIVE_CREATE_SLA_AVAILABILITY_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
