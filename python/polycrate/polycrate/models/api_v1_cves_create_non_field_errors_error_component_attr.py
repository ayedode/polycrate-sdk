from typing import Literal

ApiV1CvesCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_CVES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1CvesCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_cves_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1CvesCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_CVES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CVES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
