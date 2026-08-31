from typing import Literal

ApiV1ProvidersCreateActiveErrorComponentAttr = Literal["active"]

API_V1_PROVIDERS_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProvidersCreateActiveErrorComponentAttr] = {
    "active",
}


def check_api_v1_providers_create_active_error_component_attr(
    value: str,
) -> ApiV1ProvidersCreateActiveErrorComponentAttr:
    if value in API_V1_PROVIDERS_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_CREATE_ACTIVE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
