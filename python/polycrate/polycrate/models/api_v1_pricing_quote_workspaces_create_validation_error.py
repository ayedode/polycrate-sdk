from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_quote_workspaces_create_annotations_error_component import (
        ApiV1PricingQuoteWorkspacesCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_archived_at_error_component import (
        ApiV1PricingQuoteWorkspacesCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_archived_error_component import (
        ApiV1PricingQuoteWorkspacesCreateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_archived_reason_error_component import (
        ApiV1PricingQuoteWorkspacesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_block_storage_gb_error_component import (
        ApiV1PricingQuoteWorkspacesCreateBlockStorageGbErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_block_storage_product_error_component import (
        ApiV1PricingQuoteWorkspacesCreateBlockStorageProductErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_block_storage_quoted_price_error_component import (
        ApiV1PricingQuoteWorkspacesCreateBlockStorageQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_cluster_product_error_component import (
        ApiV1PricingQuoteWorkspacesCreateClusterProductErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_cluster_quoted_price_error_component import (
        ApiV1PricingQuoteWorkspacesCreateClusterQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_criticality_error_component import (
        ApiV1PricingQuoteWorkspacesCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_debug_mode_error_component import (
        ApiV1PricingQuoteWorkspacesCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_display_name_error_component import (
        ApiV1PricingQuoteWorkspacesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_host_product_error_component import (
        ApiV1PricingQuoteWorkspacesCreateHostProductErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_host_quoted_price_error_component import (
        ApiV1PricingQuoteWorkspacesCreateHostQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_hosts_count_error_component import (
        ApiV1PricingQuoteWorkspacesCreateHostsCountErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_kind_error_component import (
        ApiV1PricingQuoteWorkspacesCreateKindErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_label_error_component import (
        ApiV1PricingQuoteWorkspacesCreateLabelErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_labels_error_component import (
        ApiV1PricingQuoteWorkspacesCreateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_loadbalancer_count_error_component import (
        ApiV1PricingQuoteWorkspacesCreateLoadbalancerCountErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_loadbalancer_product_error_component import (
        ApiV1PricingQuoteWorkspacesCreateLoadbalancerProductErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_loadbalancer_quoted_price_error_component import (
        ApiV1PricingQuoteWorkspacesCreateLoadbalancerQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_name_error_component import (
        ApiV1PricingQuoteWorkspacesCreateNameErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_non_field_errors_error_component import (
        ApiV1PricingQuoteWorkspacesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_object_storage_gb_error_component import (
        ApiV1PricingQuoteWorkspacesCreateObjectStorageGbErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_object_storage_product_error_component import (
        ApiV1PricingQuoteWorkspacesCreateObjectStorageProductErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_object_storage_quoted_price_error_component import (
        ApiV1PricingQuoteWorkspacesCreateObjectStorageQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_platform_service_error_component import (
        ApiV1PricingQuoteWorkspacesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_provider_error_component import (
        ApiV1PricingQuoteWorkspacesCreateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_provider_id_error_component import (
        ApiV1PricingQuoteWorkspacesCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_provider_reference_error_component import (
        ApiV1PricingQuoteWorkspacesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_quote_error_component import (
        ApiV1PricingQuoteWorkspacesCreateQuoteErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_reconciliation_enabled_error_component import (
        ApiV1PricingQuoteWorkspacesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_sla_availability_error_component import (
        ApiV1PricingQuoteWorkspacesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_sla_target_error_component import (
        ApiV1PricingQuoteWorkspacesCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_slo_availability_error_component import (
        ApiV1PricingQuoteWorkspacesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_slo_target_error_component import (
        ApiV1PricingQuoteWorkspacesCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_support_product_error_component import (
        ApiV1PricingQuoteWorkspacesCreateSupportProductErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_support_quoted_price_error_component import (
        ApiV1PricingQuoteWorkspacesCreateSupportQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_target_availability_error_component import (
        ApiV1PricingQuoteWorkspacesCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_tolerations_error_component import (
        ApiV1PricingQuoteWorkspacesCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_create_total_price_error_component import (
        ApiV1PricingQuoteWorkspacesCreateTotalPriceErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingQuoteWorkspacesCreateValidationError")


@_attrs_define
class ApiV1PricingQuoteWorkspacesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingQuoteWorkspacesCreateAnnotationsErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateArchivedAtErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateArchivedErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateArchivedReasonErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateBlockStorageGbErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateBlockStorageProductErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateBlockStorageQuotedPriceErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateClusterProductErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateClusterQuotedPriceErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateCriticalityErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateDebugModeErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateDisplayNameErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateHostProductErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateHostQuotedPriceErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateHostsCountErrorComponent | ApiV1PricingQuoteWorkspacesCreateKindErrorComponent
            | ApiV1PricingQuoteWorkspacesCreateLabelErrorComponent | ApiV1PricingQuoteWorkspacesCreateLabelsErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateLoadbalancerCountErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateLoadbalancerProductErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateLoadbalancerQuotedPriceErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateNameErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateNonFieldErrorsErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateObjectStorageGbErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateObjectStorageProductErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateObjectStorageQuotedPriceErrorComponent |
            ApiV1PricingQuoteWorkspacesCreatePlatformServiceErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateProviderErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateProviderIdErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateProviderReferenceErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateQuoteErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateReconciliationEnabledErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateSlaAvailabilityErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateSlaTargetErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateSloAvailabilityErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateSloTargetErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateSupportProductErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateSupportQuotedPriceErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateTargetAvailabilityErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateTolerationsErrorComponent |
            ApiV1PricingQuoteWorkspacesCreateTotalPriceErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingQuoteWorkspacesCreateAnnotationsErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateArchivedAtErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateArchivedErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateArchivedReasonErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateBlockStorageGbErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateBlockStorageProductErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateBlockStorageQuotedPriceErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateClusterProductErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateClusterQuotedPriceErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateCriticalityErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateDebugModeErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateDisplayNameErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateHostProductErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateHostQuotedPriceErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateHostsCountErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateKindErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateLabelErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateLabelsErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateLoadbalancerCountErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateLoadbalancerProductErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateLoadbalancerQuotedPriceErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateNameErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateNonFieldErrorsErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateObjectStorageGbErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateObjectStorageProductErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateObjectStorageQuotedPriceErrorComponent
        | ApiV1PricingQuoteWorkspacesCreatePlatformServiceErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateProviderErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateProviderIdErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateProviderReferenceErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateQuoteErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateReconciliationEnabledErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateSlaAvailabilityErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateSlaTargetErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateSloAvailabilityErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateSloTargetErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateSupportProductErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateSupportQuotedPriceErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateTargetAvailabilityErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateTolerationsErrorComponent
        | ApiV1PricingQuoteWorkspacesCreateTotalPriceErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_quote_workspaces_create_annotations_error_component import (
            ApiV1PricingQuoteWorkspacesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_archived_at_error_component import (
            ApiV1PricingQuoteWorkspacesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_archived_error_component import (
            ApiV1PricingQuoteWorkspacesCreateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_archived_reason_error_component import (
            ApiV1PricingQuoteWorkspacesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_block_storage_gb_error_component import (
            ApiV1PricingQuoteWorkspacesCreateBlockStorageGbErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_block_storage_product_error_component import (
            ApiV1PricingQuoteWorkspacesCreateBlockStorageProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_block_storage_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesCreateBlockStorageQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_cluster_product_error_component import (
            ApiV1PricingQuoteWorkspacesCreateClusterProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_cluster_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesCreateClusterQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_criticality_error_component import (
            ApiV1PricingQuoteWorkspacesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_debug_mode_error_component import (
            ApiV1PricingQuoteWorkspacesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_display_name_error_component import (
            ApiV1PricingQuoteWorkspacesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_host_product_error_component import (
            ApiV1PricingQuoteWorkspacesCreateHostProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_host_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesCreateHostQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_hosts_count_error_component import (
            ApiV1PricingQuoteWorkspacesCreateHostsCountErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_kind_error_component import (
            ApiV1PricingQuoteWorkspacesCreateKindErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_label_error_component import (
            ApiV1PricingQuoteWorkspacesCreateLabelErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_labels_error_component import (
            ApiV1PricingQuoteWorkspacesCreateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_loadbalancer_count_error_component import (
            ApiV1PricingQuoteWorkspacesCreateLoadbalancerCountErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_loadbalancer_product_error_component import (
            ApiV1PricingQuoteWorkspacesCreateLoadbalancerProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_loadbalancer_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesCreateLoadbalancerQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_name_error_component import (
            ApiV1PricingQuoteWorkspacesCreateNameErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_non_field_errors_error_component import (
            ApiV1PricingQuoteWorkspacesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_object_storage_gb_error_component import (
            ApiV1PricingQuoteWorkspacesCreateObjectStorageGbErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_object_storage_product_error_component import (
            ApiV1PricingQuoteWorkspacesCreateObjectStorageProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_object_storage_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesCreateObjectStorageQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_platform_service_error_component import (
            ApiV1PricingQuoteWorkspacesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_provider_error_component import (
            ApiV1PricingQuoteWorkspacesCreateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_provider_id_error_component import (
            ApiV1PricingQuoteWorkspacesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_provider_reference_error_component import (
            ApiV1PricingQuoteWorkspacesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_quote_error_component import (
            ApiV1PricingQuoteWorkspacesCreateQuoteErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_reconciliation_enabled_error_component import (
            ApiV1PricingQuoteWorkspacesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_sla_availability_error_component import (
            ApiV1PricingQuoteWorkspacesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_sla_target_error_component import (
            ApiV1PricingQuoteWorkspacesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_slo_availability_error_component import (
            ApiV1PricingQuoteWorkspacesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_slo_target_error_component import (
            ApiV1PricingQuoteWorkspacesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_support_product_error_component import (
            ApiV1PricingQuoteWorkspacesCreateSupportProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_support_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesCreateSupportQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_target_availability_error_component import (
            ApiV1PricingQuoteWorkspacesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_tolerations_error_component import (
            ApiV1PricingQuoteWorkspacesCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateQuoteErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateLabelErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateClusterProductErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateClusterQuotedPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateHostProductErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateHostsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateHostQuotedPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateSupportProductErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateSupportQuotedPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateObjectStorageProductErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateObjectStorageGbErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateObjectStorageQuotedPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateBlockStorageProductErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateBlockStorageGbErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateBlockStorageQuotedPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateLoadbalancerProductErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateLoadbalancerCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesCreateLoadbalancerQuotedPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_pricing_quote_workspaces_create_annotations_error_component import (
            ApiV1PricingQuoteWorkspacesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_archived_at_error_component import (
            ApiV1PricingQuoteWorkspacesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_archived_error_component import (
            ApiV1PricingQuoteWorkspacesCreateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_archived_reason_error_component import (
            ApiV1PricingQuoteWorkspacesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_block_storage_gb_error_component import (
            ApiV1PricingQuoteWorkspacesCreateBlockStorageGbErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_block_storage_product_error_component import (
            ApiV1PricingQuoteWorkspacesCreateBlockStorageProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_block_storage_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesCreateBlockStorageQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_cluster_product_error_component import (
            ApiV1PricingQuoteWorkspacesCreateClusterProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_cluster_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesCreateClusterQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_criticality_error_component import (
            ApiV1PricingQuoteWorkspacesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_debug_mode_error_component import (
            ApiV1PricingQuoteWorkspacesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_display_name_error_component import (
            ApiV1PricingQuoteWorkspacesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_host_product_error_component import (
            ApiV1PricingQuoteWorkspacesCreateHostProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_host_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesCreateHostQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_hosts_count_error_component import (
            ApiV1PricingQuoteWorkspacesCreateHostsCountErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_kind_error_component import (
            ApiV1PricingQuoteWorkspacesCreateKindErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_label_error_component import (
            ApiV1PricingQuoteWorkspacesCreateLabelErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_labels_error_component import (
            ApiV1PricingQuoteWorkspacesCreateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_loadbalancer_count_error_component import (
            ApiV1PricingQuoteWorkspacesCreateLoadbalancerCountErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_loadbalancer_product_error_component import (
            ApiV1PricingQuoteWorkspacesCreateLoadbalancerProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_loadbalancer_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesCreateLoadbalancerQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_name_error_component import (
            ApiV1PricingQuoteWorkspacesCreateNameErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_non_field_errors_error_component import (
            ApiV1PricingQuoteWorkspacesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_object_storage_gb_error_component import (
            ApiV1PricingQuoteWorkspacesCreateObjectStorageGbErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_object_storage_product_error_component import (
            ApiV1PricingQuoteWorkspacesCreateObjectStorageProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_object_storage_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesCreateObjectStorageQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_platform_service_error_component import (
            ApiV1PricingQuoteWorkspacesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_provider_error_component import (
            ApiV1PricingQuoteWorkspacesCreateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_provider_id_error_component import (
            ApiV1PricingQuoteWorkspacesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_provider_reference_error_component import (
            ApiV1PricingQuoteWorkspacesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_quote_error_component import (
            ApiV1PricingQuoteWorkspacesCreateQuoteErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_reconciliation_enabled_error_component import (
            ApiV1PricingQuoteWorkspacesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_sla_availability_error_component import (
            ApiV1PricingQuoteWorkspacesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_sla_target_error_component import (
            ApiV1PricingQuoteWorkspacesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_slo_availability_error_component import (
            ApiV1PricingQuoteWorkspacesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_slo_target_error_component import (
            ApiV1PricingQuoteWorkspacesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_support_product_error_component import (
            ApiV1PricingQuoteWorkspacesCreateSupportProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_support_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesCreateSupportQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_target_availability_error_component import (
            ApiV1PricingQuoteWorkspacesCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_tolerations_error_component import (
            ApiV1PricingQuoteWorkspacesCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_create_total_price_error_component import (
            ApiV1PricingQuoteWorkspacesCreateTotalPriceErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingQuoteWorkspacesCreateAnnotationsErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateArchivedAtErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateArchivedErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateArchivedReasonErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateBlockStorageGbErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateBlockStorageProductErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateBlockStorageQuotedPriceErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateClusterProductErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateClusterQuotedPriceErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateCriticalityErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateDebugModeErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateDisplayNameErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateHostProductErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateHostQuotedPriceErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateHostsCountErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateKindErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateLabelErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateLabelsErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateLoadbalancerCountErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateLoadbalancerProductErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateLoadbalancerQuotedPriceErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateNameErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateNonFieldErrorsErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateObjectStorageGbErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateObjectStorageProductErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateObjectStorageQuotedPriceErrorComponent
                | ApiV1PricingQuoteWorkspacesCreatePlatformServiceErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateProviderErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateProviderIdErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateProviderReferenceErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateQuoteErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateReconciliationEnabledErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateSlaAvailabilityErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateSlaTargetErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateSloAvailabilityErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateSloTargetErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateSupportProductErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateSupportQuotedPriceErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateTargetAvailabilityErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateTolerationsErrorComponent
                | ApiV1PricingQuoteWorkspacesCreateTotalPriceErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_0 = (
                        ApiV1PricingQuoteWorkspacesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_1 = (
                        ApiV1PricingQuoteWorkspacesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_2 = (
                        ApiV1PricingQuoteWorkspacesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_3 = (
                        ApiV1PricingQuoteWorkspacesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_4 = (
                        ApiV1PricingQuoteWorkspacesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_5 = (
                        ApiV1PricingQuoteWorkspacesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_6 = (
                        ApiV1PricingQuoteWorkspacesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_7 = (
                        ApiV1PricingQuoteWorkspacesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_8 = (
                        ApiV1PricingQuoteWorkspacesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_9 = (
                        ApiV1PricingQuoteWorkspacesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_10 = (
                        ApiV1PricingQuoteWorkspacesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_11 = (
                        ApiV1PricingQuoteWorkspacesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_12 = (
                        ApiV1PricingQuoteWorkspacesCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_13 = (
                        ApiV1PricingQuoteWorkspacesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_14 = (
                        ApiV1PricingQuoteWorkspacesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_15 = (
                        ApiV1PricingQuoteWorkspacesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_16 = (
                        ApiV1PricingQuoteWorkspacesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_17 = (
                        ApiV1PricingQuoteWorkspacesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_18 = (
                        ApiV1PricingQuoteWorkspacesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_19 = (
                        ApiV1PricingQuoteWorkspacesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_20 = (
                        ApiV1PricingQuoteWorkspacesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_21 = (
                        ApiV1PricingQuoteWorkspacesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_22 = (
                        ApiV1PricingQuoteWorkspacesCreateQuoteErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_23 = (
                        ApiV1PricingQuoteWorkspacesCreateLabelErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_24 = (
                        ApiV1PricingQuoteWorkspacesCreateClusterProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_25 = (
                        ApiV1PricingQuoteWorkspacesCreateClusterQuotedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_26 = (
                        ApiV1PricingQuoteWorkspacesCreateHostProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_27 = (
                        ApiV1PricingQuoteWorkspacesCreateHostsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_28 = (
                        ApiV1PricingQuoteWorkspacesCreateHostQuotedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_29 = (
                        ApiV1PricingQuoteWorkspacesCreateSupportProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_30 = (
                        ApiV1PricingQuoteWorkspacesCreateSupportQuotedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_31 = (
                        ApiV1PricingQuoteWorkspacesCreateObjectStorageProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_32 = (
                        ApiV1PricingQuoteWorkspacesCreateObjectStorageGbErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_33 = (
                        ApiV1PricingQuoteWorkspacesCreateObjectStorageQuotedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_34 = (
                        ApiV1PricingQuoteWorkspacesCreateBlockStorageProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_35 = (
                        ApiV1PricingQuoteWorkspacesCreateBlockStorageGbErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_36 = (
                        ApiV1PricingQuoteWorkspacesCreateBlockStorageQuotedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_37 = (
                        ApiV1PricingQuoteWorkspacesCreateLoadbalancerProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_38 = (
                        ApiV1PricingQuoteWorkspacesCreateLoadbalancerCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_39 = (
                        ApiV1PricingQuoteWorkspacesCreateLoadbalancerQuotedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_40 = (
                    ApiV1PricingQuoteWorkspacesCreateTotalPriceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_quote_workspaces_create_error_type_40

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_quote_workspaces_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_quote_workspaces_create_validation_error.additional_properties = d
        return api_v1_pricing_quote_workspaces_create_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
