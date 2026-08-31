from typing import Literal

ApiV1CredentialsArchiveCreateSloAvailabilityErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits", "null"
]

API_V1_CREDENTIALS_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1CredentialsArchiveCreateSloAvailabilityErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
    "null",
}


def check_api_v1_credentials_archive_create_slo_availability_error_component_code(
    value: str,
) -> ApiV1CredentialsArchiveCreateSloAvailabilityErrorComponentCode:
    if value in API_V1_CREDENTIALS_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CREDENTIALS_ARCHIVE_CREATE_SLO_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
