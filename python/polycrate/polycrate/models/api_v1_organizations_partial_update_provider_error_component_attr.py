from typing import Literal

ApiV1OrganizationsPartialUpdateProviderErrorComponentAttr = Literal["provider"]

API_V1_ORGANIZATIONS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsPartialUpdateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_organizations_partial_update_provider_error_component_attr(
    value: str,
) -> ApiV1OrganizationsPartialUpdateProviderErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_PARTIAL_UPDATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
