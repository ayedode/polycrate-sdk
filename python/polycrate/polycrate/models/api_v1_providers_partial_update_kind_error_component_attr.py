from typing import Literal

ApiV1ProvidersPartialUpdateKindErrorComponentAttr = Literal["kind"]

API_V1_PROVIDERS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersPartialUpdateKindErrorComponentAttr
] = {
    "kind",
}


def check_api_v1_providers_partial_update_kind_error_component_attr(
    value: str,
) -> ApiV1ProvidersPartialUpdateKindErrorComponentAttr:
    if value in API_V1_PROVIDERS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_PARTIAL_UPDATE_KIND_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
