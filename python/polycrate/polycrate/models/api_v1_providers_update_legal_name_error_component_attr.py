from typing import Literal

ApiV1ProvidersUpdateLegalNameErrorComponentAttr = Literal["legal_name"]

API_V1_PROVIDERS_UPDATE_LEGAL_NAME_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProvidersUpdateLegalNameErrorComponentAttr] = {
    "legal_name",
}


def check_api_v1_providers_update_legal_name_error_component_attr(
    value: str,
) -> ApiV1ProvidersUpdateLegalNameErrorComponentAttr:
    if value in API_V1_PROVIDERS_UPDATE_LEGAL_NAME_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_LEGAL_NAME_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
