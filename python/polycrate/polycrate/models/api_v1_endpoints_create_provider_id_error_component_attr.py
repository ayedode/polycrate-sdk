from typing import Literal

ApiV1EndpointsCreateProviderIdErrorComponentAttr = Literal["provider_id"]

API_V1_ENDPOINTS_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1EndpointsCreateProviderIdErrorComponentAttr
] = {
    "provider_id",
}


def check_api_v1_endpoints_create_provider_id_error_component_attr(
    value: str,
) -> ApiV1EndpointsCreateProviderIdErrorComponentAttr:
    if value in API_V1_ENDPOINTS_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_ENDPOINTS_CREATE_PROVIDER_ID_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
