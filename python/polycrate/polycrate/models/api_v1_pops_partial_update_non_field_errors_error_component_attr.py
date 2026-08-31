from typing import Literal

ApiV1PopsPartialUpdateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_POPS_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1PopsPartialUpdateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_pops_partial_update_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1PopsPartialUpdateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_POPS_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_POPS_PARTIAL_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
