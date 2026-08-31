from typing import Literal

ApiV1ContactgroupsListIdentityProvidersErrorComponentAttr = Literal["identity_providers"]

API_V1_CONTACTGROUPS_LIST_IDENTITY_PROVIDERS_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ContactgroupsListIdentityProvidersErrorComponentAttr
] = {
    "identity_providers",
}


def check_api_v1_contactgroups_list_identity_providers_error_component_attr(
    value: str,
) -> ApiV1ContactgroupsListIdentityProvidersErrorComponentAttr:
    if value in API_V1_CONTACTGROUPS_LIST_IDENTITY_PROVIDERS_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_CONTACTGROUPS_LIST_IDENTITY_PROVIDERS_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
