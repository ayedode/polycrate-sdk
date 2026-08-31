from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_quote_workspaces_partial_update_annotations_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_archived_at_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_archived_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_archived_reason_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_block_storage_gb_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageGbErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_block_storage_product_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageProductErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_block_storage_quoted_price_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_cluster_product_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateClusterProductErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_cluster_quoted_price_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateClusterQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_criticality_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_debug_mode_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_display_name_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_host_product_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateHostProductErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_host_quoted_price_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateHostQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_hosts_count_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateHostsCountErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_kind_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_label_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateLabelErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_labels_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_loadbalancer_count_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerCountErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_loadbalancer_product_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerProductErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_loadbalancer_quoted_price_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_name_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_non_field_errors_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_object_storage_gb_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageGbErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_object_storage_product_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageProductErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_object_storage_quoted_price_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_platform_service_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_provider_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_provider_id_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_provider_reference_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_quote_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateQuoteErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_reconciliation_enabled_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_sla_availability_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_sla_target_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_slo_availability_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_slo_target_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_support_product_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateSupportProductErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_support_quoted_price_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateSupportQuotedPriceErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_target_availability_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_tolerations_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_pricing_quote_workspaces_partial_update_total_price_error_component import (
        ApiV1PricingQuoteWorkspacesPartialUpdateTotalPriceErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingQuoteWorkspacesPartialUpdateValidationError")


@_attrs_define
class ApiV1PricingQuoteWorkspacesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingQuoteWorkspacesPartialUpdateAnnotationsErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateArchivedAtErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateArchivedErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateArchivedReasonErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageGbErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageProductErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageQuotedPriceErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateClusterProductErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateClusterQuotedPriceErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateCriticalityErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateDebugModeErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateDisplayNameErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateHostProductErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateHostQuotedPriceErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateHostsCountErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateKindErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateLabelErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateLabelsErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerCountErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerProductErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerQuotedPriceErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateNameErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageGbErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageProductErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageQuotedPriceErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdatePlatformServiceErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateProviderErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateProviderIdErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateProviderReferenceErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateQuoteErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateSlaTargetErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateSloAvailabilityErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateSloTargetErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateSupportProductErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateSupportQuotedPriceErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateTolerationsErrorComponent |
            ApiV1PricingQuoteWorkspacesPartialUpdateTotalPriceErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingQuoteWorkspacesPartialUpdateAnnotationsErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateArchivedAtErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateArchivedErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateArchivedReasonErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageGbErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageProductErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageQuotedPriceErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateClusterProductErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateClusterQuotedPriceErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateCriticalityErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateDebugModeErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateDisplayNameErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateHostProductErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateHostQuotedPriceErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateHostsCountErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateKindErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateLabelErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateLabelsErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerCountErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerProductErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerQuotedPriceErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateNameErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageGbErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageProductErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageQuotedPriceErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdatePlatformServiceErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateProviderErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateProviderIdErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateProviderReferenceErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateQuoteErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateSlaTargetErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateSloAvailabilityErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateSloTargetErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateSupportProductErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateSupportQuotedPriceErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateTolerationsErrorComponent
        | ApiV1PricingQuoteWorkspacesPartialUpdateTotalPriceErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_quote_workspaces_partial_update_annotations_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_archived_at_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_archived_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_archived_reason_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_block_storage_gb_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageGbErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_block_storage_product_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_block_storage_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_cluster_product_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateClusterProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_cluster_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateClusterQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_criticality_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_debug_mode_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_display_name_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_host_product_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateHostProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_host_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateHostQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_hosts_count_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateHostsCountErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_kind_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_label_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateLabelErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_labels_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_loadbalancer_count_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerCountErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_loadbalancer_product_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_loadbalancer_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_name_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_non_field_errors_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_object_storage_gb_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageGbErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_object_storage_product_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_object_storage_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_platform_service_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_provider_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_provider_id_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_provider_reference_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_quote_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateQuoteErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_reconciliation_enabled_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_sla_availability_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_sla_target_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_slo_availability_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_slo_target_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_support_product_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateSupportProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_support_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateSupportQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_target_availability_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_tolerations_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateQuoteErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateLabelErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateClusterProductErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateClusterQuotedPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateHostProductErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateHostsCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateHostQuotedPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateSupportProductErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateSupportQuotedPriceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageProductErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageGbErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageQuotedPriceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageProductErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageGbErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageQuotedPriceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerProductErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerCountErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerQuotedPriceErrorComponent
            ):
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
        from ..models.api_v1_pricing_quote_workspaces_partial_update_annotations_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_archived_at_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_archived_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_archived_reason_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_block_storage_gb_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageGbErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_block_storage_product_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_block_storage_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_cluster_product_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateClusterProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_cluster_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateClusterQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_criticality_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_debug_mode_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_display_name_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_host_product_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateHostProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_host_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateHostQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_hosts_count_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateHostsCountErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_kind_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_label_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateLabelErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_labels_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_loadbalancer_count_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerCountErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_loadbalancer_product_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_loadbalancer_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_name_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_non_field_errors_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_object_storage_gb_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageGbErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_object_storage_product_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_object_storage_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_platform_service_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_provider_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_provider_id_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_provider_reference_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_quote_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateQuoteErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_reconciliation_enabled_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_sla_availability_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_sla_target_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_slo_availability_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_slo_target_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_support_product_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateSupportProductErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_support_quoted_price_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateSupportQuotedPriceErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_target_availability_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_tolerations_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_pricing_quote_workspaces_partial_update_total_price_error_component import (
            ApiV1PricingQuoteWorkspacesPartialUpdateTotalPriceErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingQuoteWorkspacesPartialUpdateAnnotationsErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateArchivedAtErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateArchivedErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateArchivedReasonErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageGbErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageProductErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageQuotedPriceErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateClusterProductErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateClusterQuotedPriceErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateCriticalityErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateDebugModeErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateDisplayNameErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateHostProductErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateHostQuotedPriceErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateHostsCountErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateKindErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateLabelErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateLabelsErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerCountErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerProductErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerQuotedPriceErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateNameErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageGbErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageProductErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageQuotedPriceErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdatePlatformServiceErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateProviderErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateProviderIdErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateProviderReferenceErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateQuoteErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateSlaTargetErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateSloAvailabilityErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateSloTargetErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateSupportProductErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateSupportQuotedPriceErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateTolerationsErrorComponent
                | ApiV1PricingQuoteWorkspacesPartialUpdateTotalPriceErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_0 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_1 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_2 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_3 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_4 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_5 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_6 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_7 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_8 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_9 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_10 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_11 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_12 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_13 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_14 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_15 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_16 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_17 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_18 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_19 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_20 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_21 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_22 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateQuoteErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_23 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateLabelErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_24 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateClusterProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_25 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateClusterQuotedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_26 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateHostProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_27 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateHostsCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_28 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateHostQuotedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_29 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateSupportProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_30 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateSupportQuotedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_31 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_32 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageGbErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_33 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateObjectStorageQuotedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_34 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_35 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageGbErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_36 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateBlockStorageQuotedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_37 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerProductErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_38 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerCountErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_39 = (
                        ApiV1PricingQuoteWorkspacesPartialUpdateLoadbalancerQuotedPriceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_40 = (
                    ApiV1PricingQuoteWorkspacesPartialUpdateTotalPriceErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_quote_workspaces_partial_update_error_type_40

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_quote_workspaces_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_quote_workspaces_partial_update_validation_error.additional_properties = d
        return api_v1_pricing_quote_workspaces_partial_update_validation_error

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
