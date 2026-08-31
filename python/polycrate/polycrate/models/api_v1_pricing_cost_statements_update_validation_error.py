from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_cost_statements_update_annotations_error_component import (
        ApiV1PricingCostStatementsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_archived_at_error_component import (
        ApiV1PricingCostStatementsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_archived_error_component import (
        ApiV1PricingCostStatementsUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_archived_reason_error_component import (
        ApiV1PricingCostStatementsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_criticality_error_component import (
        ApiV1PricingCostStatementsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_currency_error_component import (
        ApiV1PricingCostStatementsUpdateCurrencyErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_debug_mode_error_component import (
        ApiV1PricingCostStatementsUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_display_name_error_component import (
        ApiV1PricingCostStatementsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_external_invoice_id_error_component import (
        ApiV1PricingCostStatementsUpdateExternalInvoiceIdErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_generated_at_error_component import (
        ApiV1PricingCostStatementsUpdateGeneratedAtErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_generated_by_error_component import (
        ApiV1PricingCostStatementsUpdateGeneratedByErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_is_manual_error_component import (
        ApiV1PricingCostStatementsUpdateIsManualErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_kind_error_component import (
        ApiV1PricingCostStatementsUpdateKindErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_labels_error_component import (
        ApiV1PricingCostStatementsUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_name_error_component import (
        ApiV1PricingCostStatementsUpdateNameErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_non_field_errors_error_component import (
        ApiV1PricingCostStatementsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_period_end_error_component import (
        ApiV1PricingCostStatementsUpdatePeriodEndErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_period_start_error_component import (
        ApiV1PricingCostStatementsUpdatePeriodStartErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_platform_service_error_component import (
        ApiV1PricingCostStatementsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_provider_error_component import (
        ApiV1PricingCostStatementsUpdateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_provider_id_error_component import (
        ApiV1PricingCostStatementsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_provider_reference_error_component import (
        ApiV1PricingCostStatementsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_reconciliation_enabled_error_component import (
        ApiV1PricingCostStatementsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_sla_availability_error_component import (
        ApiV1PricingCostStatementsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_sla_target_error_component import (
        ApiV1PricingCostStatementsUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_slo_availability_error_component import (
        ApiV1PricingCostStatementsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_slo_target_error_component import (
        ApiV1PricingCostStatementsUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_status_error_component import (
        ApiV1PricingCostStatementsUpdateStatusErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_target_availability_error_component import (
        ApiV1PricingCostStatementsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_tolerations_error_component import (
        ApiV1PricingCostStatementsUpdateTolerationsErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_update_total_net_error_component import (
        ApiV1PricingCostStatementsUpdateTotalNetErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingCostStatementsUpdateValidationError")


@_attrs_define
class ApiV1PricingCostStatementsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingCostStatementsUpdateAnnotationsErrorComponent |
            ApiV1PricingCostStatementsUpdateArchivedAtErrorComponent |
            ApiV1PricingCostStatementsUpdateArchivedErrorComponent |
            ApiV1PricingCostStatementsUpdateArchivedReasonErrorComponent |
            ApiV1PricingCostStatementsUpdateCriticalityErrorComponent |
            ApiV1PricingCostStatementsUpdateCurrencyErrorComponent | ApiV1PricingCostStatementsUpdateDebugModeErrorComponent
            | ApiV1PricingCostStatementsUpdateDisplayNameErrorComponent |
            ApiV1PricingCostStatementsUpdateExternalInvoiceIdErrorComponent |
            ApiV1PricingCostStatementsUpdateGeneratedAtErrorComponent |
            ApiV1PricingCostStatementsUpdateGeneratedByErrorComponent |
            ApiV1PricingCostStatementsUpdateIsManualErrorComponent | ApiV1PricingCostStatementsUpdateKindErrorComponent |
            ApiV1PricingCostStatementsUpdateLabelsErrorComponent | ApiV1PricingCostStatementsUpdateNameErrorComponent |
            ApiV1PricingCostStatementsUpdateNonFieldErrorsErrorComponent |
            ApiV1PricingCostStatementsUpdatePeriodEndErrorComponent |
            ApiV1PricingCostStatementsUpdatePeriodStartErrorComponent |
            ApiV1PricingCostStatementsUpdatePlatformServiceErrorComponent |
            ApiV1PricingCostStatementsUpdateProviderErrorComponent |
            ApiV1PricingCostStatementsUpdateProviderIdErrorComponent |
            ApiV1PricingCostStatementsUpdateProviderReferenceErrorComponent |
            ApiV1PricingCostStatementsUpdateReconciliationEnabledErrorComponent |
            ApiV1PricingCostStatementsUpdateSlaAvailabilityErrorComponent |
            ApiV1PricingCostStatementsUpdateSlaTargetErrorComponent |
            ApiV1PricingCostStatementsUpdateSloAvailabilityErrorComponent |
            ApiV1PricingCostStatementsUpdateSloTargetErrorComponent | ApiV1PricingCostStatementsUpdateStatusErrorComponent |
            ApiV1PricingCostStatementsUpdateTargetAvailabilityErrorComponent |
            ApiV1PricingCostStatementsUpdateTolerationsErrorComponent |
            ApiV1PricingCostStatementsUpdateTotalNetErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingCostStatementsUpdateAnnotationsErrorComponent
        | ApiV1PricingCostStatementsUpdateArchivedAtErrorComponent
        | ApiV1PricingCostStatementsUpdateArchivedErrorComponent
        | ApiV1PricingCostStatementsUpdateArchivedReasonErrorComponent
        | ApiV1PricingCostStatementsUpdateCriticalityErrorComponent
        | ApiV1PricingCostStatementsUpdateCurrencyErrorComponent
        | ApiV1PricingCostStatementsUpdateDebugModeErrorComponent
        | ApiV1PricingCostStatementsUpdateDisplayNameErrorComponent
        | ApiV1PricingCostStatementsUpdateExternalInvoiceIdErrorComponent
        | ApiV1PricingCostStatementsUpdateGeneratedAtErrorComponent
        | ApiV1PricingCostStatementsUpdateGeneratedByErrorComponent
        | ApiV1PricingCostStatementsUpdateIsManualErrorComponent
        | ApiV1PricingCostStatementsUpdateKindErrorComponent
        | ApiV1PricingCostStatementsUpdateLabelsErrorComponent
        | ApiV1PricingCostStatementsUpdateNameErrorComponent
        | ApiV1PricingCostStatementsUpdateNonFieldErrorsErrorComponent
        | ApiV1PricingCostStatementsUpdatePeriodEndErrorComponent
        | ApiV1PricingCostStatementsUpdatePeriodStartErrorComponent
        | ApiV1PricingCostStatementsUpdatePlatformServiceErrorComponent
        | ApiV1PricingCostStatementsUpdateProviderErrorComponent
        | ApiV1PricingCostStatementsUpdateProviderIdErrorComponent
        | ApiV1PricingCostStatementsUpdateProviderReferenceErrorComponent
        | ApiV1PricingCostStatementsUpdateReconciliationEnabledErrorComponent
        | ApiV1PricingCostStatementsUpdateSlaAvailabilityErrorComponent
        | ApiV1PricingCostStatementsUpdateSlaTargetErrorComponent
        | ApiV1PricingCostStatementsUpdateSloAvailabilityErrorComponent
        | ApiV1PricingCostStatementsUpdateSloTargetErrorComponent
        | ApiV1PricingCostStatementsUpdateStatusErrorComponent
        | ApiV1PricingCostStatementsUpdateTargetAvailabilityErrorComponent
        | ApiV1PricingCostStatementsUpdateTolerationsErrorComponent
        | ApiV1PricingCostStatementsUpdateTotalNetErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_cost_statements_update_annotations_error_component import (
            ApiV1PricingCostStatementsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_archived_at_error_component import (
            ApiV1PricingCostStatementsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_archived_error_component import (
            ApiV1PricingCostStatementsUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_archived_reason_error_component import (
            ApiV1PricingCostStatementsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_criticality_error_component import (
            ApiV1PricingCostStatementsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_currency_error_component import (
            ApiV1PricingCostStatementsUpdateCurrencyErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_debug_mode_error_component import (
            ApiV1PricingCostStatementsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_display_name_error_component import (
            ApiV1PricingCostStatementsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_external_invoice_id_error_component import (
            ApiV1PricingCostStatementsUpdateExternalInvoiceIdErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_generated_at_error_component import (
            ApiV1PricingCostStatementsUpdateGeneratedAtErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_generated_by_error_component import (
            ApiV1PricingCostStatementsUpdateGeneratedByErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_kind_error_component import (
            ApiV1PricingCostStatementsUpdateKindErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_labels_error_component import (
            ApiV1PricingCostStatementsUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_name_error_component import (
            ApiV1PricingCostStatementsUpdateNameErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_non_field_errors_error_component import (
            ApiV1PricingCostStatementsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_period_end_error_component import (
            ApiV1PricingCostStatementsUpdatePeriodEndErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_period_start_error_component import (
            ApiV1PricingCostStatementsUpdatePeriodStartErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_platform_service_error_component import (
            ApiV1PricingCostStatementsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_provider_error_component import (
            ApiV1PricingCostStatementsUpdateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_provider_id_error_component import (
            ApiV1PricingCostStatementsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_provider_reference_error_component import (
            ApiV1PricingCostStatementsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_reconciliation_enabled_error_component import (
            ApiV1PricingCostStatementsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_sla_availability_error_component import (
            ApiV1PricingCostStatementsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_sla_target_error_component import (
            ApiV1PricingCostStatementsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_slo_availability_error_component import (
            ApiV1PricingCostStatementsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_slo_target_error_component import (
            ApiV1PricingCostStatementsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_status_error_component import (
            ApiV1PricingCostStatementsUpdateStatusErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_target_availability_error_component import (
            ApiV1PricingCostStatementsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_tolerations_error_component import (
            ApiV1PricingCostStatementsUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_total_net_error_component import (
            ApiV1PricingCostStatementsUpdateTotalNetErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdatePeriodStartErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdatePeriodEndErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateTotalNetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateCurrencyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateExternalInvoiceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateGeneratedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsUpdateGeneratedByErrorComponent):
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
        from ..models.api_v1_pricing_cost_statements_update_annotations_error_component import (
            ApiV1PricingCostStatementsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_archived_at_error_component import (
            ApiV1PricingCostStatementsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_archived_error_component import (
            ApiV1PricingCostStatementsUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_archived_reason_error_component import (
            ApiV1PricingCostStatementsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_criticality_error_component import (
            ApiV1PricingCostStatementsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_currency_error_component import (
            ApiV1PricingCostStatementsUpdateCurrencyErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_debug_mode_error_component import (
            ApiV1PricingCostStatementsUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_display_name_error_component import (
            ApiV1PricingCostStatementsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_external_invoice_id_error_component import (
            ApiV1PricingCostStatementsUpdateExternalInvoiceIdErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_generated_at_error_component import (
            ApiV1PricingCostStatementsUpdateGeneratedAtErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_generated_by_error_component import (
            ApiV1PricingCostStatementsUpdateGeneratedByErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_is_manual_error_component import (
            ApiV1PricingCostStatementsUpdateIsManualErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_kind_error_component import (
            ApiV1PricingCostStatementsUpdateKindErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_labels_error_component import (
            ApiV1PricingCostStatementsUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_name_error_component import (
            ApiV1PricingCostStatementsUpdateNameErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_non_field_errors_error_component import (
            ApiV1PricingCostStatementsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_period_end_error_component import (
            ApiV1PricingCostStatementsUpdatePeriodEndErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_period_start_error_component import (
            ApiV1PricingCostStatementsUpdatePeriodStartErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_platform_service_error_component import (
            ApiV1PricingCostStatementsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_provider_error_component import (
            ApiV1PricingCostStatementsUpdateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_provider_id_error_component import (
            ApiV1PricingCostStatementsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_provider_reference_error_component import (
            ApiV1PricingCostStatementsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_reconciliation_enabled_error_component import (
            ApiV1PricingCostStatementsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_sla_availability_error_component import (
            ApiV1PricingCostStatementsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_sla_target_error_component import (
            ApiV1PricingCostStatementsUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_slo_availability_error_component import (
            ApiV1PricingCostStatementsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_slo_target_error_component import (
            ApiV1PricingCostStatementsUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_status_error_component import (
            ApiV1PricingCostStatementsUpdateStatusErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_target_availability_error_component import (
            ApiV1PricingCostStatementsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_tolerations_error_component import (
            ApiV1PricingCostStatementsUpdateTolerationsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_update_total_net_error_component import (
            ApiV1PricingCostStatementsUpdateTotalNetErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingCostStatementsUpdateAnnotationsErrorComponent
                | ApiV1PricingCostStatementsUpdateArchivedAtErrorComponent
                | ApiV1PricingCostStatementsUpdateArchivedErrorComponent
                | ApiV1PricingCostStatementsUpdateArchivedReasonErrorComponent
                | ApiV1PricingCostStatementsUpdateCriticalityErrorComponent
                | ApiV1PricingCostStatementsUpdateCurrencyErrorComponent
                | ApiV1PricingCostStatementsUpdateDebugModeErrorComponent
                | ApiV1PricingCostStatementsUpdateDisplayNameErrorComponent
                | ApiV1PricingCostStatementsUpdateExternalInvoiceIdErrorComponent
                | ApiV1PricingCostStatementsUpdateGeneratedAtErrorComponent
                | ApiV1PricingCostStatementsUpdateGeneratedByErrorComponent
                | ApiV1PricingCostStatementsUpdateIsManualErrorComponent
                | ApiV1PricingCostStatementsUpdateKindErrorComponent
                | ApiV1PricingCostStatementsUpdateLabelsErrorComponent
                | ApiV1PricingCostStatementsUpdateNameErrorComponent
                | ApiV1PricingCostStatementsUpdateNonFieldErrorsErrorComponent
                | ApiV1PricingCostStatementsUpdatePeriodEndErrorComponent
                | ApiV1PricingCostStatementsUpdatePeriodStartErrorComponent
                | ApiV1PricingCostStatementsUpdatePlatformServiceErrorComponent
                | ApiV1PricingCostStatementsUpdateProviderErrorComponent
                | ApiV1PricingCostStatementsUpdateProviderIdErrorComponent
                | ApiV1PricingCostStatementsUpdateProviderReferenceErrorComponent
                | ApiV1PricingCostStatementsUpdateReconciliationEnabledErrorComponent
                | ApiV1PricingCostStatementsUpdateSlaAvailabilityErrorComponent
                | ApiV1PricingCostStatementsUpdateSlaTargetErrorComponent
                | ApiV1PricingCostStatementsUpdateSloAvailabilityErrorComponent
                | ApiV1PricingCostStatementsUpdateSloTargetErrorComponent
                | ApiV1PricingCostStatementsUpdateStatusErrorComponent
                | ApiV1PricingCostStatementsUpdateTargetAvailabilityErrorComponent
                | ApiV1PricingCostStatementsUpdateTolerationsErrorComponent
                | ApiV1PricingCostStatementsUpdateTotalNetErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_0 = (
                        ApiV1PricingCostStatementsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_1 = (
                        ApiV1PricingCostStatementsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_2 = (
                        ApiV1PricingCostStatementsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_3 = (
                        ApiV1PricingCostStatementsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_4 = (
                        ApiV1PricingCostStatementsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_5 = (
                        ApiV1PricingCostStatementsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_6 = (
                        ApiV1PricingCostStatementsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_7 = (
                        ApiV1PricingCostStatementsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_8 = (
                        ApiV1PricingCostStatementsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_9 = (
                        ApiV1PricingCostStatementsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_10 = (
                        ApiV1PricingCostStatementsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_11 = (
                        ApiV1PricingCostStatementsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_12 = (
                        ApiV1PricingCostStatementsUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_13 = (
                        ApiV1PricingCostStatementsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_14 = (
                        ApiV1PricingCostStatementsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_15 = (
                        ApiV1PricingCostStatementsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_16 = (
                        ApiV1PricingCostStatementsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_17 = (
                        ApiV1PricingCostStatementsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_18 = (
                        ApiV1PricingCostStatementsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_19 = (
                        ApiV1PricingCostStatementsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_20 = (
                        ApiV1PricingCostStatementsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_21 = (
                        ApiV1PricingCostStatementsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_22 = (
                        ApiV1PricingCostStatementsUpdatePeriodStartErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_23 = (
                        ApiV1PricingCostStatementsUpdatePeriodEndErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_24 = (
                        ApiV1PricingCostStatementsUpdateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_25 = (
                        ApiV1PricingCostStatementsUpdateTotalNetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_26 = (
                        ApiV1PricingCostStatementsUpdateCurrencyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_27 = (
                        ApiV1PricingCostStatementsUpdateExternalInvoiceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_28 = (
                        ApiV1PricingCostStatementsUpdateGeneratedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_update_error_type_29 = (
                        ApiV1PricingCostStatementsUpdateGeneratedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_cost_statements_update_error_type_30 = (
                    ApiV1PricingCostStatementsUpdateIsManualErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_cost_statements_update_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_cost_statements_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_cost_statements_update_validation_error.additional_properties = d
        return api_v1_pricing_cost_statements_update_validation_error

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
