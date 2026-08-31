from typing import Literal

ApiV1OrganizationsCreateProviderErrorComponentAttr = Literal["provider"]

API_V1_ORGANIZATIONS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1OrganizationsCreateProviderErrorComponentAttr
] = {
    "provider",
}


def check_api_v1_organizations_create_provider_error_component_attr(
    value: str,
) -> ApiV1OrganizationsCreateProviderErrorComponentAttr:
    if value in API_V1_ORGANIZATIONS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ORGANIZATIONS_CREATE_PROVIDER_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
