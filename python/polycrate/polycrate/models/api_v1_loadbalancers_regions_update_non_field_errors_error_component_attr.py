from typing import Literal

ApiV1LoadbalancersRegionsUpdateNonFieldErrorsErrorComponentAttr = Literal["non_field_errors"]

API_V1_LOADBALANCERS_REGIONS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1LoadbalancersRegionsUpdateNonFieldErrorsErrorComponentAttr
] = {
    "non_field_errors",
}


def check_api_v1_loadbalancers_regions_update_non_field_errors_error_component_attr(
    value: str,
) -> ApiV1LoadbalancersRegionsUpdateNonFieldErrorsErrorComponentAttr:
    if value in API_V1_LOADBALANCERS_REGIONS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_LOADBALANCERS_REGIONS_UPDATE_NON_FIELD_ERRORS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
