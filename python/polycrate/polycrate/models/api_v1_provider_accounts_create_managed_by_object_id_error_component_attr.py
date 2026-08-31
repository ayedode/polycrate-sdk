from typing import Literal

ApiV1ProviderAccountsCreateManagedByObjectIdErrorComponentAttr = Literal["managed_by_object_id"]

API_V1_PROVIDER_ACCOUNTS_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProviderAccountsCreateManagedByObjectIdErrorComponentAttr
] = {
    "managed_by_object_id",
}


def check_api_v1_provider_accounts_create_managed_by_object_id_error_component_attr(
    value: str,
) -> ApiV1ProviderAccountsCreateManagedByObjectIdErrorComponentAttr:
    if value in API_V1_PROVIDER_ACCOUNTS_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDER_ACCOUNTS_CREATE_MANAGED_BY_OBJECT_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
