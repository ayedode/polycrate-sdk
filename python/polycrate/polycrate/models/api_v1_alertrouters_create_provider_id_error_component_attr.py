from typing import Literal

ApiV1AlertroutersCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_ALERTROUTERS_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1AlertroutersCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_alertrouters_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1AlertroutersCreateProviderIdErrorComponentAttr:
    if value in API_V1_ALERTROUTERS_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ALERTROUTERS_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
