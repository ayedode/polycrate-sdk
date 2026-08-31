from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_cost_statements_archive_create_annotations_error_component import (
        ApiV1PricingCostStatementsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_archived_at_error_component import (
        ApiV1PricingCostStatementsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_archived_error_component import (
        ApiV1PricingCostStatementsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_archived_reason_error_component import (
        ApiV1PricingCostStatementsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_criticality_error_component import (
        ApiV1PricingCostStatementsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_currency_error_component import (
        ApiV1PricingCostStatementsArchiveCreateCurrencyErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_debug_mode_error_component import (
        ApiV1PricingCostStatementsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_display_name_error_component import (
        ApiV1PricingCostStatementsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_external_invoice_id_error_component import (
        ApiV1PricingCostStatementsArchiveCreateExternalInvoiceIdErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_generated_at_error_component import (
        ApiV1PricingCostStatementsArchiveCreateGeneratedAtErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_generated_by_error_component import (
        ApiV1PricingCostStatementsArchiveCreateGeneratedByErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_is_manual_error_component import (
        ApiV1PricingCostStatementsArchiveCreateIsManualErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_kind_error_component import (
        ApiV1PricingCostStatementsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_labels_error_component import (
        ApiV1PricingCostStatementsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_name_error_component import (
        ApiV1PricingCostStatementsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_non_field_errors_error_component import (
        ApiV1PricingCostStatementsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_period_end_error_component import (
        ApiV1PricingCostStatementsArchiveCreatePeriodEndErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_period_start_error_component import (
        ApiV1PricingCostStatementsArchiveCreatePeriodStartErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_platform_service_error_component import (
        ApiV1PricingCostStatementsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_provider_error_component import (
        ApiV1PricingCostStatementsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_provider_id_error_component import (
        ApiV1PricingCostStatementsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_provider_reference_error_component import (
        ApiV1PricingCostStatementsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_reconciliation_enabled_error_component import (
        ApiV1PricingCostStatementsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_sla_availability_error_component import (
        ApiV1PricingCostStatementsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_sla_target_error_component import (
        ApiV1PricingCostStatementsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_slo_availability_error_component import (
        ApiV1PricingCostStatementsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_slo_target_error_component import (
        ApiV1PricingCostStatementsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_status_error_component import (
        ApiV1PricingCostStatementsArchiveCreateStatusErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_target_availability_error_component import (
        ApiV1PricingCostStatementsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_tolerations_error_component import (
        ApiV1PricingCostStatementsArchiveCreateTolerationsErrorComponent,
    )
    from ..models.api_v1_pricing_cost_statements_archive_create_total_net_error_component import (
        ApiV1PricingCostStatementsArchiveCreateTotalNetErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingCostStatementsArchiveCreateValidationError")


@_attrs_define
class ApiV1PricingCostStatementsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingCostStatementsArchiveCreateAnnotationsErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateArchivedAtErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateArchivedErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateArchivedReasonErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateCriticalityErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateCurrencyErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateDebugModeErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateDisplayNameErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateExternalInvoiceIdErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateGeneratedAtErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateGeneratedByErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateIsManualErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateKindErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateLabelsErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateNameErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1PricingCostStatementsArchiveCreatePeriodEndErrorComponent |
            ApiV1PricingCostStatementsArchiveCreatePeriodStartErrorComponent |
            ApiV1PricingCostStatementsArchiveCreatePlatformServiceErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateProviderErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateProviderIdErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateProviderReferenceErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateSlaTargetErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateSloAvailabilityErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateSloTargetErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateStatusErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateTolerationsErrorComponent |
            ApiV1PricingCostStatementsArchiveCreateTotalNetErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingCostStatementsArchiveCreateAnnotationsErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateArchivedAtErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateArchivedErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateArchivedReasonErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateCriticalityErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateCurrencyErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateDebugModeErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateDisplayNameErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateExternalInvoiceIdErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateGeneratedAtErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateGeneratedByErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateIsManualErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateKindErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateLabelsErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateNameErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1PricingCostStatementsArchiveCreatePeriodEndErrorComponent
        | ApiV1PricingCostStatementsArchiveCreatePeriodStartErrorComponent
        | ApiV1PricingCostStatementsArchiveCreatePlatformServiceErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateProviderErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateProviderIdErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateProviderReferenceErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateSlaTargetErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateSloTargetErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateStatusErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateTolerationsErrorComponent
        | ApiV1PricingCostStatementsArchiveCreateTotalNetErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_cost_statements_archive_create_annotations_error_component import (
            ApiV1PricingCostStatementsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_archived_at_error_component import (
            ApiV1PricingCostStatementsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_archived_error_component import (
            ApiV1PricingCostStatementsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_archived_reason_error_component import (
            ApiV1PricingCostStatementsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_criticality_error_component import (
            ApiV1PricingCostStatementsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_currency_error_component import (
            ApiV1PricingCostStatementsArchiveCreateCurrencyErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_debug_mode_error_component import (
            ApiV1PricingCostStatementsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_display_name_error_component import (
            ApiV1PricingCostStatementsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_external_invoice_id_error_component import (
            ApiV1PricingCostStatementsArchiveCreateExternalInvoiceIdErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_generated_at_error_component import (
            ApiV1PricingCostStatementsArchiveCreateGeneratedAtErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_generated_by_error_component import (
            ApiV1PricingCostStatementsArchiveCreateGeneratedByErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_kind_error_component import (
            ApiV1PricingCostStatementsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_labels_error_component import (
            ApiV1PricingCostStatementsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_name_error_component import (
            ApiV1PricingCostStatementsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_non_field_errors_error_component import (
            ApiV1PricingCostStatementsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_period_end_error_component import (
            ApiV1PricingCostStatementsArchiveCreatePeriodEndErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_period_start_error_component import (
            ApiV1PricingCostStatementsArchiveCreatePeriodStartErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_platform_service_error_component import (
            ApiV1PricingCostStatementsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_provider_error_component import (
            ApiV1PricingCostStatementsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_provider_id_error_component import (
            ApiV1PricingCostStatementsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_provider_reference_error_component import (
            ApiV1PricingCostStatementsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_reconciliation_enabled_error_component import (
            ApiV1PricingCostStatementsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_sla_availability_error_component import (
            ApiV1PricingCostStatementsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_sla_target_error_component import (
            ApiV1PricingCostStatementsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_slo_availability_error_component import (
            ApiV1PricingCostStatementsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_slo_target_error_component import (
            ApiV1PricingCostStatementsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_status_error_component import (
            ApiV1PricingCostStatementsArchiveCreateStatusErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_target_availability_error_component import (
            ApiV1PricingCostStatementsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_tolerations_error_component import (
            ApiV1PricingCostStatementsArchiveCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_total_net_error_component import (
            ApiV1PricingCostStatementsArchiveCreateTotalNetErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1PricingCostStatementsArchiveCreateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreatePeriodStartErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreatePeriodEndErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateTotalNetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateCurrencyErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateExternalInvoiceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateGeneratedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingCostStatementsArchiveCreateGeneratedByErrorComponent):
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
        from ..models.api_v1_pricing_cost_statements_archive_create_annotations_error_component import (
            ApiV1PricingCostStatementsArchiveCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_archived_at_error_component import (
            ApiV1PricingCostStatementsArchiveCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_archived_error_component import (
            ApiV1PricingCostStatementsArchiveCreateArchivedErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_archived_reason_error_component import (
            ApiV1PricingCostStatementsArchiveCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_criticality_error_component import (
            ApiV1PricingCostStatementsArchiveCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_currency_error_component import (
            ApiV1PricingCostStatementsArchiveCreateCurrencyErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_debug_mode_error_component import (
            ApiV1PricingCostStatementsArchiveCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_display_name_error_component import (
            ApiV1PricingCostStatementsArchiveCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_external_invoice_id_error_component import (
            ApiV1PricingCostStatementsArchiveCreateExternalInvoiceIdErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_generated_at_error_component import (
            ApiV1PricingCostStatementsArchiveCreateGeneratedAtErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_generated_by_error_component import (
            ApiV1PricingCostStatementsArchiveCreateGeneratedByErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_is_manual_error_component import (
            ApiV1PricingCostStatementsArchiveCreateIsManualErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_kind_error_component import (
            ApiV1PricingCostStatementsArchiveCreateKindErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_labels_error_component import (
            ApiV1PricingCostStatementsArchiveCreateLabelsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_name_error_component import (
            ApiV1PricingCostStatementsArchiveCreateNameErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_non_field_errors_error_component import (
            ApiV1PricingCostStatementsArchiveCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_period_end_error_component import (
            ApiV1PricingCostStatementsArchiveCreatePeriodEndErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_period_start_error_component import (
            ApiV1PricingCostStatementsArchiveCreatePeriodStartErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_platform_service_error_component import (
            ApiV1PricingCostStatementsArchiveCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_provider_error_component import (
            ApiV1PricingCostStatementsArchiveCreateProviderErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_provider_id_error_component import (
            ApiV1PricingCostStatementsArchiveCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_provider_reference_error_component import (
            ApiV1PricingCostStatementsArchiveCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_reconciliation_enabled_error_component import (
            ApiV1PricingCostStatementsArchiveCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_sla_availability_error_component import (
            ApiV1PricingCostStatementsArchiveCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_sla_target_error_component import (
            ApiV1PricingCostStatementsArchiveCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_slo_availability_error_component import (
            ApiV1PricingCostStatementsArchiveCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_slo_target_error_component import (
            ApiV1PricingCostStatementsArchiveCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_status_error_component import (
            ApiV1PricingCostStatementsArchiveCreateStatusErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_target_availability_error_component import (
            ApiV1PricingCostStatementsArchiveCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_tolerations_error_component import (
            ApiV1PricingCostStatementsArchiveCreateTolerationsErrorComponent,
        )
        from ..models.api_v1_pricing_cost_statements_archive_create_total_net_error_component import (
            ApiV1PricingCostStatementsArchiveCreateTotalNetErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingCostStatementsArchiveCreateAnnotationsErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateArchivedAtErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateArchivedErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateArchivedReasonErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateCriticalityErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateCurrencyErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateDebugModeErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateDisplayNameErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateExternalInvoiceIdErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateGeneratedAtErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateGeneratedByErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateIsManualErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateKindErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateLabelsErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateNameErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1PricingCostStatementsArchiveCreatePeriodEndErrorComponent
                | ApiV1PricingCostStatementsArchiveCreatePeriodStartErrorComponent
                | ApiV1PricingCostStatementsArchiveCreatePlatformServiceErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateProviderErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateProviderIdErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateProviderReferenceErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateSlaTargetErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateSloTargetErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateStatusErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateTolerationsErrorComponent
                | ApiV1PricingCostStatementsArchiveCreateTotalNetErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_0 = (
                        ApiV1PricingCostStatementsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_1 = (
                        ApiV1PricingCostStatementsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_2 = (
                        ApiV1PricingCostStatementsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_3 = (
                        ApiV1PricingCostStatementsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_4 = (
                        ApiV1PricingCostStatementsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_5 = (
                        ApiV1PricingCostStatementsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_6 = (
                        ApiV1PricingCostStatementsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_7 = (
                        ApiV1PricingCostStatementsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_8 = (
                        ApiV1PricingCostStatementsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_9 = (
                        ApiV1PricingCostStatementsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_10 = (
                        ApiV1PricingCostStatementsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_11 = (
                        ApiV1PricingCostStatementsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_12 = (
                        ApiV1PricingCostStatementsArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_13 = (
                        ApiV1PricingCostStatementsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_14 = (
                        ApiV1PricingCostStatementsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_15 = (
                        ApiV1PricingCostStatementsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_16 = (
                        ApiV1PricingCostStatementsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_17 = (
                        ApiV1PricingCostStatementsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_18 = (
                        ApiV1PricingCostStatementsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_19 = (
                        ApiV1PricingCostStatementsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_20 = (
                        ApiV1PricingCostStatementsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_21 = (
                        ApiV1PricingCostStatementsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_22 = (
                        ApiV1PricingCostStatementsArchiveCreatePeriodStartErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_23 = (
                        ApiV1PricingCostStatementsArchiveCreatePeriodEndErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_24 = (
                        ApiV1PricingCostStatementsArchiveCreateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_25 = (
                        ApiV1PricingCostStatementsArchiveCreateTotalNetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_26 = (
                        ApiV1PricingCostStatementsArchiveCreateCurrencyErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_27 = (
                        ApiV1PricingCostStatementsArchiveCreateExternalInvoiceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_28 = (
                        ApiV1PricingCostStatementsArchiveCreateGeneratedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_29 = (
                        ApiV1PricingCostStatementsArchiveCreateGeneratedByErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_30 = (
                    ApiV1PricingCostStatementsArchiveCreateIsManualErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_cost_statements_archive_create_error_type_30

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_cost_statements_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_cost_statements_archive_create_validation_error.additional_properties = d
        return api_v1_pricing_cost_statements_archive_create_validation_error

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
