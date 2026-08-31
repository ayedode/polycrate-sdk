from typing import Literal

ApiV1IpaddressesCreateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_IPADDRESSES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IpaddressesCreateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_ipaddresses_create_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1IpaddressesCreateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_IPADDRESSES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IPADDRESSES_CREATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
