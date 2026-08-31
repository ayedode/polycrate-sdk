from typing import Literal

ApiV1RegistryRegistriesPartialUpdateSloAvailabilityErrorComponentCode = Literal[
    "invalid", "max_decimal_places", "max_digits", "max_string_length", "max_whole_digits", "null"
]

API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesPartialUpdateSloAvailabilityErrorComponentCode
] = {
    "invalid",
    "max_decimal_places",
    "max_digits",
    "max_string_length",
    "max_whole_digits",
    "null",
}


def check_api_v1_registry_registries_partial_update_slo_availability_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesPartialUpdateSloAvailabilityErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_SLO_AVAILABILITY_ERROR_COMPONENT_CODE_VALUES!r}"
    )
