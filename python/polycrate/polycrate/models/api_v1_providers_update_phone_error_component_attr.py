from typing import Literal

ApiV1ProvidersUpdatePhoneErrorComponentAttr = Literal["phone"]

API_V1_PROVIDERS_UPDATE_PHONE_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProvidersUpdatePhoneErrorComponentAttr] = {
    "phone",
}


def check_api_v1_providers_update_phone_error_component_attr(value: str) -> ApiV1ProvidersUpdatePhoneErrorComponentAttr:
    if value in API_V1_PROVIDERS_UPDATE_PHONE_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_PHONE_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
