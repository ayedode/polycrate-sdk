from typing import Literal

ApiV1ProvidersCreateArchivedReasonErrorComponentAttr = Literal["archived_reason"]

API_V1_PROVIDERS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES: set[
    ApiV1ProvidersCreateArchivedReasonErrorComponentAttr
] = {
    "archived_reason",
}


def check_api_v1_providers_create_archived_reason_error_component_attr(
    value: str,
) -> ApiV1ProvidersCreateArchivedReasonErrorComponentAttr:
    if value in API_V1_PROVIDERS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {API_V1_PROVIDERS_CREATE_ARCHIVED_REASON_ERROR_COMPONENT_ATTR_VALUES!r}"
    )
