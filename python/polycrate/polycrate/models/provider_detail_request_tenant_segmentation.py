from typing import Literal

ProviderDetailRequestTenantSegmentation = Literal["no", "planned", "unknown", "yes"]

PROVIDER_DETAIL_REQUEST_TENANT_SEGMENTATION_VALUES: set[ProviderDetailRequestTenantSegmentation] = {
    "no",
    "planned",
    "unknown",
    "yes",
}


def check_provider_detail_request_tenant_segmentation(value: str) -> ProviderDetailRequestTenantSegmentation:
    if value in PROVIDER_DETAIL_REQUEST_TENANT_SEGMENTATION_VALUES:
        return value
    raise TypeError(
        f"Unexpected value {value!r}. Expected one of {PROVIDER_DETAIL_REQUEST_TENANT_SEGMENTATION_VALUES!r}"
    )
