from typing import Literal

ApiV1IdpIdentityprovidersListTimeRangeErrorComponentCode = Literal["invalid_choice"]

API_V1_IDP_IDENTITYPROVIDERS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1IdpIdentityprovidersListTimeRangeErrorComponentCode
] = {
    "invalid_choice",
}


def check_api_v1_idp_identityproviders_list_time_range_error_component_code(
    value: str,
) -> ApiV1IdpIdentityprovidersListTimeRangeErrorComponentCode:
    if value in API_V1_IDP_IDENTITYPROVIDERS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_IDP_IDENTITYPROVIDERS_LIST_TIME_RANGE_ERROR_COMPONENT_CODE_VALUES!r}"
    )
