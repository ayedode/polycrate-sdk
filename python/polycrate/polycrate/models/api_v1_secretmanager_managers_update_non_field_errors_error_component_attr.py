from typing import Literal

ApiV1SecretmanagerManagersUpdateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_SECRETMANAGER_MANAGERS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1SecretmanagerManagersUpdateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_secretmanager_managers_update_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1SecretmanagerManagersUpdateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_SECRETMANAGER_MANAGERS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_SECRETMANAGER_MANAGERS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
