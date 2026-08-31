from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_cost_statements_create_annotations_error_component import (
        ApiV1PricingCostStatementsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_archived_at_error_component import (
        ApiV1PricingCostStatementsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_archived_error_component import (
        ApiV1PricingCostStatementsCreateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_archived_reason_error_component import (
        ApiV1PricingCostStatementsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_criticality_error_component import (
        ApiV1PricingCostStatementsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_currency_error_component import (
        ApiV1PricingCostStatementsCreateCurrencyErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_debug_mode_error_component import (
        ApiV1PricingCostStatementsCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_display_name_error_component import (
        ApiV1PricingCostStatementsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_external_invoice_id_error_component import (
        ApiV1PricingCostStatementsCreateExternalInvoiceIdErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_generated_at_error_component import (
        ApiV1PricingCostStatementsCreateGeneratedAtErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_generated_by_error_component import (
        ApiV1PricingCostStatementsCreateGeneratedByErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_is_manual_error_component import (
        ApiV1PricingCostStatementsCreateIsManualErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_kind_error_component import (
        ApiV1PricingCostStatementsCreateKindErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_labels_error_component import (
        ApiV1PricingCostStatementsCreateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_name_error_component import (
        ApiV1PricingCostStatementsCreateNameErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_non_field_errors_error_component import (
        ApiV1PricingCostStatementsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_period_end_error_component import (
        ApiV1PricingCostStatementsCreatePeriodEndErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_period_start_error_component import (
        ApiV1PricingCostStatementsCreatePeriodStartErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_platform_service_error_component import (
        ApiV1PricingCostStatementsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_provider_error_component import (
        ApiV1PricingCostStatementsCreateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_provider_id_error_component import (
        ApiV1PricingCostStatementsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_provider_reference_error_component import (
        ApiV1PricingCostStatementsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_reconciliation_enabled_error_component import (
        ApiV1PricingCostStatementsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_sla_availability_error_component import (
        ApiV1PricingCostStatementsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_sla_target_error_component import (
        ApiV1PricingCostStatementsCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_slo_availability_error_component import (
        ApiV1PricingCostStatementsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_slo_target_error_component import (
        ApiV1PricingCostStatementsCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_status_error_component import (
        ApiV1PricingCostStatementsCreateStatusErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_target_availability_error_component import (
        ApiV1PricingCostStatementsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_tolerations_error_component import (
        ApiV1PricingCostStatementsCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_create_total_net_error_component import (
        ApiV1PricingCostStatementsCreateTotalNetErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingCostStatementsCreateValidationError")


@_attrs_define
class ApiV1PricingCostStatementsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingCostStatementsCreateAnnotationsErrorComponent |
            ApiV1PricingCostStatementsCreateArchivedAtErrorComponent |
            ApiV1PricingCostStatementsCreateArchivedErrorComponent |
            ApiV1PricingCostStatementsCreateArchivedReasonErrorComponent |
            ApiV1PricingCostStatementsCreateCriticalityErrorComponent |
            ApiV1PricingCostStatementsCreateCurrencyErrorComponent | ApiV1PricingCostStatementsCreateDebugModeErrorComponent
            | ApiV1PricingCostStatementsCreateDisplayNameErrorComponent |
            ApiV1PricingCostStatementsCreateExternalInvoiceIdErrorComponent |
            ApiV1PricingCostStatementsCreateGeneratedAtErrorComponent |
            ApiV1PricingCostStatementsCreateGeneratedByErrorComponent |
            ApiV1PricingCostStatementsCreateIsManualErrorComponent | ApiV1PricingCostStatementsCreateKindErrorComponent |
            ApiV1PricingCostStatementsCreateLabelsErrorComponent | ApiV1PricingCostStatementsCreateNameErrorComponent |
            ApiV1PricingCostStatementsCreateNonFieldErrorsErrorComponent |
            ApiV1PricingCostStatementsCreatePeriodEndErrorComponent |
            ApiV1PricingCostStatementsCreatePeriodStartErrorComponent |
            ApiV1PricingCostStatementsCreatePlatformServiceErrorComponent |
            ApiV1PricingCostStatementsCreateProviderErrorComponent |
            ApiV1PricingCostStatementsCreateProviderIdErrorComponent |
            ApiV1PricingCostStatementsCreateProviderReferenceErrorComponent |
            ApiV1PricingCostStatementsCreateReconciliationEnabledErrorComponent |
            ApiV1PricingCostStatementsCreateSlaAvailabilityErrorComponent |
            ApiV1PricingCostStatementsCreateSlaTargetErrorComponent |
            ApiV1PricingCostStatementsCreateSloAvailabilityErrorComponent |
            ApiV1PricingCostStatementsCreateSloTargetErrorComponent | ApiV1PricingCostStatementsCreateStatusErrorComponent |
            ApiV1PricingCostStatementsCreateTargetAvailabilityErrorComponent |
            ApiV1PricingCostStatementsCreateTolerationsErrorComponent |
            ApiV1PricingCostStatementsCreateTotalNetErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingCostStatementsCreateAnnotationsErrorComponent
        | ApiV1PricingCostStatementsCreateArchivedAtErrorComponent
        | ApiV1PricingCostStatementsCreateArchivedErrorComponent
        | ApiV1PricingCostStatementsCreateArchivedReasonErrorComponent
        | ApiV1PricingCostStatementsCreateCriticalityErrorComponent
        | ApiV1PricingCostStatementsCreateCurrencyErrorComponent
        | ApiV1PricingCostStatementsCreateDebugModeErrorComponent
        | ApiV1PricingCostStatementsCreateDisplayNameErrorComponent
        | ApiV1PricingCostStatementsCreateExternalInvoiceIdErrorComponent
        | ApiV1PricingCostStatementsCreateGeneratedAtErrorComponent
        | ApiV1PricingCostStatementsCreateGeneratedByErrorComponent
        | ApiV1PricingCostStatementsCreateIsManualErrorComponent
        | ApiV1PricingCostStatementsCreateKindErrorComponent
        | ApiV1PricingCostStatementsCreateLabelsErrorComponent
        | ApiV1PricingCostStatementsCreateNameErrorComponent
        | ApiV1PricingCostStatementsCreateNonFieldErrorsErrorComponent
        | ApiV1PricingCostStatementsCreatePeriodEndErrorComponent
        | ApiV1PricingCostStatementsCreatePeriodStartErrorComponent
        | ApiV1PricingCostStatementsCreatePlatformServiceErrorComponent
        | ApiV1PricingCostStatementsCreateProviderErrorComponent
        | ApiV1PricingCostStatementsCreateProviderIdErrorComponent
        | ApiV1PricingCostStatementsCreateProviderReferenceErrorComponent
        | ApiV1PricingCostStatementsCreateReconciliationEnabledErrorComponent
        | ApiV1PricingCostStatementsCreateSlaAvailabilityErrorComponent
        | ApiV1PricingCostStatementsCreateSlaTargetErrorComponent
        | ApiV1PricingCostStatementsCreateSloAvailabilityErrorComponent
        | ApiV1PricingCostStatementsCreateSloTargetErrorComponent
        | ApiV1PricingCostStatementsCreateStatusErrorComponent
        | ApiV1PricingCostStatementsCreateTargetAvailabilityErrorComponent
        | ApiV1PricingCostStatementsCreateTolerationsErrorComponent
        | ApiV1PricingCostStatementsCreateTotalNetErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_cost_statements_create_annotations_error_component import (
            ApiV1PricingCostStatementsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_archived_at_error_component import (
            ApiV1PricingCostStatementsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_archived_error_component import (
            ApiV1PricingCostStatementsCreateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_archived_reason_error_component import (
            ApiV1PricingCostStatementsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_criticality_error_component import (
            ApiV1PricingCostStatementsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_currency_error_component import (
            ApiV1PricingCostStatementsCreateCurrencyErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_debug_mode_error_component import (
            ApiV1PricingCostStatementsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_display_name_error_component import (
            ApiV1PricingCostStatementsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_external_invoice_id_error_component import (
            ApiV1PricingCostStatementsCreateExternalInvoiceIdErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_generated_at_error_component import (
            ApiV1PricingCostStatementsCreateGeneratedAtErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_generated_by_error_component import (
            ApiV1PricingCostStatementsCreateGeneratedByErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_kind_error_component import (
            ApiV1PricingCostStatementsCreateKindErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_labels_error_component import (
            ApiV1PricingCostStatementsCreateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_name_error_component import (
            ApiV1PricingCostStatementsCreateNameErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_non_field_errors_error_component import (
            ApiV1PricingCostStatementsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_period_end_error_component import (
            ApiV1PricingCostStatementsCreatePeriodEndErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_period_start_error_component import (
            ApiV1PricingCostStatementsCreatePeriodStartErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_platform_service_error_component import (
            ApiV1PricingCostStatementsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_provider_error_component import (
            ApiV1PricingCostStatementsCreateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_provider_id_error_component import (
            ApiV1PricingCostStatementsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_provider_reference_error_component import (
            ApiV1PricingCostStatementsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_reconciliation_enabled_error_component import (
            ApiV1PricingCostStatementsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_sla_availability_error_component import (
            ApiV1PricingCostStatementsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_sla_target_error_component import (
            ApiV1PricingCostStatementsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_slo_availability_error_component import (
            ApiV1PricingCostStatementsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_slo_target_error_component import (
            ApiV1PricingCostStatementsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_status_error_component import (
            ApiV1PricingCostStatementsCreateStatusErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_target_availability_error_component import (
            ApiV1PricingCostStatementsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_tolerations_error_component import (
            ApiV1PricingCostStatementsCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_total_net_error_component import (
            ApiV1PricingCostStatementsCreateTotalNetErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingCostStatementsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreatePeriodStartErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreatePeriodEndErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateTotalNetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateCurrencyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateExternalInvoiceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateGeneratedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsCreateGeneratedByErrorComponent):
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
        from ..models.api_v1_pricing_cost_statements_create_annotations_error_component import (
            ApiV1PricingCostStatementsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_archived_at_error_component import (
            ApiV1PricingCostStatementsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_archived_error_component import (
            ApiV1PricingCostStatementsCreateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_archived_reason_error_component import (
            ApiV1PricingCostStatementsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_criticality_error_component import (
            ApiV1PricingCostStatementsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_currency_error_component import (
            ApiV1PricingCostStatementsCreateCurrencyErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_debug_mode_error_component import (
            ApiV1PricingCostStatementsCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_display_name_error_component import (
            ApiV1PricingCostStatementsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_external_invoice_id_error_component import (
            ApiV1PricingCostStatementsCreateExternalInvoiceIdErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_generated_at_error_component import (
            ApiV1PricingCostStatementsCreateGeneratedAtErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_generated_by_error_component import (
            ApiV1PricingCostStatementsCreateGeneratedByErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_is_manual_error_component import (
            ApiV1PricingCostStatementsCreateIsManualErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_kind_error_component import (
            ApiV1PricingCostStatementsCreateKindErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_labels_error_component import (
            ApiV1PricingCostStatementsCreateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_name_error_component import (
            ApiV1PricingCostStatementsCreateNameErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_non_field_errors_error_component import (
            ApiV1PricingCostStatementsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_period_end_error_component import (
            ApiV1PricingCostStatementsCreatePeriodEndErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_period_start_error_component import (
            ApiV1PricingCostStatementsCreatePeriodStartErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_platform_service_error_component import (
            ApiV1PricingCostStatementsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_provider_error_component import (
            ApiV1PricingCostStatementsCreateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_provider_id_error_component import (
            ApiV1PricingCostStatementsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_provider_reference_error_component import (
            ApiV1PricingCostStatementsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_reconciliation_enabled_error_component import (
            ApiV1PricingCostStatementsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_sla_availability_error_component import (
            ApiV1PricingCostStatementsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_sla_target_error_component import (
            ApiV1PricingCostStatementsCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_slo_availability_error_component import (
            ApiV1PricingCostStatementsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_slo_target_error_component import (
            ApiV1PricingCostStatementsCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_status_error_component import (
            ApiV1PricingCostStatementsCreateStatusErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_target_availability_error_component import (
            ApiV1PricingCostStatementsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_tolerations_error_component import (
            ApiV1PricingCostStatementsCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_create_total_net_error_component import (
            ApiV1PricingCostStatementsCreateTotalNetErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingCostStatementsCreateAnnotationsErrorComponent
                | ApiV1PricingCostStatementsCreateArchivedAtErrorComponent
                | ApiV1PricingCostStatementsCreateArchivedErrorComponent
                | ApiV1PricingCostStatementsCreateArchivedReasonErrorComponent
                | ApiV1PricingCostStatementsCreateCriticalityErrorComponent
                | ApiV1PricingCostStatementsCreateCurrencyErrorComponent
                | ApiV1PricingCostStatementsCreateDebugModeErrorComponent
                | ApiV1PricingCostStatementsCreateDisplayNameErrorComponent
                | ApiV1PricingCostStatementsCreateExternalInvoiceIdErrorComponent
                | ApiV1PricingCostStatementsCreateGeneratedAtErrorComponent
                | ApiV1PricingCostStatementsCreateGeneratedByErrorComponent
                | ApiV1PricingCostStatementsCreateIsManualErrorComponent
                | ApiV1PricingCostStatementsCreateKindErrorComponent
                | ApiV1PricingCostStatementsCreateLabelsErrorComponent
                | ApiV1PricingCostStatementsCreateNameErrorComponent
                | ApiV1PricingCostStatementsCreateNonFieldErrorsErrorComponent
                | ApiV1PricingCostStatementsCreatePeriodEndErrorComponent
                | ApiV1PricingCostStatementsCreatePeriodStartErrorComponent
                | ApiV1PricingCostStatementsCreatePlatformServiceErrorComponent
                | ApiV1PricingCostStatementsCreateProviderErrorComponent
                | ApiV1PricingCostStatementsCreateProviderIdErrorComponent
                | ApiV1PricingCostStatementsCreateProviderReferenceErrorComponent
                | ApiV1PricingCostStatementsCreateReconciliationEnabledErrorComponent
                | ApiV1PricingCostStatementsCreateSlaAvailabilityErrorComponent
                | ApiV1PricingCostStatementsCreateSlaTargetErrorComponent
                | ApiV1PricingCostStatementsCreateSloAvailabilityErrorComponent
                | ApiV1PricingCostStatementsCreateSloTargetErrorComponent
                | ApiV1PricingCostStatementsCreateStatusErrorComponent
                | ApiV1PricingCostStatementsCreateTargetAvailabilityErrorComponent
                | ApiV1PricingCostStatementsCreateTolerationsErrorComponent
                | ApiV1PricingCostStatementsCreateTotalNetErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_0 = (
                        ApiV1PricingCostStatementsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_1 = (
                        ApiV1PricingCostStatementsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_2 = (
                        ApiV1PricingCostStatementsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_3 = (
                        ApiV1PricingCostStatementsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_4 = (
                        ApiV1PricingCostStatementsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_5 = (
                        ApiV1PricingCostStatementsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_6 = (
                        ApiV1PricingCostStatementsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_7 = (
                        ApiV1PricingCostStatementsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_8 = (
                        ApiV1PricingCostStatementsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_9 = (
                        ApiV1PricingCostStatementsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_10 = (
                        ApiV1PricingCostStatementsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_11 = (
                        ApiV1PricingCostStatementsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_12 = (
                        ApiV1PricingCostStatementsCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_13 = (
                        ApiV1PricingCostStatementsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_14 = (
                        ApiV1PricingCostStatementsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_15 = (
                        ApiV1PricingCostStatementsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_16 = (
                        ApiV1PricingCostStatementsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_17 = (
                        ApiV1PricingCostStatementsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_18 = (
                        ApiV1PricingCostStatementsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_19 = (
                        ApiV1PricingCostStatementsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_20 = (
                        ApiV1PricingCostStatementsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_21 = (
                        ApiV1PricingCostStatementsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_22 = (
                        ApiV1PricingCostStatementsCreatePeriodStartErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_23 = (
                        ApiV1PricingCostStatementsCreatePeriodEndErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_24 = (
                        ApiV1PricingCostStatementsCreateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_25 = (
                        ApiV1PricingCostStatementsCreateTotalNetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_26 = (
                        ApiV1PricingCostStatementsCreateCurrencyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_27 = (
                        ApiV1PricingCostStatementsCreateExternalInvoiceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_28 = (
                        ApiV1PricingCostStatementsCreateGeneratedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_create_error_type_29 = (
                        ApiV1PricingCostStatementsCreateGeneratedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_cost_statements_create_error_type_30 = (
                    ApiV1PricingCostStatementsCreateIsManualErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_cost_statements_create_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_cost_statements_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_cost_statements_create_validation_error.additional_properties = d
        return api_v1_pricing_cost_statements_create_validation_error

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
