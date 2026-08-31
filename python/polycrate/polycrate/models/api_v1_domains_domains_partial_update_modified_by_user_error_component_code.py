from typing import Literal

ApiV1DomainsDomainsPartialUpdateModifiedByUserErrorComponentCode = Literal["does_not_exist", "incorrect_type"]

API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_MODIFIED_BY_USER_ERROR_COMPONENT_CODE_VALUES: set[
    ApiV1DomainsDomainsPartialUpdateModifiedByUserErrorComponentCode
] = {
    "does_not_exist",
    "incorrect_type",
}


def check_api_v1_domains_domains_partial_update_modified_by_user_error_component_code(
    value: str,
) -> ApiV1DomainsDomainsPartialUpdateModifiedByUserErrorComponentCode:
    if value in API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_MODIFIED_BY_USER_ERROR_COMPONENT_CODE_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_DOMAINS_DOMAINS_PARTIAL_UPDATE_MODIFIED_BY_USER_ERROR_COMPONENT_CODE_VALUES!r}"
    )
