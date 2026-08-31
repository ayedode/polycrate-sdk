from typing import Literal

ApiV1ExternalCredentialsCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_EXTERNAL_CREDENTIALS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ExternalCredentialsCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_external_credentials_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1ExternalCredentialsCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_EXTERNAL_CREDENTIALS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_EXTERNAL_CREDENTIALS_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
