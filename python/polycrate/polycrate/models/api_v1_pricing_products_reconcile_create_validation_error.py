from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_pricing_products_reconcile_create_annotations_error_component import (
        ApiV1PricingProductsReconcileCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_archived_at_error_component import (
        ApiV1PricingProductsReconcileCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_archived_error_component import (
        ApiV1PricingProductsReconcileCreateArchivedErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_archived_reason_error_component import (
        ApiV1PricingProductsReconcileCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_billing_interval_error_component import (
        ApiV1PricingProductsReconcileCreateBillingIntervalErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_config_error_component import (
        ApiV1PricingProductsReconcileCreateConfigErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_cost_per_unit_error_component import (
        ApiV1PricingProductsReconcileCreateCostPerUnitErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_criticality_error_component import (
        ApiV1PricingProductsReconcileCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_debug_mode_error_component import (
        ApiV1PricingProductsReconcileCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_display_name_error_component import (
        ApiV1PricingProductsReconcileCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_kind_error_component import (
        ApiV1PricingProductsReconcileCreateKindErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_labels_error_component import (
        ApiV1PricingProductsReconcileCreateLabelsErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_name_error_component import (
        ApiV1PricingProductsReconcileCreateNameErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_non_field_errors_error_component import (
        ApiV1PricingProductsReconcileCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_platform_service_error_component import (
        ApiV1PricingProductsReconcileCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_pop_error_component import (
        ApiV1PricingProductsReconcileCreatePopErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_price_per_unit_error_component import (
        ApiV1PricingProductsReconcileCreatePricePerUnitErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_provider_entity_error_component import (
        ApiV1PricingProductsReconcileCreateProviderEntityErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_provider_error_component import (
        ApiV1PricingProductsReconcileCreateProviderErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_provider_id_error_component import (
        ApiV1PricingProductsReconcileCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_provider_reference_error_component import (
        ApiV1PricingProductsReconcileCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_provider_type_id_error_component import (
        ApiV1PricingProductsReconcileCreateProviderTypeIdErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_reconciliation_enabled_error_component import (
        ApiV1PricingProductsReconcileCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_sla_availability_error_component import (
        ApiV1PricingProductsReconcileCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_sla_target_error_component import (
        ApiV1PricingProductsReconcileCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_slo_availability_error_component import (
        ApiV1PricingProductsReconcileCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_slo_target_error_component import (
        ApiV1PricingProductsReconcileCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_target_availability_error_component import (
        ApiV1PricingProductsReconcileCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_pricing_products_reconcile_create_tolerations_error_component import (
        ApiV1PricingProductsReconcileCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1PricingProductsReconcileCreateValidationError")


@_attrs_define
class ApiV1PricingProductsReconcileCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1PricingProductsReconcileCreateAnnotationsErrorComponent |
            ApiV1PricingProductsReconcileCreateArchivedAtErrorComponent |
            ApiV1PricingProductsReconcileCreateArchivedErrorComponent |
            ApiV1PricingProductsReconcileCreateArchivedReasonErrorComponent |
            ApiV1PricingProductsReconcileCreateBillingIntervalErrorComponent |
            ApiV1PricingProductsReconcileCreateConfigErrorComponent |
            ApiV1PricingProductsReconcileCreateCostPerUnitErrorComponent |
            ApiV1PricingProductsReconcileCreateCriticalityErrorComponent |
            ApiV1PricingProductsReconcileCreateDebugModeErrorComponent |
            ApiV1PricingProductsReconcileCreateDisplayNameErrorComponent |
            ApiV1PricingProductsReconcileCreateKindErrorComponent | ApiV1PricingProductsReconcileCreateLabelsErrorComponent
            | ApiV1PricingProductsReconcileCreateNameErrorComponent |
            ApiV1PricingProductsReconcileCreateNonFieldErrorsErrorComponent |
            ApiV1PricingProductsReconcileCreatePlatformServiceErrorComponent |
            ApiV1PricingProductsReconcileCreatePopErrorComponent |
            ApiV1PricingProductsReconcileCreatePricePerUnitErrorComponent |
            ApiV1PricingProductsReconcileCreateProviderEntityErrorComponent |
            ApiV1PricingProductsReconcileCreateProviderErrorComponent |
            ApiV1PricingProductsReconcileCreateProviderIdErrorComponent |
            ApiV1PricingProductsReconcileCreateProviderReferenceErrorComponent |
            ApiV1PricingProductsReconcileCreateProviderTypeIdErrorComponent |
            ApiV1PricingProductsReconcileCreateReconciliationEnabledErrorComponent |
            ApiV1PricingProductsReconcileCreateSlaAvailabilityErrorComponent |
            ApiV1PricingProductsReconcileCreateSlaTargetErrorComponent |
            ApiV1PricingProductsReconcileCreateSloAvailabilityErrorComponent |
            ApiV1PricingProductsReconcileCreateSloTargetErrorComponent |
            ApiV1PricingProductsReconcileCreateTargetAvailabilityErrorComponent |
            ApiV1PricingProductsReconcileCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1PricingProductsReconcileCreateAnnotationsErrorComponent
        | ApiV1PricingProductsReconcileCreateArchivedAtErrorComponent
        | ApiV1PricingProductsReconcileCreateArchivedErrorComponent
        | ApiV1PricingProductsReconcileCreateArchivedReasonErrorComponent
        | ApiV1PricingProductsReconcileCreateBillingIntervalErrorComponent
        | ApiV1PricingProductsReconcileCreateConfigErrorComponent
        | ApiV1PricingProductsReconcileCreateCostPerUnitErrorComponent
        | ApiV1PricingProductsReconcileCreateCriticalityErrorComponent
        | ApiV1PricingProductsReconcileCreateDebugModeErrorComponent
        | ApiV1PricingProductsReconcileCreateDisplayNameErrorComponent
        | ApiV1PricingProductsReconcileCreateKindErrorComponent
        | ApiV1PricingProductsReconcileCreateLabelsErrorComponent
        | ApiV1PricingProductsReconcileCreateNameErrorComponent
        | ApiV1PricingProductsReconcileCreateNonFieldErrorsErrorComponent
        | ApiV1PricingProductsReconcileCreatePlatformServiceErrorComponent
        | ApiV1PricingProductsReconcileCreatePopErrorComponent
        | ApiV1PricingProductsReconcileCreatePricePerUnitErrorComponent
        | ApiV1PricingProductsReconcileCreateProviderEntityErrorComponent
        | ApiV1PricingProductsReconcileCreateProviderErrorComponent
        | ApiV1PricingProductsReconcileCreateProviderIdErrorComponent
        | ApiV1PricingProductsReconcileCreateProviderReferenceErrorComponent
        | ApiV1PricingProductsReconcileCreateProviderTypeIdErrorComponent
        | ApiV1PricingProductsReconcileCreateReconciliationEnabledErrorComponent
        | ApiV1PricingProductsReconcileCreateSlaAvailabilityErrorComponent
        | ApiV1PricingProductsReconcileCreateSlaTargetErrorComponent
        | ApiV1PricingProductsReconcileCreateSloAvailabilityErrorComponent
        | ApiV1PricingProductsReconcileCreateSloTargetErrorComponent
        | ApiV1PricingProductsReconcileCreateTargetAvailabilityErrorComponent
        | ApiV1PricingProductsReconcileCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_pricing_products_reconcile_create_annotations_error_component import (
            ApiV1PricingProductsReconcileCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_archived_at_error_component import (
            ApiV1PricingProductsReconcileCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_archived_error_component import (
            ApiV1PricingProductsReconcileCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_archived_reason_error_component import (
            ApiV1PricingProductsReconcileCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_billing_interval_error_component import (
            ApiV1PricingProductsReconcileCreateBillingIntervalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_cost_per_unit_error_component import (
            ApiV1PricingProductsReconcileCreateCostPerUnitErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_criticality_error_component import (
            ApiV1PricingProductsReconcileCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_debug_mode_error_component import (
            ApiV1PricingProductsReconcileCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_display_name_error_component import (
            ApiV1PricingProductsReconcileCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_kind_error_component import (
            ApiV1PricingProductsReconcileCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_labels_error_component import (
            ApiV1PricingProductsReconcileCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_name_error_component import (
            ApiV1PricingProductsReconcileCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_non_field_errors_error_component import (
            ApiV1PricingProductsReconcileCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_platform_service_error_component import (
            ApiV1PricingProductsReconcileCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_pop_error_component import (
            ApiV1PricingProductsReconcileCreatePopErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_price_per_unit_error_component import (
            ApiV1PricingProductsReconcileCreatePricePerUnitErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_provider_entity_error_component import (
            ApiV1PricingProductsReconcileCreateProviderEntityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_provider_error_component import (
            ApiV1PricingProductsReconcileCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_provider_id_error_component import (
            ApiV1PricingProductsReconcileCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_provider_reference_error_component import (
            ApiV1PricingProductsReconcileCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_provider_type_id_error_component import (
            ApiV1PricingProductsReconcileCreateProviderTypeIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_reconciliation_enabled_error_component import (
            ApiV1PricingProductsReconcileCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_sla_availability_error_component import (
            ApiV1PricingProductsReconcileCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_sla_target_error_component import (
            ApiV1PricingProductsReconcileCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_slo_availability_error_component import (
            ApiV1PricingProductsReconcileCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_slo_target_error_component import (
            ApiV1PricingProductsReconcileCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_target_availability_error_component import (
            ApiV1PricingProductsReconcileCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_tolerations_error_component import (
            ApiV1PricingProductsReconcileCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateBillingIntervalErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreatePricePerUnitErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateCostPerUnitErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateProviderEntityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreatePopErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1PricingProductsReconcileCreateProviderTypeIdErrorComponent):
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
        from ..models.api_v1_pricing_products_reconcile_create_annotations_error_component import (
            ApiV1PricingProductsReconcileCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_archived_at_error_component import (
            ApiV1PricingProductsReconcileCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_archived_error_component import (
            ApiV1PricingProductsReconcileCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_archived_reason_error_component import (
            ApiV1PricingProductsReconcileCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_billing_interval_error_component import (
            ApiV1PricingProductsReconcileCreateBillingIntervalErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_config_error_component import (
            ApiV1PricingProductsReconcileCreateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_cost_per_unit_error_component import (
            ApiV1PricingProductsReconcileCreateCostPerUnitErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_criticality_error_component import (
            ApiV1PricingProductsReconcileCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_debug_mode_error_component import (
            ApiV1PricingProductsReconcileCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_display_name_error_component import (
            ApiV1PricingProductsReconcileCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_kind_error_component import (
            ApiV1PricingProductsReconcileCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_labels_error_component import (
            ApiV1PricingProductsReconcileCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_name_error_component import (
            ApiV1PricingProductsReconcileCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_non_field_errors_error_component import (
            ApiV1PricingProductsReconcileCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_platform_service_error_component import (
            ApiV1PricingProductsReconcileCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_pop_error_component import (
            ApiV1PricingProductsReconcileCreatePopErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_price_per_unit_error_component import (
            ApiV1PricingProductsReconcileCreatePricePerUnitErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_provider_entity_error_component import (
            ApiV1PricingProductsReconcileCreateProviderEntityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_provider_error_component import (
            ApiV1PricingProductsReconcileCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_provider_id_error_component import (
            ApiV1PricingProductsReconcileCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_provider_reference_error_component import (
            ApiV1PricingProductsReconcileCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_provider_type_id_error_component import (
            ApiV1PricingProductsReconcileCreateProviderTypeIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_reconciliation_enabled_error_component import (
            ApiV1PricingProductsReconcileCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_sla_availability_error_component import (
            ApiV1PricingProductsReconcileCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_sla_target_error_component import (
            ApiV1PricingProductsReconcileCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_slo_availability_error_component import (
            ApiV1PricingProductsReconcileCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_slo_target_error_component import (
            ApiV1PricingProductsReconcileCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_target_availability_error_component import (
            ApiV1PricingProductsReconcileCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_pricing_products_reconcile_create_tolerations_error_component import (
            ApiV1PricingProductsReconcileCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1PricingProductsReconcileCreateAnnotationsErrorComponent
                | ApiV1PricingProductsReconcileCreateArchivedAtErrorComponent
                | ApiV1PricingProductsReconcileCreateArchivedErrorComponent
                | ApiV1PricingProductsReconcileCreateArchivedReasonErrorComponent
                | ApiV1PricingProductsReconcileCreateBillingIntervalErrorComponent
                | ApiV1PricingProductsReconcileCreateConfigErrorComponent
                | ApiV1PricingProductsReconcileCreateCostPerUnitErrorComponent
                | ApiV1PricingProductsReconcileCreateCriticalityErrorComponent
                | ApiV1PricingProductsReconcileCreateDebugModeErrorComponent
                | ApiV1PricingProductsReconcileCreateDisplayNameErrorComponent
                | ApiV1PricingProductsReconcileCreateKindErrorComponent
                | ApiV1PricingProductsReconcileCreateLabelsErrorComponent
                | ApiV1PricingProductsReconcileCreateNameErrorComponent
                | ApiV1PricingProductsReconcileCreateNonFieldErrorsErrorComponent
                | ApiV1PricingProductsReconcileCreatePlatformServiceErrorComponent
                | ApiV1PricingProductsReconcileCreatePopErrorComponent
                | ApiV1PricingProductsReconcileCreatePricePerUnitErrorComponent
                | ApiV1PricingProductsReconcileCreateProviderEntityErrorComponent
                | ApiV1PricingProductsReconcileCreateProviderErrorComponent
                | ApiV1PricingProductsReconcileCreateProviderIdErrorComponent
                | ApiV1PricingProductsReconcileCreateProviderReferenceErrorComponent
                | ApiV1PricingProductsReconcileCreateProviderTypeIdErrorComponent
                | ApiV1PricingProductsReconcileCreateReconciliationEnabledErrorComponent
                | ApiV1PricingProductsReconcileCreateSlaAvailabilityErrorComponent
                | ApiV1PricingProductsReconcileCreateSlaTargetErrorComponent
                | ApiV1PricingProductsReconcileCreateSloAvailabilityErrorComponent
                | ApiV1PricingProductsReconcileCreateSloTargetErrorComponent
                | ApiV1PricingProductsReconcileCreateTargetAvailabilityErrorComponent
                | ApiV1PricingProductsReconcileCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_0 = (
                        ApiV1PricingProductsReconcileCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_1 = (
                        ApiV1PricingProductsReconcileCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_2 = (
                        ApiV1PricingProductsReconcileCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_3 = (
                        ApiV1PricingProductsReconcileCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_4 = (
                        ApiV1PricingProductsReconcileCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_5 = (
                        ApiV1PricingProductsReconcileCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_6 = (
                        ApiV1PricingProductsReconcileCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_7 = (
                        ApiV1PricingProductsReconcileCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_8 = (
                        ApiV1PricingProductsReconcileCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_9 = (
                        ApiV1PricingProductsReconcileCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_10 = (
                        ApiV1PricingProductsReconcileCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_11 = (
                        ApiV1PricingProductsReconcileCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_12 = (
                        ApiV1PricingProductsReconcileCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_13 = (
                        ApiV1PricingProductsReconcileCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_14 = (
                        ApiV1PricingProductsReconcileCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_15 = (
                        ApiV1PricingProductsReconcileCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_16 = (
                        ApiV1PricingProductsReconcileCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_17 = (
                        ApiV1PricingProductsReconcileCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_18 = (
                        ApiV1PricingProductsReconcileCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_19 = (
                        ApiV1PricingProductsReconcileCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_20 = (
                        ApiV1PricingProductsReconcileCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_21 = (
                        ApiV1PricingProductsReconcileCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_22 = (
                        ApiV1PricingProductsReconcileCreateBillingIntervalErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_23 = (
                        ApiV1PricingProductsReconcileCreatePricePerUnitErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_24 = (
                        ApiV1PricingProductsReconcileCreateCostPerUnitErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_25 = (
                        ApiV1PricingProductsReconcileCreateProviderEntityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_26 = (
                        ApiV1PricingProductsReconcileCreatePopErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_pricing_products_reconcile_create_error_type_27 = (
                        ApiV1PricingProductsReconcileCreateProviderTypeIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_pricing_products_reconcile_create_error_type_28 = (
                    ApiV1PricingProductsReconcileCreateConfigErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_pricing_products_reconcile_create_error_type_28

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_pricing_products_reconcile_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_pricing_products_reconcile_create_validation_error.additional_properties = d
        return api_v1_pricing_products_reconcile_create_validation_error

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
