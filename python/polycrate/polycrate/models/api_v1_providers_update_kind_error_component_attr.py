from typing import Literal

ApiV1ProvidersUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_PROVIDERS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[ApiV1ProvidersUpdateKindErrorComponentAttr] = {
    "kind",
}


def check_api_v1_providers_update_kind_error_component_attr(value: str) -> ApiV1ProvidersUpdateKindErrorComponentAttr:
    if value in API_V1_PROVIDERS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
