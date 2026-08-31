from typing import Literal

ApiV1IdpIdentityprovidersListTimeRangeErrorComponentAttr = Literal["time_range"]

API_V1_IDP_IDENTITYPROVIDERS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1IdpIdentityprovidersListTimeRangeErrorComponentAttr
] = {
    "time_range",
}


def check_api_v1_idp_identityproviders_list_time_range_error_component_attr(
    value: str,
) -> ApiV1IdpIdentityprovidersListTimeRangeErrorComponentAttr:
    if value in API_V1_IDP_IDENTITYPROVIDERS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_LIST_TIME_RANGE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
