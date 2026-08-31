from typing import Literal

ApiV1RegistryRegistriesPartialUpdateNonFieldErrorsErrorComponentCode = Literal["invalid", "null"]

API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1RegistryRegistriesPartialUpdateNonFieldErrorsErrorComponentCode
] = {
    "invalid",
    "null",
}


def check_api_v1_registry_registries_partial_update_non_field_errors_error_component_code(
    value: str,
) -> ApiV1RegistryRegistriesPartialUpdateNonFieldErrorsErrorComponentCode:
    if value in API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_REGISTRY_REGISTRIES_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_CODE_VALUES!r}"
    )
